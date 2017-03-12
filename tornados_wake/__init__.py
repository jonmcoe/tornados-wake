import json
from operator import itemgetter

from tornado.web import RequestHandler


def get_routes_list(application, excludes=frozenset()):
    return sorted(((i._path, _methods_from_handler_class(i.handler_class))
            for i in application.handlers[0][1]
            if i._path not in excludes),
           key=itemgetter(0))


def get_route_tree_dict(routes_list):
    d = {}
    for route, methods in routes_list:
        methods = list(methods)
        route_split = route.split('/')[1:]  # eliminate empty string in leading position
        subdict = d
        for depth, segment in enumerate(route_split):
            if '/' + segment not in subdict:
                is_last_segment = depth == len(route_split) - 1
                subdict['/' + segment] = {'': methods} if is_last_segment else {}
            subdict = subdict['/' + segment]
    return d


def make_route_handler(base_handler=RequestHandler,
                       excludes=frozenset(),
                       tree_keyword='tree', tree_default=False,
                       methods_keyword='methods', methods_default=True,
                       jsonify=True, respond_func_str='finish'):

    class RouteHandler(base_handler):

        def get(self):
            include_methods = methods_keyword and self.get_argument(methods_keyword, methods_default)
            make_tree = tree_keyword and self.get_argument(tree_keyword, tree_default)

            routes = get_routes_list(self.application, excludes=excludes)

            if make_tree:
                payload = {'routes': get_route_tree_dict(routes)}
            else:
                payload = {'routes': get_routes_list(self.application, excludes=excludes)}
            respond_func = getattr(self, respond_func_str)

            respond_func(json.dumps(payload) if jsonify else payload)

    return RouteHandler


def _methods_from_handler_class(hc):
    """
    Given a handler class, return supported methods.
    Will *not* work for any methods set dynamically (like setattr in the `prepare` or something)

    :param hc: Handler class
    :return: set of implemented methods ex. {'GET', 'POST' 'PUT'}
    """

    BASES = {RequestHandler, object}
    candidates = hc.SUPPORTED_METHODS
    result = set()
    for candidate in candidates:
        if _class_has_method(hc, candidate, BASES):
            result.add(candidate)
    return result


def _class_has_method(klass, method, bases):
    if klass in bases:
        return False
    else:
        return method.lower() in klass.__dict__ or any(_class_has_method(b, method, bases) for b in klass.__bases__)
