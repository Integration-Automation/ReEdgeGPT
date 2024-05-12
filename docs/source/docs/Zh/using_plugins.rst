ReEdgeGPT 使用插件
----
支援的插件:
Notebook id: c310c353-b9f0-4d76-ab0d-1dd5e979cf68
Instacart id: 46664d33-1591-4ce8-b3fb-ba1022b66c11
Kayak id: d6be744c-2bd9-432f-95b7-76e103946e34
Klarna id: 5f143ea3-8c80-4efd-9515-185e83b7cf8a
Opentable id: 543a7b1b-ebc6-46f4-be76-00c202990a1b
Shop id: 39e3566a-d481-4d99-82b2-6d739b1e716e
Suno id: 22b7f79d-8ea4-437e-b5fd-3e21f09f7bc1

使用 Suno 的範例:

.. code-block:: python

    import asyncio
    import json
    from pathlib import Path

    from re_edge_gpt import Chatbot
    from re_edge_gpt import ConversationStyle
    from re_edge_gpt.plugins.suno import generate_suno_music


    # If you are using jupyter pls install this package
    # from nest_asyncio import apply


    async def test_ask() -> None:
        bot = None
        try:
            cookies: list[dict] = json.loads(open(
                str(Path(str(Path.cwd()) + "/bing_cookies.json")), encoding="utf-8").read())
            bot = await Chatbot.create(cookies=cookies, mode="Bing", plugin_ids=["suno"])
            prompt = """Can you create some epic music"""
            response = await bot.ask(
                prompt=prompt,
                conversation_style=ConversationStyle.balanced,
                simplify_response=True,
                add_options=["014CB21D"],
                plugins=[{"Id": "c310c353-b9f0-4d76-ab0d-1dd5e979cf68", "Category": 1}],
                message_type="GenerateContentQuery"
            )
            # Notice! only simplify_response=True return messageId & requestId
            # If you are using raw response you need self get it.
            # If you are using non ascii char you need set ensure_ascii=False
            print(json.dumps(response, indent=2, ensure_ascii=False))
            print(await generate_suno_music(cookies, response.get("messageId"), response.get("requestId")))
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

