from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit
from flask_cors import CORS
import time

app = Flask(__name__)
CORS(app, supports_credentials=True)
app.secret_key = 'dljsaklqk24e21cjn!Ew@@dsa5'
socket = SocketIO(app, cors_allowed_origins="*")

longitude = 13.21008
latitude = 55.71106

# Translate OSM coordinate (longitude, latitude) to SVG coordinates (x,y).
# Input coords_osm is a tuple (longitude, latitude).
def translate(coords_osm):
    x_osm_lim = (13.143390664, 13.257501336)
    y_osm_lim = (55.678138854000004, 55.734680845999996)

    x_svg_lim = (212.155699, 968.644301)
    y_svg_lim = (103.68, 768.96)

    x_osm = coords_osm[0]
    y_osm = coords_osm[1]

    x_ratio = (x_svg_lim[1] - x_svg_lim[0]) / (x_osm_lim[1] - x_osm_lim[0])
    y_ratio = (y_svg_lim[1] - y_svg_lim[0]) / (y_osm_lim[1] - y_osm_lim[0])
    x_svg = x_ratio * (x_osm - x_osm_lim[0]) + x_svg_lim[0]
    y_svg = y_ratio * (y_osm_lim[1] - y_osm) + y_svg_lim[0]

    return x_svg, y_svg

def moveDrone(movement):
    global longitude
    global latitude
    d_long = movement['longitude']
    d_la = movement['latitude']
    longitude += d_long/10000
    latitude += d_la/10000

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
        x_svg, y_svg = translate((longitude, latitude))
        emit('get_location', (x_svg, y_svg))
        time.sleep(0.01)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port='5000')
