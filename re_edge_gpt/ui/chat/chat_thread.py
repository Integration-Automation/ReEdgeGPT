import asyncio
import json
from pathlib import Path
from queue import Queue
from threading import Thread

from re_edge_gpt import Chatbot, ConversationStyle
from PySide6.QtWidgets import QPlainTextEdit


class DelegateChat(object):

    def __init__(self):
        self.chat_bot = None
        self.style = ConversationStyle.creative

    def new_topic(self, message_panel: QPlainTextEdit):
        self.chat_bot = None
        message_panel.clear()

    def change_style(self, style: str):
        if style == "creative":
            self.style = ConversationStyle.creative
        elif style == "precise":
            self.style = ConversationStyle.precise
        else:
            self.style = ConversationStyle.balanced


class ChatThread(Thread):

    def __init__(self, chat_send_message: str, locale: str):
        super().__init__()
        self.current_message = None
        self.chat_send_message = chat_send_message
        PANEL_MESSAGE_QUEUE.put_nowait("Q: " + chat_send_message)
        self.locale = locale
        if DELEGATE_CHAT.chat_bot is not None:
            self.chat_bot = DELEGATE_CHAT.chat_bot

    def run(self) -> None:
        try:
            chat_response = dict()

            async def send_chat_async():
                nonlocal chat_response
                if DELEGATE_CHAT.chat_bot is None:
                    cookies = json.loads(open(
                        str(Path(str(Path.cwd()) + "/bing_cookies.json")), encoding="utf-8").read())
                    bot = await Chatbot.create(cookies=cookies)
                    response = await bot.ask(
                        prompt=self.chat_send_message, conversation_style=DELEGATE_CHAT.style, locale=self.locale
                    )
                    chat_response = response
                    DELEGATE_CHAT.chat_bot = bot
                else:
                    response = await DELEGATE_CHAT.chat_bot.ask(
                        prompt=self.chat_send_message, conversation_style=DELEGATE_CHAT.style)
                    chat_response = response

            asyncio.run(send_chat_async())
            self.current_message = chat_response
            if self.current_message is not None:
                for text_dict in self.current_message.get("item").get("messages"):
                    if text_dict.get("author") == "bot":
                        response_text: str = text_dict.get("text")
                        if response_text is not None and not response_text.isspace():
                            MESSAGE_QUEUE.put_nowait(response_text)
                            PANEL_MESSAGE_QUEUE.put_nowait("A: " + response_text)
        except Exception as error:
            EXCEPTION_QUEUE.put_nowait(repr(error))
            raise error


MESSAGE_QUEUE = Queue()
PANEL_MESSAGE_QUEUE = Queue()
DELEGATE_CHAT = DelegateChat()
EXCEPTION_QUEUE = Queue()