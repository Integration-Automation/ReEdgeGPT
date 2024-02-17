import asyncio
import json
from os import getenv
from pathlib import Path

from re_edge_gpt import Chatbot
from re_edge_gpt import ConversationStyle


# If you are using jupyter pls install this package
# from nest_asyncio import apply


async def test_ask() -> None:
    bot = None
    try:
        bot = await Chatbot.create(cookies=json.loads(getenv("EDGE_COOKIES")))
        response = await bot.ask(
            prompt="What does this image show?",
            conversation_style=ConversationStyle.balanced,
            simplify_response=True,
            attachment={"filename": "test.jpg"})
        # If you are using non ascii char you need set ensure_ascii=False
        print(json.dumps(response, indent=2, ensure_ascii=False))
        # Raw response
        # print(response)
        assert response
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
