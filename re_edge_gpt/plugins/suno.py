import asyncio
import json
import re
import secrets

import aiohttp

from re_edge_gpt.chat.constants import SUNO_HEADER


async def generate_suno_music(cookies: list[dict], iframe_id: str, request_id: str):
    new_cookies = {}
    for cookie in cookies:
        new_cookies[cookie["name"]] = cookie["value"]
    async with aiohttp.ClientSession(
            headers=SUNO_HEADER, cookies=new_cookies
    ) as session:
        generate_url = f"https://www.bing.com/videos/music?vdpp=suno&kseed=7500&SFX=2&q=&" \
                       f"iframeid={iframe_id}&requestid={request_id}"
        response = await session.get(generate_url)
        if response.status != 200:
            raise Exception("Generate suno music failed")
        skey = re.findall('skey=(.*?)&amp;', await response.text())
        if skey:
            skey = skey[0]
        else:
            raise Exception("Generate suno music failed cause by: skey")
        real_generate_url = f"https://www.bing.com/videos/api/custom/music?skey={skey}" \
                            f"&safesearch=Moderate&vdpp=suno&requestid={request_id}" \
                            f"&ig={secrets.token_hex(32).upper()}&iid=vsn&sfx=1"
        async with aiohttp.ClientSession(
                headers={"Referer": real_generate_url}, cookies=new_cookies
        ) as real_session:
            for i in range(0, 20, 1):
                await asyncio.sleep(3)
                response = await real_session.get(real_generate_url)
                suno_response: dict = json.loads(await response.text())
                suno_response = {"RawResponse": json.loads(suno_response.get("RawResponse"))}
                if suno_response.get("RawResponse").get("status") == "running":
                    continue
                if suno_response.get("RawResponse").get("status") != "complete":
                    raise Exception("Generate suno music failed cause by: status error")
                suno_response = suno_response.get("RawResponse")
                return {
                    "Image": f"https://th.bing.com/th?&id={suno_response.get('imageKey')}",
                    "Audio": f"https://th.bing.com/th?&id={suno_response.get('audioKey')}",
                    "Video": f"https://th.bing.com/th?&id={suno_response.get('videoKey')}",
                    "Duration": f"https://th.bing.com/th?&id={suno_response.get('duration')}",
                    "Style": f"https://th.bing.com/th?&id={suno_response.get('musicalStyle')}",
                    "Title": f"https://th.bing.com/th?&id={suno_response.get('gptPrompt')}",
                    "Lyrics": f"https://th.bing.com/th?&id={suno_response.get('lyrics')}",
                }
            raise Exception("Generate suno music failed")
