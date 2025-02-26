from imports.common_import import DNSResolver,error,AF_INET,Console

async def is_host_reachable(url):
    resolver = DNSResolver()

    try:
        await resolver.gethostbyname(url, AF_INET)
        Console.print(f"[[bold green]✓[/bold green]] Host: [white]{url}[/white]", style="bold")
        return True
    except error.DNSError as e:
        Console.print(f"[[bold red]✗[/bold red]] Host tidak ditemukan: [white]{url}[/white]", style="bold")
        return False
