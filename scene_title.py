#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Importante para mejorar un poco mas el joystick
# https://nerdparadise.com/programming/pygamejoystick

# Módulos
import scene
import config as cfg
import text_presets as preset
import font
import math
import pygame
import random

# Constantes


# Clases
# ---------------------------------------------------------------------

class SceneTitle(scene.Scene):
	"""Escena inicial del juego, esta es la primera que se carga cuando inicia"""

# ---------------------------------------------------------------------

# Funciones
# ---------------------------------------------------------------------
	# ~ print(f'obtencion de datos desde el padre: {scene.Scene.scene_value}')

	def __init__(self, director):

		# ~ print(f'obtencion de datos desde el padre: {super().scene_value}')
		
		self.dir = director
		
		self.event_text = preset.event_text
		self.event_text.text = "Hola desde scene_title"
		
		self.history_text = preset.history_text
		
		self.background = pygame.image.load(cfg.SpritesDir + cfg.ControllerBackground).convert()
		
		
		self.info_text_list = list()
		self.hat_list = list()
		
		if self.dir.J1:
			self.num_axes = self.dir.J1.get_numaxes()
			self.info_text_list = []
			for i in range(self.num_axes):
				self.info_text_list.append(font.Font(cfg.ParagraphFont, cfg.P2,f'info {i}',"tl",(10,10 + (20*i)),cfg.DefaultColor,cfg.InfoOutlineColor))
			
			self.num_hats = self.dir.J1.get_numhats()
			self.hat_list = []
			for i in range(self.num_hats):
				self.hat_list.append(font.Font(cfg.ParagraphFont, cfg.P2,f'info {i}',"tl",(100,10 + (20*i)),cfg.DefaultColor,cfg.InfoOutlineColor))
		

		self.activeColor = (255,0,0)
		self.normalColor = (128, 128, 128)
		
		self.colorA = self.normalColor
		self.colorB = self.normalColor
		self.colorX = self.normalColor
		self.colorY = self.normalColor
		self.colorL = self.normalColor
		self.colorR = self.normalColor
		self.colorUp = self.normalColor
		self.colorDown = self.normalColor
		self.colorLeft = self.normalColor
		self.colorRight = self.normalColor
		
		self.mouse = list()

	def on_update(self):
		self.mouse = pygame.mouse.get_pos()
		self.history_text.text = f'{str(self.mouse)}'
		
	def on_event(self):
		
		# Buttons
		self.colorLeft = self.activeColor if self.dir.horizontal == -1 else self.normalColor
		self.colorRight = self.activeColor if self.dir.horizontal == 1 else self.normalColor
		self.colorUp = self.activeColor if self.dir.vertical == 1 else self.normalColor
		self.colorDown = self.activeColor if self.dir.vertical == -1 else self.normalColor
		self.colorA = self.activeColor if self.dir.button == 'A' or self.dir.button == 'AB' else self.normalColor
		self.colorB = self.activeColor if self.dir.button == 'B' or self.dir.button == 'AB' else self.normalColor
		self.colorX = self.activeColor if self.dir.button == 'X' or self.dir.button == 'XY' else self.normalColor
		self.colorY = self.activeColor if self.dir.button == 'Y' or self.dir.button == 'XY' else self.normalColor
		self.colorL = self.activeColor if self.dir.button == 'L' or self.dir.button == 'LR' else self.normalColor
		self.colorR = self.activeColor if self.dir.button == 'R' or self.dir.button == 'LR' else self.normalColor

		if self.dir.horizontal == -1:self.event_text.text = "Key_left"		
		if self.dir.horizontal == 1:self.event_text.text = "Key_right"
		if self.dir.vertical == 1:self.event_text.text = "Key_up"
		if self.dir.vertical == -1:	self.event_text.text = "Key_down"

		self.tag_buttons()
		
		
		if self.dir.J1:
			for i in range(self.dir.J1.get_numbuttons()):
				if self.dir.J1.get_button(i):
					self.event_text.text = f'Joy button {i}'
			
			for i in range(self.num_hats):
				self.hat_list[i].text = f'hat {i}: {self.dir.J1.get_hat(i)}'
			
			for i in range(self.num_axes):
				self.info_text_list[i].text = f'Axis {i}: {round(self.dir.J1.get_axis(i),2)}'
		
	def on_draw(self, screen):
		screen.blit(self.background, (0,0))
		self.event_text.draw(screen)
		self.event_text.position = (math.sin(pygame.time.get_ticks()/1000) * cfg.WIDTH/4 + cfg.WIDTH/2, random.randrange((cfg.HEIGHT/2) -2,(cfg.HEIGHT/2) +2))
		self.event_text.draw(screen, "chromatic",2)
		
		self.draw_circle_buttons(screen)
		
		self.draw_rectangle_buttons(screen)
		
		self.history_text.draw(screen)
		
		for info in self.info_text_list:
			info.draw(screen)
			
		for hat in self.hat_list:
			hat.draw(screen)
		
		pygame.display.flip()

	def tag_buttons(self):
		button_tags = {
			'A':'Key_space or A',
			'B':'Key_left_ctrl or B',
			'X':'Key_left_shift or X',
			'Y':'Key_left_alt or Y',
			'L':'Key_Q or L',
			'R':'Key_E or R',
			'AB':'AB',
			'XY':'XY',
			'LR':'LR'
		}

		for tag in button_tags:
			if self.dir.button == tag:
				self.event_text.text = button_tags[tag]

	def draw_circle_buttons(self, screen):
		circles = [
			((314,382),self.colorA),
			((285,406),self.colorB),
			((256,382),self.colorX),
			((285,358),self.colorY)
		]
		for circle in circles:
			pygame.draw.circle(screen,circle[1],circle[0],10)

	def draw_rectangle_buttons(self, screen):
		rectangles = [
			((280,290,10,10),self.colorR),
			((95,290,10,10),self.colorL),
			((90,360,10,10),self.colorUp),
			((90,396,10,10),self.colorDown),
			((70,378,10,10),self.colorLeft),
			((108,378,10,10),self.colorRight)
		]
		for rectangle in rectangles:
			pygame.draw.rect(screen,rectangle[1],rectangle[0])
# ---------------------------------------------------------------------

def main():
	pass

if __name__ == '__main__':
	main()
