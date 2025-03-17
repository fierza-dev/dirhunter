from imports.common_import import getenv, load_dotenv

load_dotenv()

class Configuration:
    def __init__(self, host, wordlist_path=None, useragent_file=None, threads=None, timeout=None, cms=None, conf=None, adminlogin=None, randomProxy=None, proxy=None, statusCode=None,  httpSmug=None):
        self.host = host.rstrip('/')
        self.wordlist_path = self._get_wordlist_path(wordlist_path, cms, conf, adminlogin)
        self.useragent_file = useragent_file or getenv('useragents')
        self.random_proxy = getenv("random_proxy") if randomProxy else None
        self.proxy = proxy
        self.threads = threads or 3500
        self.timeout = timeout or 10
        self.statusCode = statusCode if isinstance(statusCode, list) else [200,301,302,303,307,308]
        self.paths = []
        self.results = []
        self.Getproxy = []
        self.useragents = []
        self.httpSmug =  httpSmug

    def _get_wordlist_path(self, wordlist_path, cms, conf, adminlogin):
        if wordlist_path:
            return wordlist_path
        if cms:
            return getenv(cms)
        if conf:
            return getenv("config")
        if adminlogin:
            return getenv("adminlogin")
        return getenv('wordlist')
