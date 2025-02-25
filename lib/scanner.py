from lib.check_path import check_path
from imports.common_import import gather, ClientSession, Console,create_task

class Scanner:
    def __init__(self, config):
        self.GetConfig = config

    async def limited_check_path(self, session, path):
        return await check_path(session, self.GetConfig, path)
    
    async def run_scan(self):
        Console.print(f'\n[+] Starting scan on [bold white]{self.GetConfig.host}[/bold white]', style="bold")
        
        async with ClientSession() as session:
            tasks = [create_task(self.limited_check_path(session, path)) for path in self.GetConfig.paths]
            results = await gather(*tasks, return_exceptions=True)

        self.GetConfig.results.extend([res for res in results if res and not isinstance(res, Exception)])

        Console.print(f'\n[+] PATH : {len(self.GetConfig.results)} valid paths found.', style="bold")
        Console.print(f"\n[+] Scanning Complete ...", style="bold bright_white")