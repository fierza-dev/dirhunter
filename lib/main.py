from imports.app_import import *

async def main():
    display_banner()

    args = parse_arguments()

    if args.version:
        version()

    config = await initialize_Configuration(args)
    await check_host_reachability(config.host)
    await load_resources(config)

    scanner = Scanner(config)
    await scanner.run_scan()