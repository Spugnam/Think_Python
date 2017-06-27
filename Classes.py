#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 27 15:02:44 2017

@author: Quentin
"""

from __future__ import print_function, division


class Point:
    """Represents a point in 2-D space.

    attributes: x, y
    """


def print_point(p):
    """Print a Point object in human-readable format."""
    print('(%g, %g)' % (p.x, p.y))


class Rectangle:
    """Represents a rectangle. 

    attributes: width, height, corner.
    """


def find_center(rect):
    """Returns a Point at the center of a Rectangle.

    rect: Rectangle

    returns: new Point
    """
    p = Point()
    p.x = rect.corner.x + rect.width/2.0
    p.y = rect.corner.y + rect.height/2.0
    return p


def grow_rectangle(rect, dwidth, dheight):
    """Modifies the Rectangle by adding to its width and height.

    rect: Rectangle object.
    dwidth: change in width (can be negative).
    dheight: change in height (can be negative).
    """
    rect.width += dwidth
    rect.height += dheight
    
box = Rectangle()
print(isinstance(box, Rectangle))
box.width = 100.0
box.height = 200.0
box.corner = Point()
box.corner.x = 0.0
box.corner.y = 0.0

def main():
    blank = Point()
    blank.x = 3
    blank.y = 4
    print('blank', end=' ')
    print_point(blank)

    box = Rectangle()
    print(isinstance(box, Rectangle))
    box.width = 100.0
    box.height = 200.0
    box.corner = Point()
    box.corner.x = 0.0
    box.corner.y = 0.0

    center = find_center(box)
    print('center', end=' ')
    print_point(center)

    print(box.width)
    print(box.height)
    print('grow')
    grow_rectangle(box, 50, 100)
    print(box.width)
    print(box.height)


if __name__ == '__main__':
    main()
#%%
def move_rectangle(rectangle, dx, dy):
    rectangle.corner.x += dx
    rectangle.corner.y += dy
    print(rectangle.corner.x, rectangle.corner.y)

move_rectangle(box, 10, 20) 

print(isinstance(box, Rectangle))

print(__name__)
#%%
import math

class Circle:
    '''Class Circle has a circle and a radius
    '''
    Center = Point()
    radius = int()
    
centre = Point()
centre.x = 150
centre.y= 100
    
cercle = Circle()
cercle.Center = centre
cercle.radius = 75
#%%
def point_in_circle(punto, cerchio):
    return math.sqrt(math.pow(punto.x-cerchio.Center.x, 2)+math.pow(punto.y-cerchio.Center.y,2)) <= cerchio.radius

punto = Point()
punto.x = 150
punto.y = 176

point_in_circle(punto, cercle)
#%%
import copy

def rect_in_circle(rettangolo, cerchio):
    print("rectangle:")
    print(rettangolo.corner.x, rettangolo.corner.y)
    print("cercle:")
    print(cerchio.Center.x, cerchio.Center.y)
    punto2 = copy.deepcopy(rettangolo.corner)
    punto2.x += rettangolo.width
    print(punto2.x, punto2.y)
    punto3 = copy.deepcopy(rettangolo.corner)
    punto3.y += rettangolo.height
    print(punto3.x, punto3.y)
    punto4 = copy.deepcopy(rettangolo.corner)
    punto4.x += rettangolo.width
    punto4.y += rettangolo.height
    print(punto4.x, punto4.y)
    
    return point_in_circle(rettangolo.corner, cerchio) and point_in_circle(punto2, cerchio)  and point_in_circle(punto3, cerchio) and point_in_circle(punto4, cerchio)

box2 = Rectangle()
box2.width = 3.0
box2.height = 2.0
box2.corner = Point()
box2.corner.x = 150.0
box2.corner.y = 100.0

print("rectangle in cicle:")
print(rect_in_circle(box2, cercle))

punto2 = copy.deepcopy(box2.corner)
punto2.x += box2.width
print(punto2.x, punto2.y)

punto3 = copy.deepcopy(box2.corner)
punto3.y += box2.height
print(punto3.x, punto3.y)

punto4 = copy.deepcopy(box2.corner)
punto4.x += box2.width
punto4.y += box2.height
print(punto4.x, punto4.y)

point_in_circle(punto4, cercle)

#%%
class Time:
    """Represents the time of day.
       
    attributes: hour, minute, second
    """


def print_time(t):
    """Prints a string representation of the time.

    t: Time object
    """
    print('%.2d:%.2d:%.2d' % (t.hour, t.minute, t.second))
#%%
time1 = Time()
time1.hour = 23
time1.minute = 59
time1.second = 30

print_time(time1)
#%%
def is_after(time1, time2):
    return (t1.hour, t1.minute, t1.second) > (t2.hour, t2.minute, t2.second)

#%%
def increment(t1, seconds):
    t1.hour = (t1.hour + (t1.minute + seconds // 60) // 60) % 24
    t1.minute = (t1.minute + seconds // 60) % 60
    t1.second += seconds % 60

increment(time1, 121)
#%%
print_time(time1)
#%%
def pure_increment(t1, seconds):
    t2 = Time()
    t2.hour = (t1.hour + (t1.minute + seconds // 60) // 60) % 24
    t2.minute = (t1.minute + seconds // 60) % 60
    t2.second = (t1.second + seconds) % 60
    return t2
#%%
t2 = pure_increment(time1, 10000)
print_time(t2)
#%%
import time
from datetime import date

def current_weekday():
    return date.today().weekday()

current_weekday()
#%%
from datetime import *
def days_until_birthday(birthday):
    """How long until my next birthday?"""
    today = datetime.today()
    # when is my birthday this year?
    next_birthday = datetime(today.year, birthday.month, birthday.day)

    # if it has gone by, when will it be next year
    if today > next_birthday:
        next_birthday = datetime(today.year+1, birthday.month, birthday.day)

    # subtraction on datetime objects returns a timedelta object
    delta = next_birthday - today
    return delta.days

days_until_birthday(datetime(1980, 04, 10))
#%%
def double_day(date1, date2):
    (d1, d2) = (min(date1, date2), max(date1, date2))
    delta = d2 - d1
    return d2+delta

print(double_day(date1, date2))


#%%
date1 = datetime(1980, 04, 10)
date2 = datetime(1982, 06, 30)
(d1, d2) = (min(date1, date2), max(date1, date2))
print((d1, d2))
print(d1.year, d1.month, d1.day)

vars(str)
