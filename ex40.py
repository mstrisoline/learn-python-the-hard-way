#!/usr/bin/env python

class Song(object):
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print line

happy_bday = Song(["Happy birthday to you",
                    "I don't want to get sued",
                    "So I'll stop right there"])

bulls_on_parade = Song(["They rally around the family",
                        "With pockets full of shells"])

happy_bday.sing_me_a_song()
bulls_on_parade.sing_me_a_song()

my_song = ["foo", "bar", "baz"]
x = Song(my_song)
x.sing_me_a_song()

Song(my_song).sing_me_a_song()

print Song(my_song)
