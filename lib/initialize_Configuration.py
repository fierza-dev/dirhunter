from lib.check_cms import check_cms
from lib.Configuration import Configuration

async def initialize_Configuration(args):
    cms = args.scan_with_cms if check_cms(args.scan_with_cms) else None

    return Configuration(
        host=args.url,
        wordlist_path=args.wordlist,
        useragent_file=args.user_agent,
        threads=args.threads,
        timeout=args.time_out,
        cms=cms,
        conf=args.scan_cms_config,
        adminlogin=args.scan_admin_login,
        randomProxy=args.random_proxy,
        proxy=args.proxy,
        statusCode=args.status_code,
        httpSmug =args.http_smuggling,
    )