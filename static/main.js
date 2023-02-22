document.addEventListener('DOMContentLoaded', function() {
  const socketURI = "ws://localhost:8000/ws";
  const webSocket = new WebSocket(socketURI);

  const downloadLinkEl = document.querySelector('#downloadFile');
  const sendFormEl = document.querySelector('#sendForm');


  webSocket.addEventListener('open', (event) => {
    console.log("Socket connection is ready");

  })

  webSocket.addEventListener("message", (event) => {
    console.log("MESSAGE", event);
    const messages = document.getElementById('messages')
    const message = document.createElement('li');
    const messageLink = document.createElement("a");
    messageLink.setAttribute("id", "downloadFile")
    messageLink.href = event.data;
    messageLink.innerText = "Download public key";
    messageLink.download = event.data.split('/').slice(-1);
    messages.appendChild(message);
    message.appendChild(messageLink);
  });


  downloadLinkEl.addEventListener("click", function(e) {
    e.preventDefault();
    e.click();
  });

  sendFormEl.addEventListener("click", function(e) {
    e.preventDefault();
    alert("SEND FORm");
    const data = document.forms.messageForm;
    webSocket.send(data);
  })



})