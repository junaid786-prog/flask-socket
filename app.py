from flask import Flask, request
from os import environ
from flask_socketio import SocketIO, send, emit
from json import loads

from socket_events import *
from csv_util import *


app = Flask(__name__)
socketio = SocketIO(app)


# start storing individual sensor data in a list on start event and on stop event, save the list to a csv file and clear the list also send the stats to the client
# on sensor data event, append the data to the list

clients_sensor_data = {}
CSV_FILE_DIRECTORY = 'client_data/'

@socketio.on(SOCKET_EVENT_CONNECT)
def handle_connect():
    print(f'Client connected! {request.sid}')
    clients_sensor_data[request.sid] = []

@socketio.on(SOCKET_EVENT_DISCONNECT)
def handle_disconnect():
    print('Client disconnected!')
    clients_sensor_data.pop(request.sid, None)

@socketio.on(SOCKET_EVENT_START)
def handle_start_connection(data):
    print('Client started!')
    clients_sensor_data[request.sid].clear()

@socketio.on(SOCKET_EVENT_STOP)
def handle_stop_connection(data):
    # save the list to a csv file
    print(f'Saving data to csv file... {request.sid}')
    my_sensor_data = clients_sensor_data[request.sid]
    print(my_sensor_data)
    file_path = f'{CSV_FILE_DIRECTORY}{request.sid}_sensor_data.csv'
    save_to_csv(file_path, my_sensor_data)
    # clear the list
    clients_sensor_data[request.sid].clear()
    print('Client stopped!')

@socketio.on(SOCKET_EVENT_SENSOR_DATA)
def handle_sensor_data(data):
    print('Client sent sensor data:', data)
    # convert the data to a dictionary
    data = loads(data)
    # append the data to the list
    clients_sensor_data[request.sid].append(data)
    
    emit(SOCKET_EVENT_SENSOR_DATA, data, broadcast=False)


@app.route('/')
def index():
    return f'Hello World! {environ.get("PORT")} {environ.get("VAR")}'

if __name__ == '__main__':
    socketio.run(app, debug=True)