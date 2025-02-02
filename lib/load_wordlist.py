from imports.common_import import exit, aio_open,Console

async def load_wordlist(scan_data):
    try:
        async with aio_open(scan_data.wordlist_path, mode='r') as file:
            scan_data.paths = [line.strip() async for line in file] # Batasi jumlah path jika perlu
        Console.print(f'[+] Wordlist loaded: {scan_data.wordlist_path} ({sum(1 for _ in scan_data.paths)} paths)', style="bold")
    except FileNotFoundError:
        Console.print(f'[Error] Wordlist not found: {scan_data.wordlist_path}', style="bold red")
        exit(1)
    except PermissionError:
        Console.print(f'[Error] Permission denied: {scan_data.wordlist_path}', style="bold red")
        exit(1)
