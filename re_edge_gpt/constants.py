import socket
import uuid

take_ip_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
take_ip_socket.connect(("8.8.8.8", 80))
FORWARDED_IP: str = take_ip_socket.getsockname()[0]
take_ip_socket.close()

DELIMITER = "\x1e"

HEADERS = {
    "accept": "application/json",
    "accept-language": "en-US;q=0.9",
    "accept-encoding": "gzip, deflate, br, zsdch",
    "content-type": "application/json",
    "sec-ch-ua": '"Chromium";v="116", "Not)A;Brand";v="24", "Microsoft Edge";v="116"',
    "sec-ch-ua-arch": '"x86"',
    "sec-ch-ua-bitness": '"64"',
    "sec-ch-ua-full-version": '"116.0.1938.62"',
    "sec-ch-ua-full-version-list": '"Chromium";v="116.0.5845.111", '
                                   '"Not)A;Brand";v="24.0.0.0", '
                                   '"Microsoft Edge";v="116.0.1938.62"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-model": "",
    "sec-ch-ua-platform": '"Windows"',
    "sec-ch-ua-platform-version": '"15.0.0"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "sec-ms-gec-version": "1-116.0.1938.62",
    "x-ms-client-request-id": str(uuid.uuid4()),
    "x-ms-useragent": "azsdk-js-api-client-factory/1.0.0-beta.1 core-rest-pipeline/1.12.0 OS/Windows",
    "Referer": "https://www.bing.com/search?",
    "Referrer-Policy": "origin-when-cross-origin",
    "x-forwarded-for": FORWARDED_IP,
}

HEADERS_INIT_CONVER = {
    "authority": "www.bing.com",
    "accept": "application/json",
    "accept-language": "en-US;q=0.9",
    "cache-control": "max-age=0",
    "sec-ch-ua": '"Chromium";v="116", "Not)A;Brand";v="24", "Microsoft Edge";v="116"',
    "sec-ch-ua-arch": '"x86"',
    "sec-ch-ua-bitness": '"64"',
    "sec-ch-ua-full-version": '"116.0.1938.62"',
    "sec-ch-ua-full-version-list": '"Chromium";v="116.0.5845.111", '
                                   '"Not)A;Brand";v="24.0.0.0", '
                                   '"Microsoft Edge";v="116.0.1938.62"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-model": '""',
    "sec-ch-ua-platform": '"Windows"',
    "sec-ch-ua-platform-version": '"15.0.0"',
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/116.0.0.0 Safari/537.36 "
                  "Edg/116.0.1938.62",
    "x-edge-shopping-flag": "1",
    "x-forwarded-for": FORWARDED_IP,
}
