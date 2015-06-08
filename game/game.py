#!/usr/bin/env python
from map import Map

class Game(object):
    def __init__(self,scene):
        self.scene = scene

    def play(self):
        current = self.scene.opening()
        while True:
            next = current.run()
            current = self.scene.next(next)

starting_game_map = Map('starting')
game = Game(starting_game_map)
game.play()
