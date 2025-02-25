from imports.common_import import exit, aio_open,Console

async def load_proxy(GetConfig):
    try:
        if GetConfig.random_proxy:
            async with aio_open(GetConfig.random_proxy, mode='r') as file:
                GetConfig.Getproxy = [line.strip() async for line in file]
            Console.print(f'[+] proxy loaded: {GetConfig.random_proxy} ({len(GetConfig.Getproxy)} paths)', style="bold")
    except FileNotFoundError:
        Console.print(f'[Error] Proxy not found: {GetConfig.Getproxy}', style="bold red")
        exit(1)
    except PermissionError:
        Console.print(f'[Error] Permission denied: {GetConfig.Getproxy}', style="bold red")
        exit(1)