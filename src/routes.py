from starlette.applications import Starlette
from starlette.routing import Route, Mount, WebSocketRoute
from starlette.staticfiles import StaticFiles

from .endpoints import Homepage, Echo


routes = [Route("/", Homepage),
          WebSocketRoute("/ws", Echo)]

