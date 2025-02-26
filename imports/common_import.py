from sys import exit
from pathlib import Path
from socket import AF_INET
from re import compile,match
from dotenv import load_dotenv
from rich.console import Console
from os import system,name,getenv
from random import choice,randint
from urllib.parse import urlparse
from aiofiles import open as aio_open
from async_timeout import timeout as asyncTimeout
from argparse import ArgumentParser,RawTextHelpFormatter
from aiohttp import ClientTimeout,ClientError,ClientSession
from asyncio import Semaphore,gather,run,TimeoutError,create_task
from socket import create_connection,timeout,setdefaulttimeout,error

Console = Console()
