# ReEdgeGPT

_The reverse engineering the chat feature of the new version of Bing_

[![Documentation Status](https://readthedocs.org/projects/reedgegpt/badge/?version=latest)](https://reedgegpt.readthedocs.io/en/latest/?badge=latest)

[ReEdgeGPT Doc Click Here!](https://reedgegpt.readthedocs.io/en/latest/)

If you have any problem watch bottom Q&A first.

## Another README

<details open>

[繁體中文](/Readmes/zh_tw.md)

</details>

<summary>

# Setup

</summary>

<details open>

## Install package

```bash
python3 -m pip install re_edge_gpt --upgrade
```
## Requirements

- python 3.9+
- A Microsoft Account with access to <https://bing.com/chat> (Optional, depending on your region)
- Required in a supported country or region with New Bing (Chinese mainland VPN required)

## Authentication

!!! POSSIBLY NOT REQUIRED ANYMORE !!!

**In some regions**, Microsoft has made the chat feature **available** to everyone, so you might be able to **skip this step**. You can check this with a browser (with user-agent set to reflect Edge), by **trying to start a chat without logging in**.

It was also found that it might **depend on your IP address**. For example, if you try to access the chat features from an IP that is known to **belong to a datacenter range** (vServers, root servers, VPN, common proxies, ...), **you might be required to log in** while being able to access the features just fine from your home IP address.

If you receive the following error, you can try **providing a cookie** and see if it works then:

`Exception: Authentication failed. You have not been accepted into the beta.`

### Collect cookies

- a) (Easy) Install the latest version of Microsoft Edge
- b) (Advanced) Alternatively, you can use any browser and set the user-agent to look like you're using Edge (e.g., `Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.51`). You can do this easily with an extension like "User-Agent Switcher and Manager" for [Chrome](https://chrome.google.com/webstore/detail/user-agent-switcher-and-m/bhchdcejhohfmigjafbampogmaanbfkg) and [Firefox](https://addons.mozilla.org/en-US/firefox/addon/user-agent-string-switcher/).

1. Get a browser that looks like Microsoft Edge.
2. Open [bing.com/chat](https://bing.com/chat)
3. If you see a chat feature, you are good to continue...
4. Install the cookie editor extension for [Chrome](https://chrome.google.com/webstore/detail/cookie-editor/hlkenndednhfkekhgcdicdfddnkalmdm) or [Firefox](https://addons.mozilla.org/en-US/firefox/addon/cookie-editor/)
5. Go to [bing.com/chat]([https://bing.com](https://bing.com/chat))
6. Open the extension
7. Click "Export" on the bottom right, then "Export as JSON" (This saves your cookies to clipboard)
8. Paste your cookies into a file `bing_cookies.json`.
   - NOTE: The **cookies file name MUST follow the regex pattern `bing_cookies.json`**, so that they could be recognized by internal cookie processing mechanisms

### Use cookies in code:

```python
import json
from re_edge_gpt import Chatbot


async def create_bot():
    cookies = json.loads(open("./path/to/bing_cookies.json", encoding="utf-8").read())
    bot = await Chatbot.create(cookies=cookies)
    return bot

```

</details>

<summary>

# How to use Chatbot

</summary>

<details open>

## Run from Command Line

```
 $ python3 -m re_edge_gpt -h

        ReEdgeGPT - A demo of reverse engineering the Bing GPT chatbot

        !help for help

        Type !exit to exit

usage: __main__.py [-h] [--enter-once] [--search-result] [--no-stream] [--rich] [--proxy PROXY] [--wss-link WSS_LINK]
                  [--style {creative,balanced,precise}] [--prompt PROMPT] [--cookie-file COOKIE_FILE]
                  [--history-file HISTORY_FILE] [--locale LOCALE]

options:
  -h, --help            show this help message and exit
  --enter-once
  --search-result
  --no-stream
  --rich
  --proxy PROXY         Proxy URL (e.g. socks5://127.0.0.1:1080)
  --wss-link WSS_LINK   WSS URL(e.g. wss://sydney.bing.com/sydney/ChatHub)
  --style {creative,balanced,precise}
  --prompt PROMPT       prompt to start with
  --cookie-file COOKIE_FILE
                        path to cookie file
  --history-file HISTORY_FILE
                        path to history file
  --locale LOCALE       your locale (e.g. en-US, zh-CN, en-IE, en-GB)
```

(China/US/UK/Norway has enhanced support for locale)

## Run in Python

### 1. The `Chatbot` class and `asyncio` for more granular control

Use Async for the best experience, for example:

```python
import asyncio
import json
from pathlib import Path

from re_edge_gpt import Chatbot
from re_edge_gpt import ConversationStyle


# If you are using jupyter pls install this package
# from nest_asyncio import apply


async def test_ask() -> None:
    bot = None
    try:
        cookies = json.loads(open(
            str(Path(str(Path.cwd()) + "/bing_cookies.json")), encoding="utf-8").read())
        bot = await Chatbot.create(cookies=cookies)
        response = await bot.ask(
            prompt="How to boil the egg",
            conversation_style=ConversationStyle.balanced,
            simplify_response=True
        )
        # If you are using non ascii char you need set ensure_ascii=False
        print(json.dumps(response, indent=2, ensure_ascii=False))
        # Raw response
        # print(response)
        assert response
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


```

</details>

<summary>

# How to generate image

</summary>

<details open>

## Getting authentication
> ### Chromium based browsers (Edge, Opera, Vivaldi, Brave)
> * Go to https://bing.com/
> * F12 to open console
> * In the JavaScript console, type **cookieStore.get("_U").then(result => console.log(result.value))** and press enter
> * Copy the output. This is used in --U or auth_cookie.

> ### Firefox
> * Go to https://bing.com/.
> * F12 to open developer tools
> * navigate to the storage tab
> * expand the cookies tab
> * click on the https://bing.com cookie
> * copy the value from the _U

```python
import os
import shutil
from pathlib import Path

from re_edge_gpt import ImageGen, ImageGenAsync

# create a temporary output directory for testing purposes
test_output_dir = "test_output"
# download a test image
test_image_url = "https://picsum.photos/200"
auth_cooker = open("bing_cookies.txt", "r+").read()
sync_gen = ImageGen(auth_cookie=auth_cooker)
async_gen = ImageGenAsync(auth_cookie=auth_cooker)


def test_save_images_sync():
    sync_gen.save_images([test_image_url], test_output_dir)
    sync_gen.save_images([test_image_url], test_output_dir, file_name="test_image")
    # check if the image was downloaded and saved correctly
    assert os.path.exists(os.path.join(test_output_dir, "test_image_0.jpeg"))
    assert os.path.exists(os.path.join(test_output_dir, "0.jpeg"))


# Generate image list sync
def test_generate_image_sync():
    image_list = sync_gen.get_images("tree")
    print(image_list)

if __name__ == "__main__":
    # Make dir to save image
    Path("test_output").mkdir(exist_ok=True)
    # Save image
    test_save_images_sync()
    # Generate image sync
    test_generate_image_sync()
    # Remove dir
    shutil.rmtree(test_output_dir)
```

</details>

# Q&A

<details open>

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

</details>
