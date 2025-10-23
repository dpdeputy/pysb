import tornado.ioloop
import tornado.web
import tornado.websocket
import logging

class ChatHandler(tornado.websocket.WebSocketHandler):
    clients = set()

    def open(self):
        logging.info("WebSocket opened")
        ChatHandler.clients.add(self)

    def on_message(self, message):
        logging.info(f"Received message: {message}")
        for client in ChatHandler.clients:
            if client != self:
                client.write_message(message)

    def on_close(self):
        logging.info("WebSocket closed")
        ChatHandler.clients.remove(self)

    def check_origin(self, origin):
        return True

def make_app():
    return tornado.web.Application([
        (r"/ws", ChatHandler),
    ])

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    app = make_app()
    app.listen(8888)
    logging.info("Server listening on port 8888")
    tornado.ioloop.IOLoop.current().start()
