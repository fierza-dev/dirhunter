from lib.get_headers import get_headers
from lib.process_response import process_response
from imports.common_import import TimeoutError,Semaphore,choice,ClientSession,ClientError,asyncTimeout
async def check_path(session,GetConfig,path):
	semaphore=Semaphore(GetConfig.threads);url=GetConfig.host+f"/{path.lstrip("/")}";headers=await get_headers(choice(GetConfig.useragents),GetConfig.httpSmug);proxy=choice(GetConfig.Getproxy)if GetConfig.Getproxy else GetConfig.proxy
	try:
		async with semaphore:
			async with asyncTimeout(GetConfig.timeout):
				async with session.get(url,headers=headers,proxy=proxy or None,allow_redirects=False)as response:await process_response(response.status,url,GetConfig)
	except(ClientError,TimeoutError):pass
