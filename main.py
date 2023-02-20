from starlette.applications import Starlette

from src.routes import routes

app = Starlette(routes=routes, debug=True)