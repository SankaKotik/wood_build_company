from aiohttp import web

app = web.Application()
app.router.add_static('/', path='shared')

web.run_app (app)
