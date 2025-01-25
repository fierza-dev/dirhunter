from imports.common_import import gather,ClientSession
from lib.check_path import check_path

class Scanner:
    def __init__(self, scan_data):
        self.scan_data = scan_data

    async def limited_check_path(self, session, path):
        return await check_path(session, self.scan_data, path)

    async def run_scan(self):
        print(f'\n[+] Starting scan on {self.scan_data.host}')

        async with ClientSession() as session:
            tasks = [self.limited_check_path(session, path) for path in self.scan_data.paths]
            results = await gather(*tasks, return_exceptions=True)

        self.scan_data.results.extend([res for res in results if res and not isinstance(res, Exception)])

        print(f'\n[+] Scan complete: {len(self.scan_data.results)} valid paths found.')

