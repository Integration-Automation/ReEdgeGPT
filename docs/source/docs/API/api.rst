ReEdgeGPT API
----

.. code-block:: python

    async def save_conversation(self, filename: str) -> None:
        """
        Save the conversation to a file
        """

.. code-block:: python

    async def load_conversation(self, filename: str) -> None:
        """
        Load the conversation from a file
        """

.. code-block:: python

    async def get_conversation(self) -> dict:
        """
        Gets the conversation history from conversation_id (requires load_conversation)
        """

.. code-block:: python

    async def get_activity(self) -> dict:
        """
        Gets the recent activity (requires cookies)
        """

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
    ):
        """
        Ask a question to the bot
        Response:
            {
                item (dict):
                    messages (list[dict]):
                        adaptiveCards (list[dict]):
                            body (list[dict]):
                                text (str): Response
            }
        To get the response, you can do:
            response["item"]["messages"][1]["adaptiveCards"][0]["body"][0]["text"]
        """

.. code-block:: python

    async def ask_stream(
            self,
            prompt: str,
            wss_link: str = "wss://sydney.bing.com/sydney/ChatHub",
            conversation_style: CONVERSATION_STYLE_TYPE = None,
            raw: bool = False,
            webpage_context: str | None = None,
            search_result: bool = False,
            locale: str = guess_locale(),
    ) -> Generator[bool, dict | str, None]:
        """
        Ask a question to the bot
        """

.. code-block:: python

    async def close(self) -> None:
        """
        Close the connection
        """

.. code-block:: python

    async def delete_conversation(
            self,
            conversation_id: str = None,
            conversation_signature: str = None,
            client_id: str = None,
    ) -> None:
        """
        Delete the chat in the server
        """

.. code-block:: python

    async def reset(self) -> None:
        """
        Reset the conversation
        """
