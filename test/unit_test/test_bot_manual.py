import asyncio
import json
from pathlib import Path

from re_edge_gpt import Chatbot
from re_edge_gpt import ConversationStyle


async def test_ask() -> None:
    cookies = json.loads(open(
        str(Path(str(Path.cwd()) + "/bing_cookies.json")), encoding="utf-8").read())
    bot = await Chatbot.create(cookies=cookies)
    response = await bot.ask(
        prompt="find me some information about the new ai released by meta.",
        conversation_style=ConversationStyle.balanced,
        simplify_response=True,
    )
    await bot.close()
    print(json.dumps(response, indent=2))
    assert response


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(test_ask())
