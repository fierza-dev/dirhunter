import asyncio
from lib.get_headers import get_headers
from lib.process_response import process_response
from imports.common_import import (
    Semaphore, choice, ClientSession
)

async def check_path(session: ClientSession, GetConfig, path):
    semaphore = Semaphore(GetConfig.threads)
    url = GetConfig.host + f'/{path.lstrip("/")}'
    headers = await get_headers(choice(GetConfig.useragents), GetConfig.httpSmug)
    proxy = choice(GetConfig.Getproxy) if GetConfig.Getproxy else GetConfig.proxy

    async with semaphore:
        async with asyncio.timeout(GetConfig.timeout):
            async with session.get(url, headers=headers, proxy=proxy or None, allow_redirects=False) as response:
                await process_response(response.headers,response.status, url, GetConfig)
