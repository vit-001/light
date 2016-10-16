__author__ = 'Vit'
# -*- coding: utf-8 -*-

import math
from model import Point3D,Light,Room

def create_room():
    room=Room()
    return room

def define_lights(room):
    for i in range(5):
        y=i*1.0+0.5
        print(y)
        light=Light(Point3D(0.0,y,3.10),290.0)
        room.add_light(light)
        light=Light(Point3D(4.5,y,3.10),290.0)
        room.add_light(light)
    for i in range(4):
        x=i*1.0+0.5
        print(x)
        light=Light(Point3D(x,0,3.10),290.0)
        room.add_light(light)
        light=Light(Point3D(x,5,3.10),290.0)
        room.add_light(light)

    light=Light(Point3D(4.25,0,3.10),290.0/2)
    room.add_light(light)

    light=Light(Point3D(4.25,5,3.10),290.0/2)
    room.add_light(light)

if __name__ == "__main__":
    print('Расчет освещенности')
    room=create_room()
    define_lights(room)

    print('    ',end=' ')
    for x in range(12):
        print(x*0.5,end=' ')
    print('')
    for y in range(11):
        print(y*0.5,end='==')
        for x in range(10):
            print(math.floor(room.EvXY(Point3D(x*0.5,y*0.5,0.8))),end=' ')
        print('')

