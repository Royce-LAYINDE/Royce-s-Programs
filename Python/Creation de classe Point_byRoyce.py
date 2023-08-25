# -*- coding: utf-8 -*-
"""
Created on Fri Jun 23 15:29:59 2023

@author: Royce
"""
class Point3d:
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
    def deplace(self,dx,dy,dz):
        self.x += dx
        self.y += dy
        self.z += dz
a3D=Point3d(1, 0, 0)
b3D=Point3d(0, 1, 0)
c3D=Point3d(0, 0, 1)
a3D.deplace(0, 0, 1)
b3D.deplace(0, 1, 1)
c3D.deplace(1, 1, 1)
print(f"les coordonnes de a3D sont: x={a3D.x} y={a3D.y} z={a3D.z}" )
print(f"les coordonnes de b3D sont: x={b3D.x} y={b3D.y} z={b3D.z}" )
print(f"les coordonnes de c3D sont: x={c3D.x} y={c3D.y} z={c3D.z}" )
#Avec @
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, x):
        self._x = x

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, y):
        self._y = y

a = Point(3, 7)
print("a : abscisse =", a.x)
print("a : ordonnee =", a.y)
a.x = 6
a.y = 10
print("a : abscisse =", a.x)
print("a : ordonnee =", a.y)