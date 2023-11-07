import json
from pathlib import Path

from flask import Blueprint, request

from re_edge_gpt import Chatbot, ConversationStyle

re_edge_gpt_blueprint_instance = Blueprint("re_edge_gpt_blueprint", __name__, url_prefix="/ReEdgeGPT")


@re_edge_gpt_blueprint_instance.route("/chat", methods=["POST"])
async def chat():
    prompt = request.get_json()["prompt"]
    bot = None
    try:
        cookies = json.loads(open(str(Path(str(Path.cwd()) + "/bing_cookies.json")), encoding="utf-8").read())
        bot = await Chatbot.create(cookies=cookies)
        response = await bot.ask(
            prompt=prompt,
            conversation_style=ConversationStyle.balanced,
            simplify_response=True
        )
        return json.dumps(response, indent=2, ensure_ascii=False)
    except Exception as error:
        raise error
    finally:
        if bot is not None:
            await bot.close()
