import tornado.ioloop
from tornado.web import Application, RequestHandler

from tornados_wake import make_route_handler


def make_default_application():
    routes = _get_common_routes() + [(r"/_routes", make_route_handler())]
    app = Application(routes, default_handler_class=NoRouteHandler)

    return app


def make_alternate_application():
    routes = _get_common_routes() + [
        (r"/_routes", make_route_handler(excludes={"/assets/%s", "/_routes"}, methods_default=False, tree_default=False))
    ]
    app = Application(routes, default_handler_class=NoRouteHandler)

    return app


def _get_common_routes():
    return [
    (r"/", GetOnlyHandler),
    (r"/pets", GetPostHandler),
    (r"/pets/(\S+)", GetPutDeletePatchHandler),
    (r"/pets/(\S+)/pictures", GetPostHandler),
    (r"/pets/(\S+)/pictures/(\d+)", GetPutDeletePatchHandler),
    (r"/toys", GetPostHandler),
    (r"/toys/(\d+)", GetPutDeletePatchHandler),
    (r"/assets/(.*)", GetOnlyHandler),
]


class GetOnlyHandler(RequestHandler):

    def get(self):
        self.finish('{"existing_resource": "here go"}')


class PostOnlyHandler(RequestHandler):

    def post(self):
        self.finish('{"new_resource": "here you go"}')


class GetPutDeletePatchHandler(GetOnlyHandler):

    def put(self):
        self.finish('{"replaced_resource": "here you go, hope you like it"}')

    def delete(self):
        self.finish('{"is there a resource here?": "not anymore!"}')

    def patch(self):
        self.finish('{"amended_resource": "Here you go"}')


class GetPostHandler(GetOnlyHandler, PostOnlyHandler):
    pass


class NoRouteHandler(RequestHandler):

    def get(self):
        self.finish('{"not":  "here"}')


def start_server(port):
    app = make_default_application()
    app.listen(port)

    tornado.ioloop.IOLoop.current().start()


if __name__ == '__main__':
    start_server(8000)