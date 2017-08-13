from unittest import skip

from tests.base import BaseHTTPTestCase


class TestHandlerTestCase(BaseHTTPTestCase):

    def test_routes_list_with_methods(self):
        x = self.fetch('/_routes')
        # TODO: better fixtures, maybe compare dicts
        expected = b'{"routes": [["/", ["GET"]], ["/_routes", ["GET"]], ["/assets/%s", ["GET"]], ["/pets", ["GET", "POST"]], ["/pets/%s", ["GET", "DELETE", "PATCH", "PUT"]], ["/pets/%s/pictures", ["GET", "POST"]], ["/pets/%s/pictures/%s", ["GET", "DELETE", "PATCH", "PUT"]], ["/toys", ["GET", "POST"]], ["/toys/%s", ["GET", "DELETE", "PATCH", "PUT"]]]}'
        self.assertEqual(x.body, expected)

    @skip
    def test_routes_tree_with_methods(self):
         x = self.fetch('/_routes?tree=true')
         expected = 'todo'
         self.assertEqual(x.body, expected)
