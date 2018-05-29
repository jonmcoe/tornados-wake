import json

from parameterized import parameterized
from tests.base_server_test_cases import AlternateServerTestCase, DefaultServerTestCase
from tests import fixtures


class DefaultHandlerTestCase(DefaultServerTestCase):

    @parameterized.expand([
        ('/_routes?methods=false', fixtures.PLAIN_LIST),
        ('/_routes', fixtures.METHODS_NO_TREE),
        ('/_routes?tree=true&methods=false', fixtures.TREE_NO_METHODS),
        ('/_routes?tree=true', fixtures.METHODS_AND_TREE)
    ])
    def test_http_response(self, path, expected):
        res = self.fetch(path)
        self.assertEqual(json.loads(res.body), expected)

    def test_response_ordering_tree(self):
        res_tree = self.fetch('/_routes?tree=1')
        index_assets = res_tree.body.find('assets')
        index_pets = res_tree.body.find('pets')
        index_toys = res_tree.body.find('toys')
        self.assertGreater(index_pets, index_assets)
        self.assertGreater(index_toys, index_pets)

    def test_response_ordering_tree_no_methods(self):
        res_tree = self.fetch('/_routes?tree=1&methods=false')
        index_assets = res_tree.body.find('assets')
        index_pets = res_tree.body.find('pets')
        index_toys = res_tree.body.find('toys')
        self.assertGreater(index_pets, index_assets)
        self.assertGreater(index_toys, index_pets)


class AlternateHandlerTestCase(AlternateServerTestCase):

    @parameterized.expand([
        ('/_routes', fixtures.PLAIN_LIST_WITHOUT_ROUTES_AND_ASSETS),
        ('/_routes?methods=true', fixtures.METHODS_NO_TREE_WITHOUT_ROUTES_AND_ASSETS),
        ('/_routes?tree=true', fixtures.TREE_NO_METHODS_WITHOUT_ROUTES_AND_ASSETS),
        ('/_routes?tree=true&methods=true', fixtures.METHODS_AND_TREE_WITHOUT_ROUTES_AND_ASSETS)
    ])
    def test_http_response(self, path, expected):
        res = self.fetch(path)
        self.assertEqual(json.loads(res.body), expected)
