"""
Sketch will show stars on the canvas at an estimated convergence time.
Turn mousewheel up/down to increase/decrease the time.
Press left and right arrows to advance time in greater intervals.
"""

import re
from collections import namedtuple
from input_string import input_string

Star = namedtuple("Star", "x y dx dy")


def star_position_at(star, seconds):
    x = star.x + star.dx * seconds
    y = star.y + star.dy * seconds
    return x, y


def get_arrival_times(stars):
    return [-x/dx for x, y, dx, dy in stars]


def parse_dot(raw_string):
    global arrival_times
    x, y = [int(n) for n in re.search(r'position=<(.*?)>', raw_string).group(1).split(',')]
    dx, dy = [int(n) for n in re.search(r'velocity=<(.*?)>', raw_string).group(1).split(',')]

    return Star(x, y, dx, dy)


lines = input_string.split('\n')
stars = [parse_dot(line) for line in lines]
arrival_times = get_arrival_times(stars)
eta = int(sum(arrival_times)/len(arrival_times))
time = eta

def setup():
    size(1000, 1000)
    noLoop()


def draw():
    background(0)
    translate(width/2, height/2)
    scale(1)
    fill(255)
    textSize(40)
    text("Time: " + str(time), 0, -height/3)
    
    noSmooth()
    stroke(255)
    for star in stars:
        x, y = star_position_at(star, time)
        point(x, y)


def keyPressed(e):
    global time
    if key == CODED:
        if keyCode == RIGHT:
            time += 50
        elif keyCode == LEFT:
            time -= 50
    redraw()


def mouseWheel(e):
    global time
    time += -e.getCount()
    redraw()
