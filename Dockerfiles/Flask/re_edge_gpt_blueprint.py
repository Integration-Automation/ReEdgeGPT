import json
from pathlib import Path

from flask import Blueprint, request, jsonify

from re_edge_gpt import Chatbot, ConversationStyle, ImageGenAsync
from re_edge_gpt.utils.utilities import guess_locale

re_edge_gpt_blueprint_instance = Blueprint("re_edge_gpt_blueprint", __name__, url_prefix="")

bot = {

}


async def setup_chatbot():
    cookies = json.loads(open("bing_cookies.json", encoding="utf-8").read())
    chatbot = await Chatbot.create(cookies=cookies)
    bot.update({"chatbot": chatbot})
    return chatbot


async def setup_imagebot():
    auth_cooker = open("bing_cookies.txt", "r+").read().strip()
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
      description: Data that Chat needed
      content:
        application/json:
          schema:
            properties:
              prompt:
                type: string
                example: Hello
                required: true
                description: Chat prompt
              wss_link:
                type: string
                default: wss://sydney.bing.com/sydney/ChatHub
                description: Connect to Bing endpoint wss link
                required: false
              conversation_style:
                type: string
                enum: ["creative_classic", "creative", "balanced", "precise"]
                default: balanced
                description: Chat conversation style
                required: false
              webpage_context:
                type: string
                default: null
                description: Chat webpage context
                required: false
              search_result:
                type: boolean
                default: false
                description: Chat search result?
                required: false
              locale:
                type: string
                description: User locale
                required: false
              simplify_response:
                type: boolean
                default: true
                description: Chat simplify response?
                required: false
              attachment:
                type: object
                description: Chat attachment
                required: false
                properties:
                  image_url:
                    type: string
                    default: null
                    description: Attached image url
                  base64_image:
                    type: string
                    default: null
                    description: Attached base64 string
              remove_options:
                type: array
                required: false
                description: Remove chat options
              add_options:
                type: array
                required: false
                description: Chat add options
              plugins:
                type: array
                required: false
                description: Chat plugins
              message_type:
                type: string
                required: false
                default: Chat
                description: Message type
    responses:
      200:
        description: Success chat
        content:
          application/json:
            schema:
              properties:
                author:
                  type: string
                  description: Chat Author
                image_create_text:
                  type: string
                  description: Use to create image
                max_messages:
                  type: integer
                  description: Maximum number of messages
                messageId:
                  type: string
                  description: Chat message id
                messages_left:
                  type: integer
                  description: Number of messages left
                source_keys:
                  type: array
                  description: Source title
                source_values:
                  type: array
                  description: Source link that GPT using
                suggestions:
                  type: array
                  description: GPT suggestions
                text:
                  type: string
                  description: Chat response
    """
    # Read json param
    prompt = request.json.get("prompt", None)
    wss_link = request.json.get("wss_link", "wss://sydney.bing.com/sydney/ChatHub")
    conversation_style = request.json.get("conversation_style", None)
    webpage_context = request.json.get("webpage_context", None)
    search_result = request.json.get("search_result", False)
    locale = request.json.get("locale", guess_locale())
    simplify_response = request.json.get("simplify_response", True)
    attachment = request.json.get("attachment", None)
    remove_options = request.json.get("remove_options", None)
    add_options = request.json.get("add_options", None)
    plugins = request.json.get("plugins", None)
    message_type = request.json.get("message_type", "Chat")
    conversation_style = {
        "creative_classic": ConversationStyle.creative_classic,
        "creative": ConversationStyle.creative,
        "balanced": ConversationStyle.balanced,
        "precise": ConversationStyle.precise,
    }.get(conversation_style, ConversationStyle.balanced)
    if bot.get("chatbot") is None:
        chatbot = await setup_chatbot()
    else:
        chatbot = bot.get("chatbot")
    try:
        response = await chatbot.ask(
            prompt=prompt,
            wss_link=wss_link,
            conversation_style=conversation_style,
            webpage_context=webpage_context,
            search_result=search_result,
            locale=locale,
            simplify_response=simplify_response,
            attachment=attachment,
            remove_options=remove_options,
            add_options=add_options,
            plugins=plugins,
            message_type=message_type
        )
        return jsonify(response)
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
                  description: Image generation prompt
                timeout:
                  type: integer
                  default: 200
                max_generate_time_sec:
                  type: integer
                  default: 60
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
    prompt = request.json.get("prompt")
    timeout = request.json.get("timeout", 200)
    max_generate_time_sec = request.json.get("max_generate_time_sec", 60)
    if bot.get("chatbot") is None:
        imagebot = await setup_imagebot()
    else:
        imagebot = bot.get("imagebot")
    image_list = await imagebot.get_images(
        prompt=prompt,
        timeout=timeout,
        max_generate_time_sec=max_generate_time_sec
    )
    return jsonify({"images": image_list})
