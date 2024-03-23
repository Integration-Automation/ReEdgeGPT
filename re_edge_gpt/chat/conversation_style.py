from enum import Enum

try:
    from typing import Literal, Union
except ImportError:
    from typing_extensions import Literal
from typing import Optional


class ConversationStyle(Enum):
    creative = [
        "nlu_direct_response_filter",
        "deepleo",
        "disable_emoji_spoken_text",
        "responsible_ai_policy_235",
        "enablemm",
        "dv3sugg",
        "autosave",
        "iyxapbing",
        "iycapbing",
        "h3imaginative",
        "clgalileo",
        "gencontentv3",
        "uquopt",
        "sunoupsell",
        "gndlogcf",
        "flxvsearch",
        "noknowimg",
        "eredirecturl"
    ]
    creative_classic = [
        "nlu_direct_response_filter",
        "deepleo",
        "disable_emoji_spoken_text",
        "responsible_ai_policy_235",
        "enablemm",
        "dv3sugg",
        "autosave",
        "iyxapbing",
        "iycapbing",
        "h3imaginative",
        "clgalileo",
        "gencontentv3",
        "uquopt",
        "sunoupsell",
        "gndlogcf",
        "flxvsearch",
        "noknowimg",
        "eredirecturl"
    ]
    balanced = [
        "nlu_direct_response_filter",
        "deepleo",
        "disable_emoji_spoken_text",
        "responsible_ai_policy_235",
        "enablemm",
        "dv3sugg",
        "autosave",
        "iyxapbing",
        "iycapbing",
        "enable_user_consent",
        "fluxmemcst",
        "galileo",
        "saharagenconv5",
        "dc1mncp",
        "uquopt",
        "sunoupsell",
        "crkt2t",
        "immslots",
        "cpproname",
        "vidtoppb",
        "gptv1desc2",
        "eredirecturl"
    ]
    precise = [
        "nlu_direct_response_filter",
        "deepleo",
        "disable_emoji_spoken_text",
        "responsible_ai_policy_235",
        "enablemm",
        "dv3sugg",
        "autosave",
        "iyxapbing",
        "iycapbing",
        "enable_user_consent",
        "fluxmemcst",
        "h3precise",
        "clgalileo",
        "uquopt",
        "sunoupsell",
        "crkt2t",
        "flxvsearchans",
        "noknowimg",
        "eredirecturl"
    ]


CONVERSATION_STYLE_TYPE = Optional[
    Union[ConversationStyle, Literal["creative", "balanced", "precise"]]
]
