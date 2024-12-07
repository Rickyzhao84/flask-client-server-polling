# Client-Server Polling Example

This small project demonstrates a client-server interaction where the client polls the server for the status of a task. This README provides setup instructions, dependencies, and testing information.

---

## Prerequisites

1. **Python Installation**:
   - Ensure Python is installed on your system.
   - Verify using:
     ```bash
     python --version
     ```
   - If not installed, download and install Python from [python.org](https://www.python.org/downloads/).

2. **Pip Installation**:
   - Ensure `pip` is installed. Verify using:
     ```bash
     pip --version
     ```
   - If `pip` is not installed, follow the [pip installation guide](https://pip.pypa.io/en/stable/installation/).

3. **Dependencies**:
   - Install Flask for the server to run:
     ```bash
     pip install flask
     ```

---

## Setup Instructions

### 1. Running the Server

1. Open a command-line terminal.
2. Navigate to the directory containing the server code (`server.py`).
3. Start the server by running:
   ```bash
   python server.py

4. The server will start on http://127.0.0.1:5000 and listen for client requests.

### 2. Running the Client

1. Open another command-line terminal (keep the server terminal running).
2. Navigate to the directory containing the client code (client.py).
3. Run the client by executing:
   ```bash
   python client.py
4. The client will begin polling the server and log the status updates.

## Testing Instructions

### Integration Test

1. Open a third command-line terminal (ensure the server is running).
2. Navigate to the directory containing the test code (test.py).
3. Run the test by executing:
   ```bash
   python test.py
4. The test will:
Start a new server instance in the background.
Use the client library to poll the server.
Log the interaction and print the final status.
