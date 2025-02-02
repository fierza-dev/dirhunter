from imports.common_import import aio_open,Console

async def load_useragents(scan_data):
    try:
        async with aio_open(scan_data.useragent_file, mode='r') as file:
            async for line in file:
                scan_data.useragents.append(line.strip())
        Console.print(f'[+] User-Agent list loaded: {sum(1 for _ in scan_data.useragents)} user agents', style="bold")

    except (OSError, FileNotFoundError):
        Console.print(f'[ Warning ] User-Agent file not found: {scan_data.useragent_file}. Using default User-Agent.', Style="yellow")
        scan_data.useragents = ["Mozilla/5.0 (Windows NT 6.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36"]
