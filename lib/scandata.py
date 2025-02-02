from imports.common_import import getenv, load_dotenv

load_dotenv()

class ScanData:
    def __init__(self, host, wordlist_path=None, useragent_file=None, threads=None, timeout=None):
        self.host = host
        self.wordlist_path = wordlist_path or getenv('wordlist')
        self.useragent_file = useragent_file or getenv('useragents')
        self.threads = threads or 3500
        self.timeout = timeout or 10
        self.paths = []
        self.results = []
        self.useragents = []
