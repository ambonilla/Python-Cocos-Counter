#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" 
@_ambonilla 2014

Using cocos & piglet libraries, is a small counter program 
where when you push the up key it will add a number to the 
displayed value, and the down key will substract one 

"""

import cocos
import sys
from cocos.actions import *
import pyglet
from pyglet.window import key

class TempBackground(cocos.layer.Layer):

    is_event_handler = True

    def on_key_press(self, symbol, modifiers):
        if symbol == key.UP:
            self.counter = self.counter + 1
        elif symbol == key.DOWN:
            self.counter = self.counter - 1
        elif symbol == key.ESCAPE:
            SystemExit()
            
        self.update_text()
        
    def update_text(self):
        self.label.element.text = str(self.counter)
    
    def __init__(self):
        self.startBackground = super(TempBackground, self).__init__()
        self.counter = 0
        self.label = cocos.text.Label(str(self.counter),
                                 font_name='Arial',
                                 font_size=150,
                                 anchor_x='center',
                                 anchor_y='center')
        self.label.position = 320,240
        self.update_text()
        self.add(self.label)

if __name__ == "__main__":
    cocos.director.director.init(resizable=False, fullscreen=False)
    temp_layer = TempBackground()
    main_scene = cocos.scene.Scene(temp_layer)
    cocos.director.director.run(main_scene)
