import logging; logging.basicConfig(level=logging.INFO)

import asyncio,os,json,time,aiomysql
from datetime import datetime

#导入
from aiohttp import web

def index(request):
    return web.Response(body='<h1>测试</h1>',content_type='text/html',charset = 'utf-8')

@asyncio.coroutine
def init(loop):
    app = web.Application(loop=loop)
    app.router.add_route('GET','/',index)
    srv = yield from loop.create_server(app.make_handler(),'127.0.0.1',9000)
    logging.info('服务器启动 URLhttp://127.0.0.1:9000')
    return srv


loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()