from tornado.web import Application, RequestHandler

from tornados_wake import make_route_handler


def make_application():
    routes = [
        (r"/", GetOnlyHandler),
        (r"/pets", GetPostHandler),
        (r"/pets/(\S+)", GetPutDeletePatchHandler),
        (r"/pets/(\S+)/pictures", GetPostHandler),
        (r"/pets/(\S+)/pictures/(\d+)", GetPutDeletePatchHandler),
        (r"/toys", GetPostHandler),
        (r"/toys/(\d+)", GetPutDeletePatchHandler),
        (r"/assets/(.*)", GetOnlyHandler),
        (r"/routes", make_route_handler())
    ]
    app = Application(routes, default_handler_class=GetOnlyHandler)

    return app


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
