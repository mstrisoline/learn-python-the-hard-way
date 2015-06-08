#!/usr/bin/env python
from scene import Scene
from starting import Starting
from front_door import FrontDoor
from back_door import BackDoor
from kitchen import Kitchen
from first_floor import FirstFloor
from upstairs import Upstairs
from garage import Garage
class Map(object):

    scenes = {
       'starting' : Starting(),
       'front_door': FrontDoor(),
       'back_door': BackDoor(),
       'kitchen': Kitchen(),
       'first_floor': FirstFloor(),
       'upstairs': Upstairs(),
       'garage': Garage()
    }

    def __init__(self, start):
        self.start = start

    def next(self, next):
        return Map.scenes.get(next)

    def opening(self):
        return self.next(self.start)
