import asyncio
from lib.get_headers import get_headers
from lib.process_response import process_response
from imports.common_import import Semaphore,choice,ClientSession
async def check_path(session,GetConfig,path):
	A=GetConfig;D=Semaphore(A.threads);B=A.host+f"/{path.lstrip("/")}";E=await get_headers(choice(A.useragents),A.httpSmug);F=choice(A.Getproxy)if A.Getproxy else A.proxy
	async with D:
		async with asyncio.timeout(A.timeout):
			async with session.get(B,headers=E,proxy=F or None,allow_redirects=False)as C:await process_response(C.headers,C.status,B,A)
