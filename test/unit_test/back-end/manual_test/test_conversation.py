import asyncio
import json
from pathlib import Path

from re_edge_gpt import Chatbot
from re_edge_gpt import ConversationStyle

# If you are using jupyter pls install this package
# from nest_asyncio import apply

conversation_dict = {}


async def test_ask() -> None:
    bot = None
    try:
        cookies: list[dict] = json.loads(open(
            str(Path(str(Path.cwd()) + "/bing_cookies.json")), encoding="utf-8").read())
        bot = await Chatbot.create(cookies=cookies)
        response = await bot.ask(
            prompt="Translate next word what I say to english",
            conversation_style=ConversationStyle.balanced,
            simplify_response=True
        )
        # If you are using non ascii char you need set ensure_ascii=False
        print(json.dumps(response, indent=2, ensure_ascii=False))
        print(await bot.chat_hub.get_conversation())
        conversation_dict.update(await bot.chat_hub.get_conversation())
    except Exception as error:
        raise error
    finally:
        if bot is not None:
            await bot.close()


async def test_ask_conversation() -> None:
    bot = None
    try:
        cookies: list[dict] = json.loads(open(
            str(Path(str(Path.cwd()) + "/bing_cookies.json")), encoding="utf-8").read())
        bot = await Chatbot.create(cookies=cookies)
        await bot.chat_hub.set_conversation(conversation_dict=conversation_dict)
        response = await bot.ask(
            prompt="піца",
            conversation_style=ConversationStyle.balanced,
            simplify_response=True
        )
        # If you are using non ascii char you need set ensure_ascii=False
        print(json.dumps(response, indent=2, ensure_ascii=False))
    except Exception as error:
        raise error
    finally:
        if bot is not None:
            await bot.close()


if __name__ == "__main__":
    # If you are using jupyter pls use nest_asyncio apply()
    # apply()
    try:
        loop = asyncio.get_running_loop()
    except RuntimeError:
        loop = asyncio.get_event_loop()
    loop.run_until_complete(test_ask())
    loop.run_until_complete(test_ask_conversation())
