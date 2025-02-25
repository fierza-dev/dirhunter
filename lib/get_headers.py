from imports.common_import import randint

GENERAL_HEADERS = {
    "Cache-Control": "no-cache",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
}

BYPASS_HEADERS = {
    "Cache-Control": "no-cache",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "X-Forwarded-For": f"{randint(1, 255)}.{randint(1, 255)}.{randint(1, 255)}.{randint(1, 255)}",
    "X-Client-IP": f"{randint(1, 255)}.{randint(1, 255)}.{randint(1, 255)}.{randint(1, 255)}",
    "X-Remote-IP": f"{randint(1, 255)}.{randint(1, 255)}.{randint(1, 255)}.{randint(1, 255)}",
    "X-Remote-Addr": f"{randint(1, 255)}.{randint(1, 255)}.{randint(1, 255)}.{randint(1, 255)}",
    "X-Original-URL": "/admin",
    "X-Rewrite-URL": "/admin",
    "Referer": "https://www.google.com/",
    "Origin": "https://www.google.com/",
    "TE": "trailers",
    "Content-Length": "0",
    "X-HTTP-Method": "PUT",
    "X-HTTP-Method-Override": "PUT",
    "X-Method-Override": "PUT",
    "Upgrade-Insecure-Requests": "1",
    "Expect": "100-continue",  
}

async def get_headers(useragent, use_bypass):
    headers = GENERAL_HEADERS.copy()
    if use_bypass:
        headers.update(BYPASS_HEADERS)
    headers["User-Agent"] = useragent
    return headers
