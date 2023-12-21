Q&A
----

Details

.. code-block:: markdown

    > * Q: Exception: Throttled: Request is throttled.
    >   * A: Bing's chat rate limit.
    >   * ![rate_limit.png](images/rate_limit.png)
    > * Q: RuntimeError: This event loop is already running
    >   * A: If you are using Jupyter, pls use nest_asyncio.apply()
    >   * Like: https://github.com/Integration-Automation/ReEdgeGPT/issues/30
    > * Q: json.dumps return non utf-8 char
    >   * A: json.dumps(response, ensure_ascii=False)
    >   * Like: https://github.com/Integration-Automation/ReEdgeGPT/issues/32
    > * Q: Exception: UnauthorizedRequest: Cannot retrieve user status.
    >   * A: Renew your cookie file.
    > * Q: Exception: conversationSignature
    >   * A: Clear all your bing cookie and renew your cookie file.
    >   * Like: https://github.com/Integration-Automation/ReEdgeGPT/issues/17
    >   * And: https://github.com/Integration-Automation/ReEdgeGPT/issues/22
    > * Q: ValueError: Invalid header value b'_U=***\n'
    > * A: Renew your image cookie.
    > * Q: Image blocking or redirect error
    >   * A: Now we can't generate multi image on same time (Cause bing limit)
    >   * See https://github.com/Integration-Automation/ReEdgeGPT/issues/22
    > * Q: UnauthorizedRequest: Token issued by https://sydney.bing.com/sydney is invalid
    >   * A: Bing block your connect, Try to use proxy or clear cookie.
