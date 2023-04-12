#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  scene_physics.py
#  
#  Copyright 2021 Braulio Madrid <darkcom@darkcom-X455LD>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

import scene
import text_presets as presets
import config as cfg
import pygame
import math, random

'''
MVCL - movimiento vertical de caida libre
siempre hay una variable que se descarta en los problemas

Vf = Vo +/- g*t, descarta h
h = ((vo + vf)2) * t descarta g
h = Vo*t +- ((g*t**2)/2) descarta Vf
Vf ** 2 = Vo ** 2 +- 2*g*h descarta t

+ si el movil baja
- si el movil sube
'''


class ScenePhysicsTest(scene.Scene):
	def __init__(self,director):

		self.event_text = presets.event_text
		self.event_text.text = ("Hola desde Scene Physics Test")

		self. info_text = presets.info_text
		self. subevent_text = presets.subevent_text
		
		self.x_position = 320
		self.y_position = 2
		self.Vo = 0
		self.t = 210
		self.gravity = 9.8
		
		self.on_ground = False
		
		self.dir = director

	def on_update(self):
		self.ticks = pygame.time.get_ticks()
		
		self.info_text.text = f'ticks: {self.ticks}, gravedad: {self.y_position}, time: {self.t}'
		self.subevent_text.text = "Sub Event text"
		
		self.t += 1
		
		
		self.y_position += self.t
					
		if self.y_position < 448 - 32:
			self.on_ground = False
			
		else:
			self.y_position = 448 - 32
			self.on_ground = True
			

	def on_event(self):
		#if super().J1:
		if self.dir.button == 'Y' and self.on_ground:
			self.t = -30
		elif self.dir.button == 'B':
			pass
		elif self.dir.button == 'A':
			pass

		self.x_position += self.dir.horizontal

	def on_draw(self, screen):
		screen.fill(cfg.ScreenFillColor)
		self.event_text.position = (math.sin(pygame.time.get_ticks()/1000) * cfg.WIDTH/4 + cfg.WIDTH/2, random.randrange((cfg.HEIGHT/2) -2,(cfg.HEIGHT/2) +2))
		self.event_text.draw(screen,'chromatic',2)
		
		self.info_text.draw(screen,'caption',0)
		self.subevent_text.draw(screen,'caption',0)
		
		pygame.draw.rect(screen, (128,0,0),(self.x_position,self.y_position,16,32))
		
		pygame.draw.rect(screen, (32,128,96),(0,448,640,32))
		
		pygame.display.flip()


def main(args):
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
