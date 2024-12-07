import requests
import time

class VideoTranslationClient:
    def __init__(self, server_url, max_retry = 5, initial_delay = 1, max_delay = 16):
        # Configurable Parameters: Users can adjust max_retry, initial_delay, and max_delay to suit customer needs
        self.server_url = server_url
        self.max_retry = max_retry
        self.initial_delay = initial_delay
        self.max_delay = max_delay

    def get_status(self):
        """
        Polls the server for the status of a task.
        Uses retries in case of errors or pending status.
        """
        delay = self.initial_delay
        retry = 0

        while retry < self.max_retry:
            try:
                response = requests.get(f"{self.server_url}/status")
                result = response.json().get("result")
                print(f"Status: {result}")

                if result in ["completed", "error"]:
                    return result

                time.sleep(delay)
                # Gradually increase wait time to reduce server load
                delay = min(delay * 2, self.max_delay)
            except Exception as e:
                print(f"Retry {retry + 1}: Failed to fetch status. Waiting {delay}s before retrying...")
                time.sleep(delay)
                retry += 1

        # Made up max retrys to prevent server breakdown and throw exceptions
        raise Exception("Max retrys reached")

client = VideoTranslationClient("http://127.0.0.1:5000")
try:
    status = client.get_status()
    print(f"Final Status: {status}")
except Exception as e:
    print(f"Failed to get status: {e}")
