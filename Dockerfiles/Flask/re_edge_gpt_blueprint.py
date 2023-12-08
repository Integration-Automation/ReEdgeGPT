import json
from pathlib import Path

from flask import Blueprint, request, jsonify

from re_edge_gpt import Chatbot, ConversationStyle, ImageGenAsync

re_edge_gpt_blueprint_instance = Blueprint("re_edge_gpt_blueprint", __name__, url_prefix="/ReEdgeGPT")

bot = {

}


async def setup_chatbot():
    cookies = json.loads(open(str(Path(str(Path.cwd()) + "bing_cookies.json")), encoding="utf-8").read())
    chatbot = await Chatbot.create(cookies=cookies)
    bot.update({"chatbot": chatbot})
    return chatbot


async def setup_imagebot():
    auth_cooker = open("bing_cookies.txt", "r+").read()
    imagebot = ImageGenAsync(auth_cookie=auth_cooker)
    bot.update({"imagebot": imagebot})
    return imagebot


@re_edge_gpt_blueprint_instance.route("/chat", methods=["POST"])
async def chat():
    """
    Send a prompt and chat mode to chat with Bing
    ---
   post:
    description: Chat with bing
    tags:
      - GPT
    requestBody:
      description: Data that chat needed
      content:
        application/json:
          schema:
            properties:
              prompt:
                type: string
                example: How to boil the eggs
              conversation_style:
                type: string
                enum: ["creative", "balanced", "precise"]
                default: balanced
              simplify_response:
                type: boolean
              attachment:
                type: object
                properties:
                  image_url:
                    type: string
                    default: null
                  filename:
                    type: string
                    default: null
                  base64_image:
                    type: string
                    default: null
    responses:
      200:
        description: Success chat
        content:
          application/json:
            schema:
              properties:
                text:
                  type: string
                author:
                  type: string
                sources:
                  type: string
                sources_link:
                  type: string
                suggestions:
                  type: array
                  example: [
                    "How do I know if the eggs are fresh?",
                    "What is a soft-boiled egg?",
                    "Can you give me some recipes with boiled eggs?"
                    ]
                messages_left:
                  type: integer
                  example: 29
                max_messages:
                  type: integer
                  example: 30
    """
    prompt = request.get_json()["prompt"]
    conversation_style = request.get_json()["conversation_style"]
    conversation_style = {
        "creative": ConversationStyle.creative,
        "balanced": ConversationStyle.balanced,
        "precise": ConversationStyle.precise,
    }.get(conversation_style, ConversationStyle.balanced)
    simplify_response = request.get_json()["simplify_response"]
    attachment = request.get_json()["attachment"]
    if bot.get("chatbot") is None:
        chatbot = await setup_chatbot()
    else:
        chatbot = bot.get("chatbot")
    try:
        response = await chatbot.ask(
            prompt=prompt,
            conversation_style=conversation_style,
            simplify_response=simplify_response,
            attachment=attachment
        )
        return jsonify(response)
    except Exception as error:
        raise error
    finally:
        if chatbot is not None:
            await chatbot.close()


@re_edge_gpt_blueprint_instance.route("/image", methods=["POST"])
async def image():
    """
    Send a prompt to generate image
    ---
    post:
      description: Generate image using DALL3-E
      tags:
        - GPT
      requestBody:
        description: prompt
        content:
          application/json:
            schema:
              properties:
                prompt:
                  type: string
      responses:
        200:
          description: Success generate image
          content:
            application/json:
              schema:
                properties:
                  images:
                    type: array
                    example: [
                      "image_url1",
                      "image_url2",
                      "image_url3"
                      ]
    """
    prompt = request.get_json()["prompt"]
    if bot.get("chatbot") is None:
        imagebot = await setup_imagebot()
    else:
        imagebot = bot.get("imagebot")
    image_list = await imagebot.get_images(prompt)
    return jsonify({"images": image_list})
