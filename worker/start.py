"""It sends message to socket server.

This file sends message after some regular intervals to the
socket server hosted by the server application."""

from ws4py.client.threadedclient import WebSocketClient


# create this class inside any python file and
# instantiate it. Then its instance can be used
# to send events to socket server
class SomeWork(WebSocketClient):

    def opened(self):
        def data_provider():
            for i in range(1, 200, 25):
                yield "#" * i

        self.send(data_provider())

        for i in range(0, 200, 25):
            print i
            self.send("*" * i)

    def closed(self, code, reason = None):
        print "Closed down", code, reason

    def received_message(self, message):
        print message
        if len(message) == 175:
            self.close(reason="Bye bye")


if __name__ == "__main__":
    # start what ever you want
    try:
        ws = SomeWork('ws://localhost:8080/ws',
                protocols=['http-only', 'chat'])
        ws.connect()
        ws.run_forever()
    except KeyboardInterrupt:
        ws.close()

