from imports.common_import import randint

GENERAL_HEADERS = {
    "Cache-Control": "no-cache",
    "Pragma": "no-cache",  
    "Accept-Encoding": "gzip, deflate, br",  
    "Connection": "keep-alive",  
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8", 
    "Accept-Language": "en-US,en;q=0.9",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-User": "?1",
    "Sec-Fetch-Dest": "document",
    "Upgrade-Insecure-Requests": "1",
    "DNT": "1",
}

BYPASS_HEADERS = {
    "Cache-Control": "no-cache",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Upgrade-Insecure-Requests": "1",
    "Referer": "https://www.google.com/",
    "Origin": "https://www.google.com/",
    "TE": "trailers",
    "Expect": "100-continue",
    "X-Forwarded-For": f"{randint(1, 255)}.{randint(1, 255)}.{randint(1, 255)}.{randint(1, 255)}",
    "X-Client-IP": f"{randint(1, 255)}.{randint(1, 255)}.{randint(1, 255)}.{randint(1, 255)}",
    "X-Real-IP": f"{randint(1, 255)}.{randint(1, 255)}.{randint(1, 255)}.{randint(1, 255)}",  
    "X-Originating-IP": f"{randint(1, 255)}.{randint(1, 255)}.{randint(1, 255)}.{randint(1, 255)}",  
    "X-Original-URL": "/admin",
    "X-Rewrite-URL": "/admin",
    "X-Forwarded-Path": "/admin", 
    "X-HTTP-Method": "POST", 
    "X-HTTP-Method-Override": "POST",
    "X-Method-Override": "POST",  
    "Content-Length": "0",
    "Transfer-Encoding": "chunked", 
    "DNT": "1", 
    "Pragma": "no-cache",
}

async def get_headers(useragent, use_bypass):
    headers = GENERAL_HEADERS.copy()
    if use_bypass:
        headers.update(BYPASS_HEADERS)
    headers["User-Agent"] = useragent
    return headers
