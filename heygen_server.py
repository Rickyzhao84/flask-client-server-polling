from flask import Flask, jsonify, request
import random
import time
import logging

logging.basicConfig(level=logging.INFO)

app = Flask(__name__)
start_time = time.time()
delay = 10

@app.route('/status', methods=['GET'])
def get_status():
    """
    Endpoint to get the status of a task.
    Simulates a delay and possible random errors.
    """
    elapsed_time = time.time() - start_time
    logging.info(f"Total elapsed time: {elapsed_time:.2f} seconds")

    # Check if the task is still in progress based on the elapsed time
    if elapsed_time < delay:
        logging.info("Status: pending")
        return jsonify({"result": "pending"})
    else:
        curr_random = random.random()
        logging.info(f"Random number for error simulation: {curr_random:.2f}")
        
        if curr_random > 0.8:
            logging.error("Status: error")
            return jsonify({"result": "error"}), 500
        
        logging.info("Status: completed")
        return jsonify({"result": "completed"})

app.run(debug=True)
