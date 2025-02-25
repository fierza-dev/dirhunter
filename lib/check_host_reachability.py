from imports.app_import import is_host_reachable
from imports.common_import import Console

async def check_host_reachability(host):
    if not await is_host_reachable(host):
        Console.print(f'[bold red1][!][/bold red1] Host {host} is not reachable. Exiting.', style="bold")
        exit(1)