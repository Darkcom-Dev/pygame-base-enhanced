#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  scene_sound_test.py
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

class SceneSoundTest(scene.Scene):
	def __init__(self,director):

		self.event_text = presets.event_text
		self.event_text.text = ("Hola desde Scene Sound Test")

		self. info_text = presets.info_text
		self. subevent_text = presets.subevent_text
		pygame.mixer.music.load(cfg.AudioDir + cfg.AudioTest)
		pygame.mixer.music.play()

		self.dir = director

	def on_update(self):
		ticks = pygame.mixer.music.get_pos()
		self.info_text.text = f' {ticks} ticks, {(ticks//60000)%60} minutos, {(ticks//1000)%60} segundos'
		self.subevent_text.text = f'{pygame.mixer.music.get_volume() * 100}'

	def on_event(self):
		#if super().J1:
		if self.dir.button == 'Y':
			pygame.mixer.music.pause()
		elif self.dir.button == 'B':
			pygame.mixer.music.unpause()
		elif self.dir.button == 'A':
			pygame.mixer.music.rewind()
			pygame.mixer.music.play()

		if self.dir.horizontal == -1:
			'''super().J1.get_hat(0)[1] == -1 or '''
			
			pygame.mixer.music.set_volume(round(pygame.mixer.music.get_volume() - 0.01,3))
		elif self.dir.horizontal == 1:
			'''super().J1.get_hat(0)[1] == 1 or '''
			
			pygame.mixer.music.set_volume(round(pygame.mixer.music.get_volume() + 0.01,3))

	def on_draw(self, screen):
		screen.fill(cfg.ScreenFillColor)
		self.event_text.position = (math.sin(pygame.time.get_ticks()/1000) * cfg.WIDTH/4 + cfg.WIDTH/2, random.randrange((cfg.HEIGHT/2) -2,(cfg.HEIGHT/2) +2))
		self.event_text.draw(screen,'chromatic',2)
		
		self.info_text.draw(screen,'caption',0)
		self.subevent_text.draw(screen,'caption',0)
		pygame.display.flip()


def main(args):
	return 0

if __name__ == '__main__':
	import sys
	sys.exit(main(sys.argv))
