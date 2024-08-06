from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit, join_room, leave_room
import time
import threading

app = Flask(__name__)
app.config['SECRET_KEY'] = '2b3@5d!_w7qz6^V&fR#n8KjE2*4M9oL@3P7r8CzV0d1X5G6H'  # A strong, randomly generated secret key
socketio = SocketIO(app, cors_allowed_origins="*")

@app.route('/')
def index():
    return render_template('index.html')

def background_task(room):
    while True:
        time.sleep(10)  # Simulate a delay for data update
        socketio.emit('notification', {'message': f'Notification for room {room}'}, room=room)

@socketio.on('join')
def handle_join(data):
    username = data['username']
    room = f'room_{username}'
    join_room(room)
    print(f'{username} joined {room}')
    # Start background task only if it is not already running
    if not hasattr(handle_join, 'background_threads'):
        handle_join.background_threads = {}
    if room not in handle_join.background_threads:
        thread = threading.Thread(target=background_task, args=(room,))
        thread.daemon = True
        thread.start()
        handle_join.background_threads[room] = thread

@socketio.on('leave')
def handle_leave(data):
    username = data['username']
    room = f'room_{username}'
    leave_room(room)
    print(f'{username} left {room}')

@socketio.on('connect')
def handle_connect():
    print('Client connected')

@socketio.on('disconnect')
def handle_disconnect():
    print('Client disconnected')

if __name__ == '__main__':
    socketio.run(app, debug=True)
