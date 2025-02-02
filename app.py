#!/usr/bin/python3
_A='bold'
from imports.app_import import*
from imports.common_import import exit,gather,run,Console
async def main():
	display_banner();args=parse_arguments()
	if args.version:Console.print('[-] Version : 2.2 (Cheetah Booster)',style=_A);exit(1)
	scan_data=ScanData(host=args.url,wordlist_path=args.wordlist,useragent_file=args.user_agent,threads=args.threads,timeout=args.time_out)
	if not await is_host_reachable(scan_data.host):Console.print(f"[bold red1][!][/bold red1] Host {scan_data.host} is not reachable. Exiting.",style=_A);exit(1)
	await gather(load_wordlist(scan_data),load_useragents(scan_data));scanner=Scanner(scan_data);await scanner.run_scan()
if __name__=='__main__':
	try:run(main())
	except KeyboardInterrupt:Console.print('\n[bold red1][!][/bold red1] Scan interrupted. Goodbye!',style=_A);exit(1)
