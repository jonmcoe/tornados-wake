import sys

from tornados_wake import RoutesListElement
from tests import simple_app

if sys.version_info.major == 2:
    from mock import ANY
else:
    from unittest.mock import ANY


PLAIN_LIST = {
    "routes": [
       "/",
        "/_routes",
        "/assets/%s",
        "/pets",
        "/pets/%s",
        "/pets/%s/pictures",
        "/pets/%s/pictures/%s",
        "/toys",
        "/toys/%s"
    ]
}


METHODS_NO_TREE = {
    "routes": [
        ["/", ["GET"]],
        ["/_routes", ["GET"]],
        ["/assets/%s", ["GET"]],
        ["/pets", ["GET", "POST"]],
        ["/pets/%s", ["GET", "DELETE", "PATCH", "PUT"]],
        ["/pets/%s/pictures", ["GET", "POST"]],
        ["/pets/%s/pictures/%s", ["GET", "DELETE", "PATCH", "PUT"]],
        ["/toys", ["GET", "POST"]],
        ["/toys/%s", ["GET", "DELETE", "PATCH", "PUT"]]
    ]
}


TREE_NO_METHODS = {
    "routes": {
        "/": {
            "": None
        },
        "/_routes": {
            "": None
        },
        "/assets": {
            "/%s": {
                "": None
            }
        },
        "/pets": {
            "": None,
            "/%s": {
                "": None,
                "/pictures": {
                    "": None,
                    "/%s": {
                        "": None
                    }
                }
            }
        },
        "/toys": {
            "": None,
            "/%s": {
                "": None
            }
        }
    }
}


METHODS_AND_TREE = {
    "routes": {
        "/": {
            "": ["GET"]
        },
        "/_routes": {
            "": ["GET"]
        },
        "/assets": {
            "/%s": {
                "": ["GET"]
            }
        },
        "/pets": {
            "": ["GET", "POST"],
            "/%s": {
                "": ["GET", "DELETE", "PATCH", "PUT"],
                "/pictures": {
                    "": ["GET", "POST"],
                    "/%s": {
                        "": ["GET", "DELETE", "PATCH", "PUT"]
                    }
                }
            }
        },
        "/toys": {
            "": ["GET", "POST"],
            "/%s": {
                "": ["GET", "DELETE", "PATCH", "PUT"]
            }
        }
    }
}


PLAIN_LIST_WITHOUT_ROUTES_AND_ASSETS = {
    "routes": [
       "/",
        "/pets",
        "/pets/%s",
        "/pets/%s/pictures",
        "/pets/%s/pictures/%s",
        "/toys",
        "/toys/%s"
    ]
}


METHODS_NO_TREE_WITHOUT_ROUTES_AND_ASSETS = {
    "routes": [
        ["/", ["GET"]],
        ["/pets", ["GET", "POST"]],
        ["/pets/%s", ["GET", "DELETE", "PATCH", "PUT"]],
        ["/pets/%s/pictures", ["GET", "POST"]],
        ["/pets/%s/pictures/%s", ["GET", "DELETE", "PATCH", "PUT"]],
        ["/toys", ["GET", "POST"]],
        ["/toys/%s", ["GET", "DELETE", "PATCH", "PUT"]]
    ]
}


TREE_NO_METHODS_WITHOUT_ROUTES_AND_ASSETS = {
    "routes": {
        "/": {
            "": None
        },
        "/pets": {
            "": None,
            "/%s": {
                "": None,
                "/pictures": {
                    "": None,
                    "/%s": {
                        "": None
                    }
                }
            }
        },
        "/toys": {
            "": None,
            "/%s": {
                "": None
            }
        }
    }
}


METHODS_AND_TREE_WITHOUT_ROUTES_AND_ASSETS = {
    "routes": {
        "/": {
            "": ["GET"]
        },
        "/pets": {
            "": ["GET", "POST"],
            "/%s": {
                "": ["GET", "DELETE", "PATCH", "PUT"],
                "/pictures": {
                    "": ["GET", "POST"],
                    "/%s": {
                        "": ["GET", "DELETE", "PATCH", "PUT"]
                    }
                }
            }
        },
        "/toys": {
            "": ["GET", "POST"],
            "/%s": {
                "": ["GET", "DELETE", "PATCH", "PUT"]
            }
        }
    }
}


ROUTES_LIST = [
    RoutesListElement(path='/', handler_class=simple_app.GetOnlyHandler, http_methods=['GET']),
    RoutesListElement(path='/_routes', handler_class=ANY, http_methods=['GET']),
    RoutesListElement(path='/assets/%s', handler_class=simple_app.GetOnlyHandler, http_methods=['GET']),
    RoutesListElement(path='/pets', handler_class=simple_app.GetPostHandler, http_methods=['GET', 'POST']),
    RoutesListElement(path='/pets/%s', handler_class=simple_app.GetPutDeletePatchHandler, http_methods=['GET', 'DELETE', 'PATCH', 'PUT']),
    RoutesListElement(path='/pets/%s/pictures', handler_class=simple_app.GetPostHandler, http_methods=['GET', 'POST']),
    RoutesListElement(path='/pets/%s/pictures/%s', handler_class=simple_app.GetPutDeletePatchHandler, http_methods=['GET', 'DELETE', 'PATCH', 'PUT']),
    RoutesListElement(path='/toys', handler_class=simple_app.GetPostHandler, http_methods=['GET', 'POST']),
    RoutesListElement(path='/toys/%s', handler_class=simple_app.GetPutDeletePatchHandler, http_methods=['GET', 'DELETE', 'PATCH', 'PUT'])
]


ROUTES_LIST_WITHOUT_ROUTES_AND_ASSETS = [ROUTES_LIST[0]] + ROUTES_LIST[3:]
