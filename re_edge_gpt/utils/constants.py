import random
import uuid


FORWARDED_IP = f"1.0.0.{random.randint(0, 255)}"

DELIMITER = "\x1e"

HEADERS = {
    "accept": "application/json",
    "accept-language": "en;q=0.9,en-US;q=0.8",
    "accept-encoding": "gzip, deflate, br, zsdch",
    "content-type": "application/json",
    "sec-ch-ua": '"Not A(Brand";v="99", '
                 '"Microsoft Edge";v="121", '
                 '"Chromium";v="121"',
    "sec-ch-ua-arch": '"x86"',
    "sec-ch-ua-bitness": '"64"',
    "sec-ch-ua-full-version": '"121.0.2277.83"',
    "sec-ch-ua-full-version-list": '"Not A(Brand";v="99.0.0.0", '
                                   '"Microsoft Edge";v="121.0.2277.83", '
                                   '"Chromium";v="121.0.6167.85"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-model": "",
    "sec-ch-ua-platform": '"Windows"',
    "sec-ch-ua-platform-version": '"15.0.0"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "sec-ms-gec-version": "1-120.0.2210.133",
    "x-ms-client-request-id": str(uuid.uuid4()),
    "x-ms-useragent": "azsdk-js-api-client-factory/1.0.0-beta.1 core-rest-pipeline/1.12.3 OS/Windows",
    "Referer": "https://www.bing.com/search?form=NTPCHB&q=Bing+AI&showconv=1",
    "Referrer-Policy": "origin-when-cross-origin",
    "x-forwarded-for": FORWARDED_IP,
}

HEADERS_INIT_CONVER = {
    "accept": "application/json",
    "accept-language": "en;q=0.9,en-US;q=0.8",
    "cache-control": "max-age=0",
    "sec-ch-ua": '"Not A(Brand";v="99", '
                 '"Microsoft Edge";v="121", '
                 '"Chromium";v="121"',
    "sec-ch-ua-arch": '"x86"',
    "sec-ch-ua-bitness": '"64"',
    "sec-ch-ua-full-version": '"121.0.2277.83"',
    "sec-ch-ua-full-version-list": '"Not A(Brand";v="99.0.0.0", '
                                   '"Microsoft Edge";v="121.0.2277.83", '
                                   '"Chromium";v="121.0.6167.85"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-model": '""',
    "sec-ch-ua-platform": '"Windows"',
    "sec-ch-ua-platform-version": '"15.0.0"',
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/120.0.0.0 "
                  "Safari/537.36 "
                  "Edg/120.0.0.0",
    "x-edge-shopping-flag": "1",
    "X-Ms-Useragent": "azsdk-js-api-client-factory/1.0.0-beta.1 core-rest-pipeline/1.12.3 OS/Windows",
    "x-forwarded-for": FORWARDED_IP,
}

IMAGE_HEADER = {
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate, br",
    "Content-Type": "multipart/form-data",
    "Referer": "https://www.bing.com/search?q=Bing+AI&showconv=1&FORM=hpcodx",
    "sec-ch-ua": '"Not A(Brand";v="99", '
                 '"Microsoft Edge";v="121", '
                 '"Chromium";v="121"',
    "sec-ch-ua-arch": '"x86"',
    "sec-ch-ua-bitness": '"64"',
    "sec-ch-ua-full-version": '"121.0.2277.83"',
    "sec-ch-ua-full-version-list": '"Not A(Brand";v="99.0.0.0", '
                                   '"Microsoft Edge";v="121.0.2277.83", '
                                   '"Chromium";v="121.0.6167.85"',
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": "Windows",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/120.0.0.0 "
                  "Safari/537.36 "
                  "Edg/120.0.0.0",
}

BUNDLE_VERSION = "1.1498.1"

SYDNEY_INIT_HEADER = HEADERS_INIT_CONVER.update(
    {
        "Referer": "https://copilot.microsoft.com/",
        "X-Edge-Shopping-Flag": "0",
    }
)

SYDNEY_HEADER = HEADERS.update(
    {
        "Cache-Control": "no-cache",
        "Connection": "Upgrade",
        "Origin": "https://copilot.microsoft.com",
        "Pragma": "no-cache",
    }
)
