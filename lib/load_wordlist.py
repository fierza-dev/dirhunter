from imports.common_import import exit, aio_open,Console

async def load_wordlist(GetConfig):
    try:
        async with aio_open(GetConfig.wordlist_path, mode='r') as file:
            GetConfig.paths = [line.strip() async for line in file]
        Console.print(f'[+] Wordlist loaded: {GetConfig.wordlist_path} ({len(GetConfig.paths)} paths)', style="bold")
    except FileNotFoundError:
        Console.print(f'[Error] Wordlist not found: {GetConfig.wordlist_path}', style="bold red")
        exit(1)