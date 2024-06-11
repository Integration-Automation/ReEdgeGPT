ReEdgeGPT 擴充範例
----

ReEdgeGPT 可以使用在以下系統上 [GUI, API, Dockerfile] 等等.

下面是在此專案裡的一些範例:

- API & Dockerfiles 範例
 - Dockerfiles/Flask
 - test/unit_test/api
 - re_edge_gpt/api

- UI 範例
 - test/unit_test/ui
 - re_edge_gpt/ui

- Discord 機器人範例

.. code-block:: python

    import json
    import socket
    from pathlib import Path

    import discord
    import requests
    from re_edge_gpt import Chatbot, ConversationStyle, ImageGenAsync

    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)
    auth_cooker = open("bing_cookies.txt", "r+").read()
    async_gen = ImageGenAsync(auth_cookie=auth_cooker)


    class ChatDelegate(object):

        def __init__(self):
            self.chat_bot = None
            self.mode_setting = {
                ConversationStyle.creative,
                ConversationStyle.balanced,
                ConversationStyle.precise
            }
            self.mode = ConversationStyle.creative


    CHAT_DELEGATE = ChatDelegate()


    @client.event
    async def on_ready():
        print(f"We have logged in as {client.user}")


    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        if message.content.startswith("$CHAT"):
            content_string = message.content.replace("$CHAT", "")
            if CHAT_DELEGATE.chat_bot is None:
                cookies = json.loads(open(
                    str(Path(str(Path.cwd()) + "/bing_cookies.json")), encoding="utf-8").read())
                chat_bot = await Chatbot.create(cookies=cookies)
                response = await chat_bot.ask(
                    prompt=content_string, conversation_style=ConversationStyle.creative)
            else:
                chat_bot = CHAT_DELEGATE.chat_bot
                response = await CHAT_DELEGATE.chat_bot.ask(
                    prompt=content_string, conversation_style=ConversationStyle.creative)
            discord_response = "No response"
            for text_dict in response.get("item").get("messages"):
                if text_dict.get("author") == "bot":
                    discord_response = text_dict.get("text")
            CHAT_DELEGATE.chat_bot = chat_bot
            await message.channel.send(discord_response)

        if message.content.startswith("$IMAGE"):
            content_string = message.content.replace("$IMAGE", "")
            try:
                for image in await async_gen.get_images(content_string):
                    await message.channel.send(image)
            except Exception as error:
                await message.channel.send(error)

        if message.content.startswith("$NEW_TOPIC"):
            CHAT_DELEGATE.chat_bot = None


    client.run("Your token")
