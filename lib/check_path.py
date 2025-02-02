from imports.common_import import (
    choice, TimeoutError, ClientError, Console, Semaphore,timeout
)

DEFAULT_HEADERS = {
    "Cache-Control": "no-cache",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
}

async def get_headers(useragent):
    return {**DEFAULT_HEADERS, "User-Agent": useragent}

async def process_response(status, url, scan_data):
        if status == 200:
            Console.print(f"[[bold sea_green1]{status}[/bold sea_green1]] [bold white]{url}[/bold white]")
            scan_data.results.append(url)
async def check_path(session, scan_data, path):
    semaphore = Semaphore(scan_data.threads)
    url = f'{scan_data.host.strip("/")}/{path.lstrip("/")}'
    headers = await get_headers(choice(scan_data.useragents))

    try:
        async with semaphore:
            async with timeout(scan_data.timeout):
                async with session.get(url, headers=headers, allow_redirects=False) as response:
                    await process_response(response.status, url, scan_data)
    except (ClientError, TimeoutError):
        pass
