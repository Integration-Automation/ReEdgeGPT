import uuid
from datetime import datetime
from typing import Union

from re_edge_gpt.chat.conversation_style import CONVERSATION_STYLE_TYPE
from re_edge_gpt.chat.conversation_style import ConversationStyle
from re_edge_gpt.utils.utilities import get_location_hint_from_locale
from re_edge_gpt.utils.utilities import get_ran_hex
from re_edge_gpt.utils.utilities import guess_locale


class ChatHubRequest:
    def __init__(
            self,
            conversation_signature: str,
            client_id: str,
            conversation_id: str,
            invocation_id: int = 3,
    ) -> None:
        self.struct: dict = {}

        self.client_id: str = client_id
        self.conversation_id: str = conversation_id
        self.conversation_signature: str = conversation_signature
        self.invocation_id: int = invocation_id

    def update(
            self,
            prompt: str,
            conversation_style: CONVERSATION_STYLE_TYPE,
            webpage_context: Union[str, None] = None,
            search_result: bool = False,
            locale: str = guess_locale(),
            image_url: str = None,
            plugins: list = None,
            message_type: str = "Chat"
    ) -> None:
        if conversation_style:
            if not isinstance(conversation_style, ConversationStyle):
                conversation_style = getattr(ConversationStyle, conversation_style)
        message_id = str(uuid.uuid4())
        request_id = str(uuid.uuid4())
        # Get the current local time
        now_local = datetime.now()

        # Get the current UTC time
        now_utc = datetime.utcnow()

        # Calculate the time difference between local and UTC time
        timezone_offset = now_local - now_utc

        # Get the offset in hours and minutes
        offset_hours = int(timezone_offset.total_seconds() // 3600)
        offset_minutes = int((timezone_offset.total_seconds() % 3600) // 60)

        # Format the offset as a string
        offset_string = f"{offset_hours:+03d}:{offset_minutes:02d}"

        # Get current time
        timestamp = datetime.now().strftime("%Y-%m-%dT%H:%M:%S") + offset_string
        style = conversation_style.name.capitalize()  # Make first letter uppercase
        not_in_style = {"creative_classic": "CreativeClassic"}
        self.struct = {
            "arguments": [
                {
                    "optionsSets": conversation_style.value,
                    "allowedMessageTypes": [
                        "ActionRequest",
                        "Chat",
                        "ConfirmationCard",
                        "Context",
                        "InternalSearchQuery",
                        "InternalSearchResult",
                        "Disengaged",
                        "InternalLoaderMessage",
                        "Progress",
                        "RenderCardRequest",
                        "RenderContentRequest",
                        "AdsQuery",
                        "SemanticSerp",
                        "GenerateContentQuery",
                        "SearchQuery",
                        "GeneratedCode",
                        "InternalTasksMessage"
                    ],
                    "sliceIds": [
                        "disbotgrtcf",
                        "ntbkgold2",
                        "ntbkf1",
                        "qna10",
                        "thdnsrch",
                        "slangcf",
                        "vnextr100",
                        "vnext100",
                        "vnextvoice",
                        "rdlidncf",
                        "semserpnomlbg",
                        "semserpnoml",
                        "srchqryfix",
                        "cacntjndcae",
                        "edgenorrwrap",
                        "cmcpupsalltf",
                        "sunoupsell",
                        "313dynaplfs0",
                        "0312hrthrots0",
                        "0317immslotsc",
                        "228pyfiles0",
                        "kcclickthrucf",
                        "sportsatis0",
                        "0317dc1pro",
                        "defgrey",
                        "ssadsv4chtiidnoifbm",
                        "adsltmdsc",
                        "ssadsv2nocm"
                    ],
                    "plugins": plugins,
                    "isStartOfSession": self.invocation_id == 3,
                    "message": {
                        "locale": locale,
                        "market": locale,
                        "region": locale[-2:],  # en-US -> US
                        "locationHints": get_location_hint_from_locale(locale),
                        "timestamp": timestamp,
                        "author": "user",
                        "inputMethod": "Keyboard",
                        "text": prompt,
                        "messageType": message_type,
                        "messageId": message_id,
                        "requestId": request_id,
                        "imageUrl": image_url if image_url else None,
                        "originalImageUrl": image_url if image_url else None,
                    },
                    "tone": style if style not in not_in_style.keys()
                    else not_in_style.get(style),
                    "requestId": request_id,
                    "conversationSignature": self.conversation_signature,
                    "participant": {
                        "id": self.client_id,
                    },
                    "conversationId": self.conversation_id,
                },
            ],
            "invocationId": str(self.invocation_id),
            "target": "chat",
            "type": 4,
        }
        if search_result:
            have_search_result = [
                "InternalSearchQuery",
                "InternalSearchResult",
                "InternalLoaderMessage",
                "RenderCardRequest",
            ]
            self.struct["arguments"][0]["allowedMessageTypes"] += have_search_result
        if webpage_context:
            self.struct["arguments"][0]["previousMessages"] = [
                {
                    "author": "user",
                    "description": webpage_context,
                    "contextType": "WebPage",
                    "messageType": "Context",
                    "messageId": "discover-web--page-ping-mriduna-----",
                },
            ]
        self.invocation_id += 1

        # print(timestamp)
