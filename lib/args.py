from imports.common_import import Path,ArgumentParser

def parse_arguments():
    parser = ArgumentParser(description="Directory Scanner")
    parser.add_argument('-u', '--url', type=str, required=True, help='Target URL')
    parser.add_argument('-wl', '--wordlist', type=Path,help='Custom wordlist path')
    parser.add_argument('-ua', '--user-agent', type=Path, help='Custom User-Agent file path')
    parser.add_argument('-ws', '--webshell', help='Searching for webshell files in the web directory (Next Update)')
    return parser.parse_args()
