from unittest import TestCase

from tornados_wake import get_routes_list
from tests import fixtures
from tests.simple_app import make_default_application


class RoutesListTestCase(TestCase):

    def test_routes_list(self):
        self.assertEquals(get_routes_list(make_default_application()), fixtures.ROUTES_LIST)

    def test_routes_list_with_excludes(self):
        self.assertEquals(
            get_routes_list(make_default_application(), excludes={"/_routes", "/assets/%s"}),
            fixtures.ROUTES_LIST_WITHOUT_ROUTES_AND_ASSETS
        )
