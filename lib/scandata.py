from imports.common_import import getenv,cycle,load_dotenv

load_dotenv()

class ScanData:
    def __init__(self, host, wordlist_path=None, useragent_file=None):
        self.host = host
        self.wordlist_path = wordlist_path or getenv('wordlist')
        self.useragent_file = useragent_file or getenv('useragents')
        self.paths = []
        self.results = []
        self.useragents = []
        self.current_useragent = None

    def set_random_useragent(self):
        self.current_useragent = next(cycle(self.useragents)) if self.useragents else next(cycle(self.useragent_file))