from imports.common_import import Console

async def process_response(status, url, scan_data):
    if status in scan_data.statusCode:
        if status == 200:
            Console.print(f"[[bold sea_green1]{status}[/bold sea_green1]] [bold white]{url}[/bold white]")
        else:
            Console.print(f"[[bold red1]{status}[/bold red1]] [bold white]{url}[/bold white]")
        scan_data.results.append(url)