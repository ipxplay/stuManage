import asyncio
from aiohttp import web
from SimpleWebServer.web.myjinja import html
from urllib.parse import parse_qs
from SimpleWebServer.util.txtutil import checkUserAndPwd
from SimpleWebServer.web.model.model import Model
from SimpleWebServer.util.weblogging import weblog
from SimpleWebServer.util.configutil import getPort
import tkinter


async def check(info):
#     print(parse_qs(info.query_string))
    username = parse_qs(info.query_string)["username"][0]
    password = parse_qs(info.query_string)["password"][0]
    msg = "fail!"  
    model = Model()
    if model.checkUserSAndpwd(username, password):
        msg = "success!"
    else:
        pass
    return web.Response(body=html("msg.html",**locals()),content_type="text/html")

    
async def index(request):
    data=""
    
    ip = str(request._transport_peername[0])
    path = str(request.message.url)
    logfile =os.path.abspath("../../logs/web.log") 
#     print(logfile)
    weblog(logfile,ip, path)

    with open("../views/login.html",encoding="utf-8") as f:
        data = f.read()
    data1 = web.Response(body=data,content_type="text/html")
    return data1
import os

async def hello(request):
    data = "hello world!"
    data1 = web.Response(body=data,content_type="text/html")
    return data1

async def posthello(request):
    data = "this is a post hello world!"
    data1 = web.Response(body=data,content_type="text/html")
    return data1

async def init(loop):
    app = web.Application()
    app.router.add_route('GET', '/', index)
    app.router.add_route('GET', '/check', check)
    
    app.router.add_route('GET', '/hello', hello)
    app.router.add_route("POST", '/posthello', posthello)
#     web.run_app(app)
        
    runner = web.AppRunner(app)
    await runner.setup()
    
    site = web.TCPSite(runner=runner,port=getPort())
    await site.start()

loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()