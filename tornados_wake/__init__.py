import json


def get_routes_list(application, excludes=frozenset()):
    return sorted([i._path for i in application.handlers[0][1] if i._path not in excludes])


def get_route_tree_dict(application, excludes=frozenset()):
    routes_split = [route.split('/')[1:] for route in get_routes_list(application, excludes=excludes)]
    return _make_tree_from_list(routes_split)


def make_route_handler(base_handler,
                       excludes=frozenset(), pretty_keyword='pretty', jsonify=True, respond_func_str='finish'):

    class RouteHandler(base_handler):

        def get(self):
            if pretty_keyword and self.get_argument(pretty_keyword, None):
                payload = {'routes': get_route_tree_dict(self.application, excludes=excludes)}
            else:
                payload = {'routes': get_routes_list(self.application, excludes=excludes)}
            respond_func = getattr(self, respond_func_str)

            respond_func(json.dumps(payload) if jsonify else payload)

    return RouteHandler


def _make_tree_from_list(list_split):
    d = {'/': {}}
    for route in list_split:
        subdict = d['/']
        for depth, segment in enumerate(route):
            if segment not in subdict:
                subdict[segment] = {'': {}} if depth == len(route) - 1 else {}
            subdict = subdict[segment]
    _prune(d)
    return d


def _prune(d):
    for k, v in d.items():
        if v == {'': {}} or v == {}:
            d[k] = None
        elif isinstance(v, dict):
            _prune(v)
