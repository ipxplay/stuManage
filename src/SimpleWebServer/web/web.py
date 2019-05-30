import asyncio
from aiohttp import web
from SimpleWebServer.web.myjinja import html
from urllib.parse import parse_qs
from SimpleWebServer.util.txtutil import checkUserAndPwd

async def check(info):
#     print(parse_qs(info.query_string))
    username = parse_qs(info.query_string)["username"][0]
    password = parse_qs(info.query_string)["password"][0]
    msg = "fail!"  
#     if username=="wxit" and password=="wxit":
#         msg = "success!"
#     else:
#         pass
    if checkUserAndPwd(username, password):
        msg = "success!"
    else:
        pass
    return web.Response(body=html("msg.html",**locals()),content_type="text/html")
    


async def index(request):
    data=""
    with open("./views/login.html",encoding="utf-8") as f:
        data = f.read()
    data1 = web.Response(body=data,content_type="text/html")
    return data1

async def init(loop):
    app = web.Application()
    app.router.add_route('GET', '/', index)
    app.router.add_route('GET', '/check', check)
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner,"10.35.53.100","9000")
    await site.start()

loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()