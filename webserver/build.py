from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit
from flask_cors import CORS
import time

app = Flask(__name__)
CORS(app, supports_credentials=True)
app.secret_key = 'dljsaklqk24e21cjn!Ew@@dsa5'
socket = SocketIO(app, cors_allowed_origins="*")

x_coord = 13.21008
y_coord = 55.71106

# Intialize MySQL
def translate(coords):
    x_origins_lim = (13.143390664, 13.257501336)
    y_origins_lim = (55.678138854000004, 55.734680845999996)

    x_translated_lim = (212.155699, 968.644301)
    y_translated_lim = (103.68, 768.96)

    x_origin = coords[0]
    y_origin = coords[1]

    x_ratio = (x_translated_lim[1] - x_translated_lim[0]) / (x_origins_lim[1] - x_origins_lim[0])
    y_ratio = (y_translated_lim[1] - y_translated_lim[0]) / (y_origins_lim[1] - y_origins_lim[0])
    x_translated = x_ratio * (x_origin - x_origins_lim[0]) + x_translated_lim[0]
    y_translated = y_ratio * (y_origins_lim[1] - y_origin) + y_translated_lim[0]

    return x_translated, y_translated

def moveDrone(movement):
    global x_coord
    global y_coord
    dx = movement['x']
    dy = movement['y']
    x_coord += dx/10000
    y_coord += dy/10000

@app.route('/drone', methods=['POST'])
def drone():
    movement = request.get_json()
    moveDrone(movement)
    return 'Get data'

@app.route('/', methods=['GET'])
def map():
    return render_template('index.html')

@socket.on('get_location')
def get_location():
    while True:
        x_translated, y_translated = translate((x_coord, y_coord))
        emit('get_location', (x_translated, y_translated))
        time.sleep(0.01)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port='5000')
