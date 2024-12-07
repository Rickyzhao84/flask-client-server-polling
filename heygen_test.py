import threading
import time
from heygen_client import VideoTranslationClient
from heygen_server import app

def run_server():
    app.run(port=5000, debug=False, use_reloader=False)

def test_integration():
    server_thread = threading.Thread(target=run_server)
    server_thread.start()
    time.sleep(2)

    client = VideoTranslationClient(server_url="http://127.0.0.1:5000")
    
    try:
        print("Starting client...")
        status = client.get_status()
        print(f"Final Status: {status}")
    except Exception as e:
        print(f"Failed: {e}")
    finally:
        
        print("Finished")

test_integration()
