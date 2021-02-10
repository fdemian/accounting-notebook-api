# Route imports
from api.routes.Index import IndexHandler
from api.routes.NotFound import NotFoundHandler
from api.routes.Transactions import TransactionHandler, TransactionsHandler
from api.routes.Account import AccountHandler
from tornado.web import StaticFileHandler
from os import path

def get_app_routes(static_path):

    routes = [
       (r"/api/transactions/(.*)", TransactionHandler),
       (r"/api/transactions", TransactionsHandler),
       (r"/api/account", AccountHandler),
       (r"/api/(.*)", NotFoundHandler),
       (r"/static/(.*)", StaticFileHandler, {"path": static_path}),
       (r"/(manifest\.json)", StaticFileHandler, {"path": static_path}),
       (r"/(favicon\.png)", StaticFileHandler, {"path": static_path}),
       (r"/(robots\.txt)", StaticFileHandler, {"path": static_path}),
       (r"/.*", IndexHandler)
    ]

    return routes
