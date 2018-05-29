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
