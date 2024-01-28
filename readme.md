# Flask Server

This repository contains a Flask server that performs the following steps:

## Steps

1. **Listen on PORT:** The server listens on a specified port for incoming connections.
2. **Establish Connection:** Once a connection is established, the server is ready to receive and process data.
3. **Make Related User Data Field into Dict:** The server organizes user data into a dictionary for efficient handling.
4. **Start Collecting User Data:** It begins collecting user data based on the established connection.
5. **On Event `stop`, Save All Data into User File:** When the server receives a stop event, it saves all collected data into a user file.

## Process

To run the Flask server, follow these steps:

1. Activate the virtual environment:

    ```bash
    source ./env/bin/activate
    ```

2. Install the required dependencies:

    ```bash
    pip3 install -r requirements.txt
    ```

3. Run the Flask server:

    ```bash
    python3 server.py
    ```

This will start the server, and it will be ready to receive and process data.
