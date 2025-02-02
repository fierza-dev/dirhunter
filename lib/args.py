from imports.common_import import Path, ArgumentParser

def parse_arguments():
    parser = ArgumentParser(
        usage="%(prog)s -u <URL> [options]",
    )
    
    parser.add_argument('-u', '--url', type=str, help='Target URL')
    parser.add_argument('-v', '--version', action='store_true', help='Show the version of Dirhunter')
    parser.add_argument('-wl', '--wordlist', type=Path, help='Custom wordlist file path')
    parser.add_argument('-ua', '--user-agent', type=Path, help='Custom User-Agent file path')
    parser.add_argument('--threads', type=int, help="Custom Speed Scanning Using Threads, e.g., 50 (min) to 3500 (max)")
    parser.add_argument('-t','--time-out', type=int, help="Custom Time Out Scanning, e.g., 10 (deafult)")
    
    return parser.parse_args()
