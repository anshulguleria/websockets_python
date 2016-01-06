from ws4py.websocket import WebSocket

class EchoWebSocket(WebSocket):
    def received_message(self, message):
        # called when server receives message

        # return the received message
        self.send(message.data, message.is_binary)
