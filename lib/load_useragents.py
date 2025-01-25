from imports.common_import import Fore,Style

async def load_useragents(scan_data):
    try:
        scan_data.useragents = scan_data.useragent_file
        scan_data.set_random_useragent()
        print(f'[+] User-Agent list loaded: {len(scan_data.useragents)} user agents')
    except FileNotFoundError:
        print(f'[{Fore.YELLOW}Warning{Style.RESET_ALL}] User-Agent file not found: {scan_data.useragent_file}. Using default User-Agent.')
        scan_data.set_random_useragent()