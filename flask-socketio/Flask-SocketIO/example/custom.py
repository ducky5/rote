from threading import Lock
from flask import Flask, render_template, session
from flask_socketio import SocketIO, emit

async_mode = None

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, async_mode=async_mode)
thread = None
thread_lock = Lock()

# def background_thread():
#     """Example of how to send server generated events to clients."""
#     count = 0
#     while True:
#         socketio.sleep(10)
#         count += 1
#         socketio.emit('my_response',
#                       {'data': 'Server generated event', 'count': count})

@app.route('/')
def index():
    return render_template('custom.html')

# @socketio.event
# def connect():
#     global thread
#     with thread_lock:
#         if thread is None:
#             thread = socketio.start_background_task(background_thread)
#     emit('my_response', {'data': 'Connected', 'count': 0})

# emits from server to client
@socketio.event
def my_event(message):
    # increment receive count by 1
    session['receive_count'] = session.get('receive_count', 0) + 1
    # emits back to client
    emit('my_response',
         {'data': message['data'], 'count': session['receive_count']})

if __name__ == '__main__':
    socketio.run(app, debug=True)
