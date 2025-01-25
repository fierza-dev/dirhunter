from imports.common_import import setdefaulttimeout,timeout,create_connection,Fore,Style

setdefaulttimeout(5)

def is_host_reachable(host):
    print(f'[{Fore.WHITE}*{Style.RESET_ALL}] Checking host...')
    try:
        with create_connection((host, 80)):
            print(f'[{Fore.GREEN}✓{Style.RESET_ALL}] Host {host} is reachable.')
            return True
    except (timeout, OSError):
        print(f'[{Fore.RED}X{Style.RESET_ALL}] Host {host} is not reachable.')
        return False