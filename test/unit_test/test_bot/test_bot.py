import asyncio
import json
from os import getenv

from re_edge_gpt import Chatbot
from re_edge_gpt import ConversationStyle


async def test_ask() -> None:
    bot = await Chatbot.create(cookies=json.loads(getenv("EDGE_COOKIES")))
    response = await bot.ask(
        prompt="find me some information about the new ai released by meta.",
        conversation_style=ConversationStyle.balanced
    )
    await bot.close()
    print(json.dumps(response, indent=2))
    assert response


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(test_ask())
