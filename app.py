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
	display_banner();OO00O000O0OOO0000=parse_arguments();OO000O0O000OOOOOO=ScanData(host=OO00O000O0OOO0000.url,wordlist_path=OO00O000O0OOO0000.wordlist,useragent_file=OO00O000O0OOO0000.user_agent)
	if not is_host_reachable(OO000O0O000OOOOOO.host):print(f"[!] Host {OO000O0O000OOOOOO.host} is not reachable. Exiting.");exit(1)
	await gather(load_wordlist(OO000O0O000OOOOOO),load_useragents(OO000O0O000OOOOOO));O00O00000OOO00O00=Scanner(OO000O0O000OOOOOO);await O00O00000OOO00O00.run_scan()
if __name__=='__main__':
	try:run(main())
	except KeyboardInterrupt:print('\n[!] Scan interrupted. Goodbye!');exit(1)
