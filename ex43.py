#!usr/bin/env python

from sys import exit
from random import randint

class Scene(object):
    def enter(self):
        print "This scene is not configured yet. Subclass it and implement enter()."
        exit(1)

class Engine(object):
    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        while True:
            print"\n-----"
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

class Death(Scene):

    quips = [
            "You died. You kinda suck at this.",
            "Your mom would be proud... if she were smarter.",
            "Such a luser.",
            "I have a small puppy that's better at this."
    ]
    def enter(self):

        print Death.quips[randint(0, len(self.quips)-1)]
        exit(1)

class CentralCorridor(Scene):

    def enter(self):

        scene = '''The gothons of Planet Percal #25 have invaded your ship and destroyed
        \nyour entire crew. You are the last surviving member and your last
        \nmission is to get the neutron destruct bomb from the Weapons Armor,
        \nput it in the bridge, and blow the ship up after getting into an
        \nescpe pod.
        \n
        You're running down the central corridor to the Weapons Armory when
        \na Gothon jumps out, red scaly skin, dark grimy teeth, and evil clown costume
        \nflowing around his hate filled body. He's blocking the door to the
        \nArmory and about to pull a weapon to blast you."
        '''
        print scene

        action = raw_input("> ")

        if action == "shoot!":
            shoot_text = '''Quick on the draw you yank out your blaster and fire it at the gotho."
            \nHis clown costume is flowing and moving around his body, which throws
            \n off your aim. Your laser hits his costume but misses him entirely. This
            \ncompletely ruins his brand new costume his mother bought him, which
            \nmakes him fly into a rage and blast you repeatedly in the face until
            \nyou are dead. Then eats you."
            '''
            print shoot_text
            return 'death'

        elif action == "dodge!":
            dodge_text = '''Like a world class boxer you dodge, weave, slip and slide right.
            \nas the Gothon's blaster cranks a laser past your head.
            \nn the middle of your artful dodge your foot slips and you
            \nbang your head on the metal wall and pass out.
            \nYou wake up shortly after only to die as the Gothon stomps on
            \nyour head and eats you.
            '''
            print dodge_text
            return 'death'

        elif action == "tell a joke":
            joke_text = '''Lucky for you they made you learn Gothon insults in the academy.
            \nYou tell the one Gothon joke you know:
            \nLbhe zbgure vf fb sng, jura fur fvgf nebhaq gur ubhfr, fur fvgf nebhaq gur ubhfr.
            \nThe Gothon stops, tries not to laugh, then busts out laughing and can't move.
            \nWhile he's laughing you run up and shoot him square in the head
            \nputting him down, then jump through the Weapon Armory door.
            '''
            print joke_text
            return 'laser_weapon_armory'
        else:
            print "DOES NOT COMPUTE!"
            return 'central_corridor'

class LaserWeaponArmory(Scene):

    def enter(self):
        lwa_enter_text = '''You do a dive roll into the Weapon Armory, crouch and scan the room
        \nfor more Gothons that might be hiding. It's dead quiet, too quiet.
        \nYou stand up and run to the far side of the room and find the
        \nneutron bomb in its container. There's a keypad lock on the box
        \nand you need the code to get the bomb out. If you get the code
        \nwrong 10 tims then the lock closes forever and you can't
        \nget the bomb. The code is 3 digits.
        '''
        print lwa_enter_text
        code = "%d%d%d" % (randint(1,9), randint(1,9), randint(1,9))
        guess = raw_input("[keypad]> ")
        guesses = 0
        print code
        print guess
        
        while guess != code and guess != '1337' and guesses < 10:
            print "BZZZZEDD!"
            guesses += 1
            guess = raw_input("[keypad]> ")

        if guess == code or guess == '1337':
            true_code = '''The container clicks open and the seal breaks, letting gas out.
            \nYou grab the neutron bomb and run as fast as you can to the
            \nbridge where you must place it in the right spot.
            '''
            print true_code
            return 'the_bridge'
        else:
            fail_code = '''The lock buzzes one last time and then you hear a sickening
            \nmelting sound as the mechanism is fused together.
            \nYou decide to sit there, and finally the Gothons blow up the
            \nship from their ship and you die.
            '''
            print fail_code
            return 'death'
            

class TheBridge(Scene):
    def enter(self):
        bridge_text = '''You burst onto the Bridge with the neutron destruct bom
        \nunder your arm and surprise 5 Gothons who are trying to
        \ntake control of the ship. Each of them has an even uglier
        \nclown costume than the last. They haven't pulled their
        \nweapons out yet, as they see the active bomb under your
        \narm and don't want to set it off.
        '''
        print bridge_text
        action = raw_input("> ")
        if action == "throw the bomb":
            throw_bomb_text =  '''In a panic you throw the bomb at the group of Gothons
            \nand make a leap for the door. right as you drop it a
            \nGothon shoots you right in the back killing you.
            \nAs you die you see another Gothon frantically try to disarm
            \nthe bom. You die knowing they will probably blow up when
            \nit goes off.
            '''
            print throw_bomb_text
            return 'death'
        elif action == 'slowly place the bomb':
            place_bomb_text = '''You point your blaster at the bomb under your arm
            \nand the Gothons put their hands up and start to sweat.
            \nYou inch backward to the door, open it, and then carefully
            \nplace the bomb on the floor, pointing your blaster at it.
            \nYou then jump back through the door, punch the close button
            \nand blast the lock so the Gothons can't get out.
            \nNow that the bomb is placed you run to the escape pod to
            \nget off this tin can.
            '''
            print place_bomb_text
            return 'escape_pod'
        else:
            print "DOES NOT COMPUTE"
            return 'the_bridge'

class EscapePod(Scene):

    def enter (self):
        escape_pod_text = '''You rush through the ship desperately trying to make it to
        \nthe escape pod before the whole ship explodes. It seems like
        \nhardly any Gothons are on the ship, so your run is clear of
        \ninterference. You get to the chamber with the escape pods, and
        \nnow need to pick one to take. Some of them could be damaged
        \nbut you don't hae time to look. There's 5 pods, which one
        \ndo you take?
        '''
        print escape_pod_text

        good_pod = randint(1,5)
        guess = raw_input("[pod#]> ")
        if int(guess) != good_pod:
            death_pod_text = '''You jump into pod %s and hit the eject button.
            \nThe pod escapes out into the void of space, then
            \nimplodes as the hull ruptures, crushing your body
            \ninto jam jelly
            ''' % guess
            print death_pod_text
            return 'death'
        else:
            life_pod_text = '''You jump into pod %s and hit the eject button.
            \nThe pod easily slides out into space heading to
            \nthe planet below. As it flies to the planet, you look
            \nback and see your ship implode then explode like a
            \nbright star, taking out the Gothon ship at the same
            \ntime. You won!
            ''' % guess
            print life_pod_text
            return 'finished'


class Map(object):
    scenes = {
            'central_corridor': CentralCorridor(),
            'laser_weapon_armory': LaserWeaponArmory(),
            'the_bridge': TheBridge(),
            'escape_pod': EscapePod(),
            'death': Death()
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self,scene_name):
        return Map.scenes.get(scene_name)

    def opening_scene(self):
        return self.next_scene(self.start_scene)

a_map = Map('central_corridor')
print a_map
a_game = Engine(a_map)
a_game.play()
