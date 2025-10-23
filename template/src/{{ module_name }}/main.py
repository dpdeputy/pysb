from {{ module_name }}.server import make_app
import tornado.ioloop
import logging

def main():
    logging.basicConfig(level=logging.INFO)
    app = make_app()
    app.listen(8888)
    logging.info("Server listening on port 8888")
    tornado.ioloop.Ioloop.current().start()

if __name__ == "__main__":
    main()
