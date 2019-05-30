import asyncio
from aiohttp import web


def index(request):
    return web.Response(body="<html><title>WXIT</title><body><h3>Hello</h3></body></html>",content_type="text/html")

async def init(loop):
    app = web.Application()
    app.router.add_route('GET', '/', index)
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner,"10.35.53.100","9000")
    await site.start()

loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()