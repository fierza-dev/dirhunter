from imports.common_import import gather,ClientSession,ClientTimeout, ClientError, compile, Semaphore, aio_open, Fore, Style, Path

#! Konfigurasi global
RESULT_FOLDER = Path("result")
RESULT_FOLDER.mkdir(parents=True, exist_ok=True)

SEMAPHORE = Semaphore(100)
TIMEOUT = ClientTimeout(total=5)

HEADERS = {
    "User-Agent": "",
    "Cache-Control": "no-cache",
    "Accept-Encoding": "gzip, deflate",
    "Connection": "Keep-Alive",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
}

MAX_FILENAME_LENGTH = 128

async def write_result_to_file(scan_data, url, status):
    sanitize_pattern = compile(r'[^a-zA-Z0-9_-]')
    sanitized_url = sanitize_pattern.sub('_', scan_data.host)[:MAX_FILENAME_LENGTH]
    file_path = RESULT_FOLDER / f"{sanitized_url}-result.txt"
    
    async with aio_open(file_path, mode='a') as file:
        await file.write(f"[{status}] {url}\n")

async def process_response(status, url, scan_data):
    if status in (500, 429, 404, 301):
        print(f"[{Fore.LIGHTRED_EX}{status}{Style.RESET_ALL}] {url}")
    elif status in (200, 302, 307):
        print(f"[{Fore.GREEN}{status}{Style.RESET_ALL}] {url}")
        await write_result_to_file(scan_data, url, status)

async def check_path(session, scan_data, path):
    url = f'http://{scan_data.host.strip("/")}/{path.lstrip("/")}'
    headers = HEADERS.copy()
    headers["User-Agent"] = scan_data.current_useragent

    async with SEMAPHORE:
        try:
            async with session.get(url, headers=headers, allow_redirects=False, timeout=TIMEOUT) as response:
                await process_response(response.status, url, scan_data)
        except ClientTimeout:
            print(f"[{Fore.RED}Timeout{Style.RESET_ALL}] {url} - kemungkinan server lambat.")
        except ClientError as e:
            print(f"[{Fore.RED}ClientError: {e}{Style.RESET_ALL}] {url} - mungkin URL salah atau server error.")

async def main(scan_data, paths):
    async with ClientSession() as session:
        tasks = [check_path(session, scan_data, path) for path in paths]
        await gather(*tasks)
