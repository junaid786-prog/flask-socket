from flask import Flask
from flask_socketio import SocketIO

from socket_events import *

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def index():
    return 'Hello World!'

@socketio.on(SOCKET_EVENT_CONNECT)
def handle_connect():
    print('Client connected!')

@socketio.on(SOCKET_EVENT_DISCONNECT)
def handle_disconnect():
    print('Client disconnected!')

@socketio.on(SOCKET_EVENT_START)
def handle_start():
    print('Client started!')

@socketio.on(SOCKET_EVENT_STOP)
def handle_stop():
    print('Client stopped!')

@socketio.on(SOCKET_EVENT_SENSOR_DATA)
def handle_sensor_data(data):
    print('Client sent sensor data:', data)


if __name__ == '__main__':
    socketio.run(app, debug=True)