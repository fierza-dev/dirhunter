from imports.app_import import load_proxy,load_wordlist
from lib.load_useragents import load_useragents
from imports.common_import import gather

async def load_resources(config):
    await gather(
        load_wordlist(config),
        load_useragents(config),
        load_proxy(config),
    )