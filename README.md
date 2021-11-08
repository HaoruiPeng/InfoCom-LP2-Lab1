# LP2 Drone Project - Lab 1
Intall the requied Python packages
```
pip3 install -r requirements.txt
```
Go to `/webserver`, run the flask server:
```
export FLASK_APP=build.py
export FLASK_ENV=development
flask run
```
Go to `/pi`, run the Pi controller:
```
python3 pi_controller.py
```
In the terminal running `pi_controller.py`, use arrow keys or 'wasd' to move the 'drone' on the website. 

Note: Don't user `python3 build.py` to run the webserver, since this does not porvide all the functionalities requied by the application.

