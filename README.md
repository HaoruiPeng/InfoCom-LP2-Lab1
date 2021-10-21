# LP2 Drone Project - Lab 1
In `/webserver`, run the flask server:
```
export FLASK_APP=build.py
export FLASK_ENV=development
flask run
```
In `/pi`, run the Pi controller:
```
python3 pi_controller.py
```
Don't user `python3 build.py` to run the webserver, since this does not porvide all the functionalities requied by the application.
