import argparse
import asyncio
import json
import re
import sys
from pathlib import Path

from prompt_toolkit import PromptSession
from prompt_toolkit.auto_suggest import AutoSuggestFromHistory
from prompt_toolkit.completion import WordCompleter
from prompt_toolkit.history import InMemoryHistory
from prompt_toolkit.key_binding import KeyBindings

from re_edge_gpt.chat.re_edge_gpt import Chatbot


def create_session() -> PromptSession:
    kb = KeyBindings()

    @kb.add("enter")
    def _(event) -> None:
        buffer_text = event.current_buffer.text
        if buffer_text.startswith("!"):
            event.current_buffer.validate_and_handle()
        else:
            event.current_buffer.insert_text("\n")

    @kb.add("escape")
    def _(event) -> None:
        if event.current_buffer.complete_state:
            # event.current_buffer.cancel_completion()
            event.current_buffer.text = ""

    return PromptSession(key_bindings=kb, history=InMemoryHistory())


def create_completer(commands: list, pattern_str: str = "$") -> WordCompleter:
    return WordCompleter(words=commands, pattern=re.compile(pattern_str))


def _create_history_logger(f) -> callable:
    def logger(*args, **kwargs) -> None:
        tmp = sys.stdout
        sys.stdout = f
        print(*args, **kwargs, flush=True)
        sys.stdout = tmp

    return logger


async def get_input_async(
        session: PromptSession = None,
        completer: WordCompleter = None,
) -> str:
    """
    Multiline input function.
    """
    return await session.prompt_async(
        completer=completer,
        multiline=True,
        auto_suggest=AutoSuggestFromHistory(),
    )


async def async_main(args: argparse.Namespace) -> None:
    """
    Main function
    options:
        enter-once
        search-result
        no-stream
        rich
        proxy: Proxy service
        wss-link: websocket link to connect to ChatHub
        style: Copilot Chat style
        prompt: Chat prompt
        cookie-file: cookie file path
        locale: locale ISO Language Codes
    """
    print("Initializing...")
    print("Enter `alt+enter` or `escape+enter` to send a message")
    # Read and parse cookies
    cookies = None
    if args.cookie_file:
        file_path = Path(args.cookie_file)
        if file_path.exists():
            with file_path.open("r", encoding="utf-8") as f:
                cookies = json.load(f)
    bot = await Chatbot.create(proxy=args.proxy, cookies=cookies)
    session = create_session()
    completer = create_completer(["!help", "!exit", "!reset"])
    initial_prompt = args.prompt

    while True:
        print("\nYou:")
        if initial_prompt:
            question = initial_prompt
            print(question)
            initial_prompt = None
        else:
            question = (
                input()
                if args.enter_once
                else await get_input_async(session=session, completer=completer)
            )
        print()
        if question == "!exit":
            await bot.close()
            break
        if question == "!help":
            print(
                """
            !help - Show this help message
            !exit - Exit the program
            !reset - Reset the conversation
            """,
            )
            continue
        if question == "!reset":
            await bot.reset()
            continue
        print("Bot:")
        response = await bot.ask(
                prompt=question,
                conversation_style=args.style,
                wss_link=args.wss_link,
                locale=args.locale,
                simplify_response=True
            )
        print(response.get("text", "No response"))
    await bot.close()


def main() -> None:
    print(
        """
        ReEdgeGPT - A demo of reverse engineering the Bing GPT chatbot

        !help for help

        Type !exit to exit
    """,
    )
    parser = argparse.ArgumentParser()
    parser.add_argument("--enter-once", action="store_true")
    parser.add_argument("--search-result", action="store_true")
    parser.add_argument("--no-stream", action="store_true")
    parser.add_argument("--rich", action="store_true")
    parser.add_argument(
        "--proxy",
        help="Proxy URL (e.g. socks5://127.0.0.1:1080)",
        type=str,
    )
    parser.add_argument(
        "--wss-link",
        help="WSS URL(e.g. wss://sydney.bing.com/sydney/ChatHub)",
        type=str,
        default="wss://sydney.bing.com/sydney/ChatHub",
    )
    parser.add_argument(
        "--style",
        choices=["creative", "balanced", "precise"],
        default="balanced",
    )
    parser.add_argument(
        "--prompt",
        type=str,
        default="",
        required=False,
        help="prompt to start with",
    )
    parser.add_argument(
        "--cookie-file",
        type=str,
        default="",
        required=False,
        help="path to cookie file",
    )
    parser.add_argument(
        "--locale",
        type=str,
        default="en-US",
        required=False,
        help="your locale",
    )
    args = parser.parse_args()
    asyncio.run(async_main(args))


if __name__ == "__main__":
    main()
