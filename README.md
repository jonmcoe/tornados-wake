# Tornado's Wake
Route mapper for charting where your `tornado` goes.

[![Latest Version](https://badge.fury.io/py/tornados-wake.png)](https://pypi.python.org/pypi/tornados-wake/)
[![Build Status](https://travis-ci.org/jonmcoe/tornados-wake.svg?branch=master)](https://travis-ci.org/jonmcoe/tornados-wake)

Add an entry like:

`(r"/_routes", tornados_wake.make_route_handler()),`

to your application's routes list and it will be served at `localhost:8080/_routes`

get a response like (simplest `/_routes?methods=false`):

```json
{
  "routes": [
    "/",
    "/assets/%s",
    "/pets",
    "/pets/%s",
    "/pets/%s/pictures",
    "/pets/%s/pictures/%s",
    "/routes",
    "/toys",
    "/toys/%s"
  ]
}
```

or for a tree-like structure and an indication of which HTTP methods are available, use `/_routes?tree=true`

```json
{
  "routes": {
    "/pets": {
      "": [
        "GET",
        "POST"
      ],
      "/%s": {
        "": [
          "GET",
          "DELETE",
          "PATCH",
          "PUT"
        ],
        "/pictures": {
          "": [
            "GET",
            "POST"
          ],
          "/%s": {
            "": [
              "GET",
              "DELETE",
              "PATCH",
              "PUT"
            ]
          }
        }
      }
    },
    "/toys": {
      "": [
        "GET",
        "POST"
      ],
      "/%s": {
        "": [
          "GET",
          "DELETE",
          "PATCH",
          "PUT"
        ]
      }
    },
    "/routes": {
      "": [
        "GET"
      ]
    },
    "/": {
      "": [
        "GET"
      ]
    },
    "/assets": {
      "/%s": {
        "": [
          "GET"
        ]
      }
    }
  }
}
```

A few kwargs are available to the handler's constructor for customizing query args/defaults,
specifying private routes to exclude, and using a base class specific to your app instead of tornado's
standard `RequestHandler`.

```
def make_route_handler(base_handler=RequestHandler,
                       excludes=frozenset(),
                       tree_keyword='tree', tree_default=False,
                       methods_keyword='methods', methods_default=True,
                       jsonify=True, respond_func_str='finish'):
```

If you do not want to use the handler at all, but are still interested in getting a list of routes you can use/format in
your own way then you should instead use `tornados_wake.get_routes_list` which has the following signature:

```
def get_routes_list(application, excludes=frozenset()):
```

and returns a namedtuple called `RoutesListElement` containing
* `path` (str)
* `handler_class` (class)
* `http_methods` (List[str])
