from imports.common_import import DNSResolver,error,AF_INET,Console,error

async def is_host_reachable(url):
    host = DNSResolver()
    
    try:
        await host.gethostbyname(url, AF_INET)
        Console.print(f"[[bold sea_green1]✓[/bold sea_green1]] Host: [bright_white]{url}[/bright_white]", style="bold")
        return True
    except error.DNSError:
        return False
