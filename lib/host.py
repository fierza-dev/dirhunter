from imports.common_import import urlparse,Console

async def is_host_reachable(url):
    parsed_url = urlparse(url)
    
    if not (parsed_url.scheme and parsed_url.netloc):
        Console.print(f"[[bold red1]x[/bold red1]] Invalid URL format: {url}", style="bold")
        return None
    
    Console.print(f"[[bold sea_green1]✓[/bold sea_green1]] Host: {parsed_url.netloc}", style="bold bright_white")
    return True
