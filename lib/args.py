from imports.common_import import Path, ArgumentParser,RawTextHelpFormatter

def parse_arguments():
    parser = ArgumentParser(
        usage="%(prog)s -u <URL> [options]",
        formatter_class=RawTextHelpFormatter,
    )

    # General Options
    parser.add_argument('-u', '--url', type=str, help='Target URL')
    parser.add_argument('-v', '--version', action='store_true', help='Show the version of Dirhunter')

    # Custom Options
    customOptions = parser.add_argument_group("Custom Options")
    customOptions.add_argument('--wordlist', type=Path, help='Custom wordlist file path')
    customOptions.add_argument('--user-agent', type=str, help='Custom User-Agent string')
    customOptions.add_argument('--threads', type=int, help="Custom Speed Scanning Using Threads (e.g., 50 to 3500)")
    customOptions.add_argument('--time-out', type=int, help="Custom Timeout Scanning (default: 10 seconds)")
    customOptions.add_argument('--http-smuggling', action='store_true', help="Bypass WAF Using Http Smuggling")

    # Scanning Modes
    scanningModes = parser.add_argument_group("Scanning Modes Options")
    scanningModes.add_argument('--scan-with-cms', type=str, help="Scan web directory using CMS (e.g., wordpress)")
    scanningModes.add_argument('--scan-cms-config', action='store_true', help="Scan CMS configuration files")
    scanningModes.add_argument('--scan-admin-login', action='store_true', help="Scan admin login directories")
    scanningModes.add_argument("--status-code", type=int, nargs='+',help="Include status codes")

    # Proxy Options
    proxyOptions = parser.add_argument_group("Proxy Options")
    proxyOptions .add_argument('--random-proxy', action='store_true', help="Scan with a random proxy")
    proxyOptions .add_argument('--proxy', type=str, help="Use a specific proxy (e.g., socks5://127.0.0.1:12345)")

    return parser.parse_args()
