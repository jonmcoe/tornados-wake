from tornado.testing import AsyncHTTPTestCase

from tests import simple_app


class BaseHTTPTestCase(AsyncHTTPTestCase):

    def get_app(self):
        return simple_app.make_application()
