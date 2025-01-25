from imports.common_import import exit,aio_open,Fore,Style

async def load_wordlist(scan_data):
    try:
        async with aio_open(scan_data.wordlist_path, mode='r') as file:
            scan_data.paths = (await file.read()).strip().splitlines()
        print(f'[+] Wordlist loaded: {scan_data.wordlist_path} ({len(scan_data.paths)} paths)')
    except FileNotFoundError:
        print(f'[{Fore.RED}Error{Style.RESET_ALL}] Wordlist not found: {scan_data.wordlist_path}')
        exit(1)