from bot.handlers.now_handler import NowHandler
from bot.handlers.free_handler import FreeHandler
from bot.handlers.room_handler import RoomHandler
from bot.handlers.utility import retrieve_rooms
from flask import Flask, request, abort
from bot.handlers.parsing import *

startUpdater()
app = Flask(__name__)

@app.route('/now', methods=['POST'])
def now():
    token = request.form.get('token', None)  # TODO: validate the token
    command = request.form.get('command', None)
    text = request.form.get('text', None)

    if not token:  # or some other failure condition
        abort(400)

    handler = NowHandler()
    return handler.handleMessage()

@app.route('/free', methods=['POST'])
def free():
    token = request.form.get('token', None)  # TODO: validate the token
    command = request.form.get('command', None)
    text = request.form.get('text', None)

    if not token:  # or some other failure condition
        abort(400)

    handler = FreeHandler()
    return handler.handleMessage()

@app.route('/booking', methods=['POST'])
def booking():
    ScheduleUpdater.lookupFromServer()
    token = request.form.get('token', None)  # TODO: validate the token
    command = request.form.get('command', None)
    text = request.form.get('text', None)

    if not token:  # or some other failure condition
        abort(400)

    roomId = ''
    messageRoom = text.split()[0]
    for r in retrieve_rooms():
        if r.upper() == messageRoom.upper():
            roomId = r
    handler = RoomHandler(roomId)
    ScheduleUpdater.lookupFromServer()
    return str(ScheduleAccess().getScheduleForRoom(roomId)) + '\n' + text + handler.handleMessage()

@app.route('/')
def hello_world():
    return 'Hello from Flask!'
