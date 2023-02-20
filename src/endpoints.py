import uuid
import os
from starlette import status
from starlette.endpoints import HTTPEndpoint, WebSocketEndpoint
from starlette.responses import RedirectResponse, HTMLResponse
from starlette.templating import Jinja2Templates
from starlette.responses import FileResponse

from .utils import get_keys
from .ws import Channel

template = Jinja2Templates(directory='templates')

class Homepage(HTTPEndpoint):
    async def get(self, request):
        return template.TemplateResponse('chat.html', {'request': request})


class Echo(WebSocketEndpoint):
    encoding = None
    channel_groups = 1
    id_list = [2, 1]

    async def on_connect(self, websocket) -> None:
        channel_uuid = self.id_list.pop()
        key = get_keys(channel_uuid)
        self.channel = Channel(channel_uuid=channel_uuid, websocket=websocket, encoding=self.encoding)
        Channel.group_add(self.channel, self.channel_groups, websocket)
        await websocket.accept()
        l = os.path.join('secrer_chat', 'test2_public.pem')
        with open(f"{channel_uuid}_public.pem", "r") as f:
            g = f.read()
            await self.channel.send(websocket, l)

    async def on_receive(self, websocket, data):
        print(data)
        l = []
        l.append(data)
        print(l)
        group = self.channel.CHANNEL_GROUPS.get(self.channel_groups)
        for web in group:
            await self.channel.send(web, data)
