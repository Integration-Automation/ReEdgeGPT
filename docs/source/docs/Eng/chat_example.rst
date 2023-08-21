ReEdgeGPT Chat Example
----

.. code-block:: python

    import asyncio
    import json
    from pathlib import Path

    from re_edge_gpt import Chatbot
    from re_edge_gpt import ConversationStyle


    async def test_ask() -> None:
        # Read local bing_cookies.json (if you don't have this file please read README)
        cookies = json.loads(open(
            str(Path(str(Path.cwd()) + "/bing_cookies.json")), encoding="utf-8").read())
        # init BOT
        bot = await Chatbot.create(cookies=cookies)
        # Start chat and get Bing response
        response = await bot.ask(
            prompt="Hello.",
            conversation_style=ConversationStyle.balanced,
            simplify_response=True,
        )
        print(json.dumps(response, indent=2))
        response = await bot.ask(
            prompt="How do I make a cake?",
            conversation_style=ConversationStyle.balanced,
            simplify_response=True,
        )
        print(json.dumps(response, indent=2))
        response = await bot.ask(
            prompt="Can you suggest me an easy recipe for beginners?",
            conversation_style=ConversationStyle.balanced,
            simplify_response=True,
        )
        print(json.dumps(response, indent=2))
        response = await bot.ask(
            prompt="Thanks",
            conversation_style=ConversationStyle.balanced,
            simplify_response=True,
        )
        print(json.dumps(response, indent=2))
        # Close bot
        await bot.close()

    if __name__ == "__main__":
        loop = asyncio.get_event_loop()
        loop.run_until_complete(test_ask())
