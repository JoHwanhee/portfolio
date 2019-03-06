from os import environ
from FlaskWebProject1 import app

if __name__ == '__main__':
    HOST = environ.get('SERVER_HOST', '127.0.0.1')
    try:
        PORT = int(environ.get('SERVER_PORT', '8080'))
    except ValueError:
        PORT = 8080
    app.run(HOST, PORT)
