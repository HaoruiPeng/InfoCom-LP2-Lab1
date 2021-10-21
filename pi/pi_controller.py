import requests
import time
import random
import click

SERVER_URL = "http://127.0.0.1:5000/drone"
x = 0
y = 0
send_vel = False

while True:
    c = click.getchar()
    if c == '\x1b[D' or c =='a':
        click.echo('Left')
        send_vel = True
        x = -1
        y = 0
    elif c == '\x1b[C' or c == 'd':
        click.echo('Right')
        send_vel = True
        x = 1
        y = 0
    elif c == '\x1b[A' or c =='w':
        click.echo('Up')
        send_vel = True
        x = 0
        y = 1
    elif c == '\x1b[B' or c == 's':
        click.echo('Down')
        send_vel = True
        x = 0
        y = -1
    else:
        click.echo('Invalid input :(')
        send_vel = False
    if send_vel:
        with requests.Session() as session:
            current_location = {'x': x,
                                'y': y
                                }
            resp = session.post(SERVER_URL, json=current_location)
