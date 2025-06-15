# health_server.py
from flask import Flask
import threading

app = Flask(__name__)

@app.route('/')
def health():
    return "I'm healthy!", 200

def run():
    app.run(host="0.0.0.0", port=8080)

def start_health_server():
    thread = threading.Thread(target=run)
    thread.daemon = True
    thread.start()
