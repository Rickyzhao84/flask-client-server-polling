# Video Translation Server

This small project demonstrates a client-server interaction where the client runs the server for the status of a task. This README provides setup instructions, dependencies, and testing information.

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
2. Navigate to the directory containing the server code (`heygen_server.py`).
3. Start the server by running:
   ```bash
   python heygen_server.py

4. The server will start on http://127.0.0.1:5000 and listen for client requests.

### 2. Running the Client

1. Open another command-line terminal (keep the server terminal running).
2. Navigate to the directory containing the client code (heygen_client.py).
3. Run the client by executing:
   ```bash
   python heygen_client.py
4. The client will begin running the server and log the status updates.

## Testing Instructions

### Integration Test

1. Open a third command-line terminal (ensure the server is running).
2. Navigate to the directory containing the test code (heygen_test.py).
3. Run the test by executing:
   ```bash
   python heygen_test.py
4. The test will:
Start a new server instance in the background.
Use the client library to running the server.
Log the interaction and print the final status.

## Others

### Why Multiple Terminals?

One terminal is used for running the server, another for running the client, and a third for testing the integration.

### Bells and Whistles

1. Logging
2. Error handling
3. Delay increases each time until reaching max limit
4. User configurable parameters in client initialization

### Example Output
    ```bash 
    127.0.0.1 - - [07/Dec/2024 16:35:05] "GET /status HTTP/1.1" 200 -

### Example Client Output

   ```bash
   Starting client...
   Server status: pending
   Server status: pending
   Server status: completed
   Final Status: completed
   Finished


