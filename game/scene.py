#!/usr/bin/env python

from sys import exit

class Scene(object):

    def run(self):
        print "Implement this scene"
        exit(1)

    def validate_choices(self, choices):
        user_input = input('# ')
        while not False:
            if type(user_input) is int:
                if user_input <= choices and user_input != 0:
                    return user_input
                else:
                    print "Please input a number equal to the choice you want to make"
                    user_input = input('# ')
            else:
                print "Please input a number equal to the choice you want to make"
                user_input = input('# ')
