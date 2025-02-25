from imports.common_import import system,name,Console

def display_banner():
    system("cls" if name == "nt" else "clear")
    
    BANNER = """
    
██████  ██ ██████  ██   ██ ██    ██ ███    ██ ████████ ███████ ██████  
██   ██ ██ ██   ██ ██   ██ ██    ██ ████   ██    ██    ██      ██   ██ 
██   ██ ██ ██████  ███████ ██    ██ ██ ██  ██    ██    █████   ██████  
██   ██ ██ ██   ██ ██   ██ ██    ██ ██  ██ ██    ██    ██      ██   ██ 
██████  ██ ██   ██ ██   ██  ██████  ██   ████    ██    ███████ ██   ██ 

[!] Legal Disclaimer : This tool is for educational purposes only. 
    Use only on systems you have permission to test. Unauthorized use is illegal.
    The developers are not responsible for any damages or legal issues. USE AT YOUR OWN RISK.
"""
    Console.print(f"[bold bright_white]{BANNER}[bold bright_white]")