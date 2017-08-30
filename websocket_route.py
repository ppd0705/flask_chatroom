from flask import session
from flask_socketio import (
    emit,
    join_room,
    leave_room,
    SocketIO,
)

# 创建websocket对象
socketio = SocketIO()


@socketio.on('connect', namespace='/chat')
def test_connect():
    print('Client connected')


@socketio.on('disconnect', namespace='/chat')
def test_disconnect():
    print('Client disconnected')


@socketio.on('join', namespace='/chat')
def on_join(data):
    username = session.get('name')
    room = data
    join_room(room)
    session['room'] = room
    data = username + ' has entered the room.'
    emit('status', data, room=room)


@socketio.on('leave', namespace='/chat')
def on_leave(data):
    username = session.get('name')
    room = session.get('room')
    leave_room(room)
    data = username + ' has lefted the room.'
    emit('status', data, room=room)


@socketio.on('send', namespace='/chat')
def on_send(data):
    username = session.get('name')
    room = session.get('room')
    message = '{}: {}'.format(username, data)
    emit('message', message, room=room)
