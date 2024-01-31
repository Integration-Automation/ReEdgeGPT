import base64
import json

import aiohttp

payload = {
    "imageInfo": {},
    "knowledgeRequest": {
        "invokedSkills": ["ImageById"],
        "subscriptionId": "Bing.Chat.Multimodal",
        "invokedSkillsRequestData": {"enableFaceBlur": True},
        "convoData": {
            "convoid": "",
            "convotone": "Balanced"
        }
    }
}


async def upload_image_url(image_url: str, conversation_id: str, proxy: str = None, face_blur: bool = True):
    async with aiohttp.ClientSession(
            headers={"Referer": "https://www.bing.com/search?q=Bing+AI&showconv=1&FORM=hpcodx"},
    ) as session:
        url = "https://www.bing.com/images/kblob"

        new_payload = payload
        new_payload.get("knowledgeRequest").update(
            {"invokedSkillsRequestData": {"enableFaceBlur": face_blur}})
        new_payload.get("imageInfo").update({"url": image_url})
        new_payload.get("knowledgeRequest").get("convoData").update({"convoid": conversation_id})
        data = aiohttp.FormData()
        data.add_field('knowledgeRequest', json.dumps(new_payload), content_type="application/json")
        async with session.post(url, data=data, proxy=proxy) as resp:
            return (await resp.json())["blobId"]


async def upload_image(filename: str = None, base64_image: str = None, proxy: str = None, face_blur: bool = True):
    async with aiohttp.ClientSession(
            headers={"Referer": "https://www.bing.com/search?q=Bing+AI&showconv=1&FORM=hpcodx"},
    ) as session:
        url = "https://www.bing.com/images/kblob"

        new_payload = payload.get("knowledgeRequest").update(
            {"invokedSkillsRequestData": {"enableFaceBlur": face_blur}})

        if filename is not None:
            with open(filename, 'rb') as f:
                file_data = f.read()
                image_base64 = base64.b64encode(file_data)
        elif base64_image is not None:
            image_base64 = base64_image
        else:
            raise Exception('no image provided')

        data = aiohttp.FormData()
        data.add_field('knowledgeRequest', json.dumps(new_payload), content_type="application/json")
        data.add_field('imageBase64', image_base64, content_type="application/octet-stream")

        async with session.post(url, data=data, proxy=proxy) as resp:
            return (await resp.json())["blobId"]
