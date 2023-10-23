Q&A
----

Details

.. code-block:: markdown

    * Q: RuntimeError: This event loop is already running
        * A: If you are using Jupyter, pls use nest_asyncio.apply()
    * Q: Exception: UnauthorizedRequest: Cannot retrieve user status.
        * A: Renew your cookie file.
    * Q: Exception: conversationSignature
        * A: Clear all your bing cookie and renew your cookie file.
        * Like : #17
        * And: #22
    * Q: ValueError: Invalid header value b'_U=***\n'
        * A: Renew your image cookie.
    * Q: Image blocking or redirect error
        * A: Now we can't generate multi image on same time (Cause bing limit)
        * See #22
    * Q: UnauthorizedRequest: Token issued by https://sydney.bing.com/sydney is invalid
        * Bing block your connect, Try to use proxy or clear cookie.
