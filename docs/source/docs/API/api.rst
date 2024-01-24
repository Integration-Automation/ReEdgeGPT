ReEdgeGPT API
----

.. code-block:: python

    async def get_conversation(self) -> dict:
    """
    Save the conversation to a dict
    conversation_dict: use to save conversation
    bot: ReEdgeGPT instance
    cookies: cookie dict
    example below:
    """
    conversation_dict = {}
    bot = None
    cookies: list[dict] = json.loads(open(
        str(Path(str(Path.cwd()) + "/bing_cookies.json")), encoding="utf-8").read())
    bot = await Chatbot.create(cookies=cookies)
    conversation_dict.update(await bot.chat_hub.get_conversation())

.. code-block:: python

    async def set_conversation(self, conversation_dict: dict):
    """
    Load the conversation from a dict
    bot: ReEdgeGPT instance
    cookies: cookie dict
    example below:
    """
    bot = None
    cookies: list[dict] = json.loads(open(
        str(Path(str(Path.cwd()) + "/bing_cookies.json")), encoding="utf-8").read())
    bot = await Chatbot.create(cookies=cookies)
    await bot.chat_hub.set_conversation(conversation_dict=conversation_dict)

.. code-block:: python

    async def ask(
            self,
            prompt: str,
            wss_link: str = "wss://sydney.bing.com/sydney/ChatHub",
            conversation_style: CONVERSATION_STYLE_TYPE = None,
            webpage_context: str | None = None,
            search_result: bool = False,
            locale: str = guess_locale(),
            simplify_response: bool = False,
            attachment: dict[str, str] = None
    ):
        """
        Ask a question to the bot
        :param prompt: The prompt to ask Bing
        :param wss_link: The link to the Bing web service
        :param conversation_style: The style of the Bing chat
        :param webpage_context: U don't need use this param in normal use
        :param search_result: Search web True or False
        :param locale: Bing service locale
        :param simplify_response: Simplify response True or False
        :param attachment: Send image
            attachment example:
                For url using
                attachment={"image_url": r"<image_url>"})
                For local file using
                attachment={"filename": r"<file_path>"})
                For base64 image using
                attachment={"base64_image": r"<base64_image_str>"})
        """

.. code-block:: python

    async def close(self) -> None:
        """
        Close the connection
        """

.. code-block:: python

    async def reset(self) -> None:
        """
        Reset the conversation
        """
