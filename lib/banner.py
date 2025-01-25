from imports.common_import import Fore,Style,system,name

def display_banner():
    system("cls" if name == "nt" else "clear")
    
    ANSI_WHITE = Fore.LIGHTWHITE_EX
    RESET = Style.RESET_ALL
    
    BANNER = """
▗▄▄▄ ▗▄▄▄▖▗▄▄▖ ▗▖ ▗▖▗▖ ▗▖▗▖  ▗▖▗▄▄▄▖▗▄▄▄▖▗▄▄▖ 
▐▌  █  █  ▐▌ ▐▌▐▌ ▐▌▐▌ ▐▌▐▛▚▖▐▌  █  ▐▌   ▐▌ ▐▌
▐▌  █  █  ▐▛▀▚▖▐▛▀▜▌▐▌ ▐▌▐▌ ▝▜▌  █  ▐▛▀▀▘▐▛▀▚▖
▐▙▄▄▀▗▄█▄▖▐▌ ▐▌▐▌ ▐▌▝▚▄▞▘▐▌  ▐▌  █  ▐▙▄▄▖▐▌ ▐▌ v2.2 (BETA)

[!] Legal Disclaimer : This tool is for educational purposes only. 
    Use only on systems you have permission to test. Unauthorized use is illegal.
    The developers are not responsible for any damages or legal issues. USE AT YOUR OWN RISK.
"""
    print(ANSI_WHITE+BANNER+RESET)
