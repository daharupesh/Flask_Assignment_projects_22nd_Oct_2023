from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import time

app = Flask(__name__)
app.config['SECRET_KEY'] = '8d2a6c84b6d7e8f5a3e9d0c1b2e5a4f3'  # Replace with a secure key in production
socketio = SocketIO(app, cors_allowed_origins="*")

@app.route('/')
def index():
    return render_template('index.html')

def background_task():
    while True:
        time.sleep(5)  # Simulate a delay for data update
        socketio.emit('update', {'data': 'This is real-time data update!'})

@socketio.on('connect')
def handle_connect():
    print('Client connected')
    socketio.start_background_task(target=background_task)

@socketio.on('disconnect')
def handle_disconnect():
    print('Client disconnected')

if __name__ == '__main__':
    socketio.run(app, debug=True)
