const ws = new WebSocket('ws://localhost:8000/ws')

ws.onopen = function (event) {
    console.log(event)
    newUser()
}

ws.onmessage = function (event) {
    console.log(event)
    let data = JSON.parse(event.data)
    switch (data.action) {
        case 'new':
            chatList(data.chats)
    }
}

function send(data) {
    ws.send(JSON.stringify(data))
}


function createChat(event) {
    send({action: 'create'})
}

document.getElementById('chat-create').addEventListener('click', createChat)