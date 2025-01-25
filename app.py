#!/usr/bin/python3
from lib.scanner import Scanner
from lib.scandata import ScanData
from lib.args import parse_arguments
from lib.banner import display_banner
from lib.host import is_host_reachable
from lib.load_wordlist import load_wordlist
from lib.load_useragents import load_useragents
from imports.common_import import exit,gather,run

async def main():
    display_banner()

    args = parse_arguments()

    scan_data = ScanData(host=args.url, wordlist_path=args.wordlist, useragent_file=args.useragent)
    
    if not is_host_reachable(scan_data.host):
        print(f'[!] Host {scan_data.host} is not reachable. Exiting.')
        exit(1)

    await gather(
        load_wordlist(scan_data),
        load_useragents(scan_data)
    )

    scanner = Scanner(scan_data)
    await scanner.run_scan()

if __name__ == '__main__':
    try:
        run(main())
    except KeyboardInterrupt:
        print('\n[!] Scan interrupted. Goodbye!')
        exit(1)
