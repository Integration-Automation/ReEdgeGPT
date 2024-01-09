import socket
import uuid

take_ip_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
take_ip_socket.connect(("8.8.8.8", 80))
FORWARDED_IP: str = take_ip_socket.getsockname()[0]
take_ip_socket.close()

DELIMITER = "\x1e"

HEADERS = {
    "accept": "application/json",
    "accept-language": "en,zh-TW;q=0.9,zh;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "accept-encoding": "gzip, deflate, br, zsdch",
    "content-type": "application/json",
    "sec-ch-ua": '"Microsoft Edge";v="120", '
                 '"Chromium";v="120", '
                 '"Not?A_Brand";v="8"',
    "sec-ch-ua-arch": '"x86"',
    "sec-ch-ua-bitness": '"64"',
    "sec-ch-ua-full-version": '"120"',
    "sec-ch-ua-full-version-list": '"Microsoft Edge";v="120", '
                                   '"Chromium";v="120", '
                                   '"Not?A_Brand";v="8"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-model": "",
    "sec-ch-ua-platform": '"Windows"',
    "sec-ch-ua-platform-version": '"15.0.0"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "sec-ms-gec-version": "1-120",
    "x-ms-client-request-id": str(uuid.uuid4()),
    "Referer": "https://copilot.microsoft.com/",
    "Referrer-Policy": "origin-when-cross-origin",
    "x-forwarded-for": FORWARDED_IP,
}

HEADERS_INIT_CONVER = {
    "accept": "application/json",
    "accept-language": "en,zh-TW;q=0.9,zh;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "cache-control": "max-age=0",
    "sec-ch-ua": '"Microsoft Edge";v="120", '
                 '"Chromium";v="120", '
                 '"Not?A_Brand";v="8"',
    "sec-ch-ua-arch": '"x86"',
    "sec-ch-ua-bitness": '"64"',
    "sec-ch-ua-full-version": '"120"',
    "sec-ch-ua-full-version-list": '"Microsoft Edge";v="120", "'
                                   'Chromium";v="120",'
                                   ' "Not?A_Brand";v="8"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-model": '""',
    "sec-ch-ua-platform": '"Windows"',
    "sec-ch-ua-platform-version": '"15.0.0"',
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/120.0.0.0 "
                  "Safari/537.36 "
                  "Edg/120.0.2210.91",
    "x-edge-shopping-flag": "0",
    "x-forwarded-for": FORWARDED_IP,
}

BUNDLE_VERSION = "1.1381.12"
