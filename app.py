from flask import Flask
from flask_socketio import SocketIO, send, emit
from json import dumps, loads
from socket_events import *
from csv_util import *


app = Flask(__name__)
socketio = SocketIO(app)


# start storing individual sensor data in a list on start event and on stop event, save the list to a csv file and clear the list also send the stats to the client
# on sensor data event, append the data to the list

my_sensor_data = []

@socketio.on(SOCKET_EVENT_CONNECT)
def handle_connect():
    print('Client connected!')

@socketio.on(SOCKET_EVENT_DISCONNECT)
def handle_disconnect():
    print('Client disconnected!')

@socketio.on(SOCKET_EVENT_START)
def handle_start_connection(data):
    print('Client started!')
    my_sensor_data.clear()

@socketio.on(SOCKET_EVENT_STOP)
def handle_stop_connection(data):
    # save the list to a csv file
    print('Saving data to csv file...')
    print(my_sensor_data)
    save_to_csv('sensor_data.csv', my_sensor_data)
    # clear the list
    my_sensor_data.clear()
    print('Client stopped!')

@socketio.on(SOCKET_EVENT_SENSOR_DATA)
def handle_sensor_data(data):
    print('Client sent sensor data:', data)
    # convert the data to a dictionary
    data = loads(data)
    # append the data to the list
    my_sensor_data.append(data)
    
    emit(SOCKET_EVENT_SENSOR_DATA, data, broadcast=False)


@app.route('/')
def index():
    return 'Hello World!'

if __name__ == '__main__':
    socketio.run(app, debug=True)