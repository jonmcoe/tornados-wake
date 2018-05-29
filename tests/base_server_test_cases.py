from tornado.testing import AsyncHTTPTestCase

from tests import simple_app


class DefaultServerTestCase(AsyncHTTPTestCase):

    def get_app(self):
        return simple_app.make_default_application()


class AlternateServerTestCase(AsyncHTTPTestCase):

    def get_app(self):
        return simple_app.make_alternate_application()
