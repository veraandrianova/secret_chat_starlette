class Channel:
    CHANNEL_GROUPS = {}

    def __init__(self, channel_uuid, websocket, encoding):
        self.channel_uuid = channel_uuid
        self.websocket = websocket
        self.encoding = encoding

    def group_add(self, group, websocket):
        self.CHANNEL_GROUPS.setdefault(group, [])
        self.CHANNEL_GROUPS[group].append(websocket)

    async def send(self, websocket, data):
        if self.encoding is None:
            if type(data) == 'str':
                await websocket.send_text(data)
            else:
                await websocket.send_bytes(data)
        elif self.encoding == "json":
            try:
                await websocket.send_json(data)
            except RuntimeError:
                pass
        elif self.encoding == "text":
            try:
                await websocket.send_text(data)
            except RuntimeError:
                pass
        elif self.encoding == "bytes":
            try:
                await websocket.send_bytes(data)
            except RuntimeError:
                pass
        else:
            try:
                await websocket.send(data)
            except RuntimeError:
                pass
