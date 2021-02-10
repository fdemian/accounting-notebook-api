import ssl
import tornado.web
from base64 import b64encode
from os import urandom, path
from api.Routes import get_app_routes
from api.Options import load_options
from tornado.httpserver import HTTPServer

config_file = 'config.ini'
static_path = path.join(path.dirname(__file__), "static")

if __name__ == "__main__":
    options = load_options(config_file)
    routes = get_app_routes(static_path)
    options['notification_handlers'] = dict([])
    application = tornado.web.Application(routes,balance=options["initial_balance"], transactions=[], **options)
    app_port = options["port"]

    # Start application.
    server = HTTPServer(application)
    server.listen(app_port)
    tornado.ioloop.IOLoop.instance().start()