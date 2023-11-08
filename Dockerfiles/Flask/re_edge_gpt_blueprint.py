import json
from pathlib import Path

from flask import Blueprint, request, jsonify

from re_edge_gpt import Chatbot, ConversationStyle

re_edge_gpt_blueprint_instance = Blueprint("re_edge_gpt_blueprint", __name__, url_prefix="/ReEdgeGPT")


@re_edge_gpt_blueprint_instance.route("/chat", methods=["POST"])
async def chat():
    prompt = request.get_json()["prompt"]
    conversation_style = request.get_json()["conversation_style"]
    conversation_style = {
        "creative": ConversationStyle.creative,
        "balanced": ConversationStyle.balanced,
        "precise": ConversationStyle.precise,
    }.get(conversation_style, ConversationStyle.balanced)
    simplify_response = request.get_json()["simplify_response"]
    bot = None
    try:
        cookies = json.loads(open(str(Path(str(Path.cwd()) + "/bing_cookies.json")), encoding="utf-8").read())
        bot = await Chatbot.create(cookies=cookies)
        response = await bot.ask(
            prompt=prompt,
            conversation_style=conversation_style,
            simplify_response=simplify_response
        )
        return jsonify(response)
    except Exception as error:
        raise error
    finally:
        if bot is not None:
            await bot.close()
