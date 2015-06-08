#!/usr/bin/env python
from scene import Scene
class Starting(Scene):
    def run(self):
        text = '''
        You have survived a mass bombinb raid because you chose to go hunting.
        You have no water or food and have seen no game in days. All you have
        is your hunting knife and your trusty old 30-30 rifle with 30 rounds.
        You come across a lone abandoned farm house in the woods.
        It has a detached garage and a front and back door. It looks recently
        abandoned. With little daylight left you could use some supplies and
        a potentially safe nights rest. What do you check out first?
        1) The Garage
        2) The Front Door
        3) The Back Door
        '''

        print text

        user_choice = self.validate_choices(3)

        if user_choice == 1:
            return 'garage'
        elif user_choice == 2:
            return 'front_door'
        elif user_choice == 3:
            return 'back_door'
        else:
            print "Logic Validation Error, sorry for the inconvieneince"
            return 'Starting'
