import ast
from starlette.endpoints import HTTPEndpoint, WebSocketEndpoint
from starlette.templating import Jinja2Templates

from .utils import get_keys, create_signature, check_signature
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
        with open(f"temp/{channel_uuid}_public.pem", "r") as f:
            await self.channel.send(websocket, f"temp/{channel_uuid}_public.pem")

    async def on_receive(self, websocket, data):
        print(data)
        # data_dict = ast.literal_eval(data)
        # message = data_dict.get('message')
        # key = data_dict.get('key')
        # signature = data_dict.get('signature')
        # signature = create_signature(self.channel.channel_uuid, message)
        # print(signature)
        # check_signature(key, signature, message)
        group = self.channel.CHANNEL_GROUPS.get(self.channel_groups)
        for web in group:
            await self.channel.send(web, data)
