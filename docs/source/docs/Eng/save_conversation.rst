ReEdgeGPT Save Conversation
----

.. code-block:: python

    import asyncio
    import json
    from pathlib import Path

    from re_edge_gpt import Chatbot
    from re_edge_gpt import ConversationStyle

    # If you are using jupyter pls install this package
    # from nest_asyncio import apply

    conversation_dict = {}
    cookies: list[dict] = json.loads(open(str(Path(str(Path.cwd()) + "/bing_cookies.json")), encoding="utf-8").read())


    async def test_ask(chatbot: Chatbot) -> None:
        try:

            response = await chatbot.ask(
                prompt="Translate next word what I say to english",
                conversation_style=ConversationStyle.balanced,
                simplify_response=True
            )
            # If you are using non ascii char you need set ensure_ascii=False
            print(json.dumps(response, indent=2, ensure_ascii=False))
            print(await chatbot.chat_hub.get_conversation())
            conversation_dict.update(await chatbot.chat_hub.get_conversation())
        except Exception as error:
            raise error


    async def test_ask_conversation(chatbot: Chatbot) -> None:

        try:
            await chatbot.chat_hub.set_conversation(conversation_dict=conversation_dict)
            response = await chatbot.ask(
                prompt="піца",
                conversation_style=ConversationStyle.balanced,
                simplify_response=True
            )
            # If you are using non ascii char you need set ensure_ascii=False
            print(json.dumps(response, indent=2, ensure_ascii=False))
        except Exception as error:
            raise error


    async def create_chatbot():
        chatbot = await Chatbot.create(cookies=cookies)
        return chatbot

    if __name__ == "__main__":
        # If you are using jupyter pls use nest_asyncio apply()
        # apply()
        try:
            loop = asyncio.get_running_loop()
        except RuntimeError:
            loop = asyncio.get_event_loop()
        bot = loop.run_until_complete(create_chatbot())
        loop.run_until_complete(test_ask(bot))
        loop.run_until_complete(test_ask_conversation(bot))
