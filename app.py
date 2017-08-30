from config import secret_key
from flask import Flask
from routes import main as main_route
from websocket_route import socketio

def configured_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = secret_key
    app.register_blueprint(main_route)
    socketio.init_app(app)
    return app

if __name__ == '__main__':
    app = configured_app()
    app.debug = True
    socketio.run(app,host='127.0.0.1', port=810)