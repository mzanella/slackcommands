from bot.handlers.now_handler import NowHandler
from flask import Flask, request, abort
import os

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

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)