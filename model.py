__author__ = 'Vit'
# -*- coding: utf-8 -*-

import math

class Point3D():
    def __init__(self,x=0.0,y=0.0,z=0.0):
        self.x=x
        self.y=y
        self.z=z

    def distance(self,other):
        return math.sqrt((self.x-other.x)**2+(self.y-other.y)**2+(self.z-other.z)**2)

class Light():
    def __init__(self,point=Point3D(),I=0.0):
        self.point=point
        self.I=I

    def set_point(self,point=Point3D()):
        self.point=point

    def set_luminous_intensity(self,I):
        self.I=I

class Room():
    def __init__(self):
        self.lights=list()

    def add_light(self,light):
        self.lights.append(light)

    def EvXY(self,point=Point3D()):
        Ev=0.0
        for light in self.lights:
            r=point.distance(light.point)
            Ev+=(light.I/r**2)*(math.fabs(light.point.z-point.z)/r)
        return Ev

if __name__ == "__main__":
    print('Расчет освещенности')
    room=Room()
    light=Light(Point3D(0.0,0.0,2.85),290.0)
    room.add_light(light)
    light=Light(Point3D(3.0,3.0,2.85),290.0)
    # light.set_point(Point3D(1.5,1.5,2.85))
    # light.set_luminous_intensity(290.0)
    room.add_light(light)

    for y in range(4):
        for x in range(4):
            print(math.floor(room.EvXY(Point3D(x*1.0,y*1.0,0.8))),end=' ')
        print('')

