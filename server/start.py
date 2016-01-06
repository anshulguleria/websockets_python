import cherrypy
from ws4py.server.cherrypyserver import WebSocketPlugin
from ws4py.server.cherrypyserver import WebSocketTool
from echoserver import EchoWebSocket


WebSocketPlugin(cherrypy.engine).subscribe()
cherrypy.tools.websocket = WebSocketTool()

class Root(object):

    @cherrypy.expose
    def index(self):
        return "hello world!"

    @cherrypy.expose
    def ws(self):
        handler = cherrypy.request.ws_handler

if __name__ == "__main__":
    cherrypy.tree.mount(Root(), '/', {
        '/ws': {
            "tools.websocket.on": True,
            "tools.websocket.handler_cls": EchoWebSocket
        }
    })

    cherrypy.engine.start()
    cherrypy.engine.block()
