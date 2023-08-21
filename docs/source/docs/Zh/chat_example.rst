ReEdgeGPT 對話範例
----

.. code-block:: python

    import asyncio
    import json
    from pathlib import Path

    from re_edge_gpt import Chatbot
    from re_edge_gpt import ConversationStyle


    async def test_ask() -> None:
        # 取得本地 bing_cookies.json (沒有請讀 README)
        cookies = json.loads(open(
            str(Path(str(Path.cwd()) + "/bing_cookies.json")), encoding="utf-8").read())
        # 初始化 BOT
        bot = await Chatbot.create(cookies=cookies)
        # 開始對話並取得 Bing 回應
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
        # 關閉對話
        await bot.close()

    if __name__ == "__main__":
        loop = asyncio.get_event_loop()
        loop.run_until_complete(test_ask())
