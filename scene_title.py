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
		
		# ~ pygame.joystick.init() # inicializa el modulo de joystick
		# ~ self.J1 = pygame.joystick.Joystick(0) # crea una instancia de un joystick
		# ~ self.J1.init() # inicializa la instancia de un joystick
		
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
		

		self.buttonBPosition = (314,382)
		self.buttonAPosition = (285,406)
		self.buttonXPosition = (256,382)
		self.buttonYPosition = (285,358)
		
		self.buttonLPosition = (95,290,10,10)
		self.buttonRPosition = (280,290,10,10)
		
		self.dPadUp = (90,360,10,10)
		self.dPadDown = (90,396,10,10)
		self.dPadLeft = (70,378,10,10)
		self.dPadRight = (108,378,10,10)
		
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

		# Directions
		if self.dir.horizontal == -1:
			self.colorLeft = self.activeColor
			self.event_text.text = "Key_left"
		else:
			self.colorLeft = self.normalColor
		if self.dir.horizontal == 1:
			self.colorRight = self.activeColor
			self.event_text.text = "Key_right"
		else:
			self.colorRight = self.normalColor
		if self.dir.vertical == 1:
			self.colorUp = self.activeColor
			self.event_text.text = "Key_up"
		else:
			self.colorUp = self.normalColor
		if self.dir.vertical == -1:
			self.colorDown = self.activeColor
			self.event_text.text = "Key_down"
		else:
			self.colorDown = self.normalColor
		# Buttons
		if self.dir.button == 'AB':
			self.event_text.text == 'AB'
		if self.dir.button == 'XY':
			self.event_text.text == 'XY'
		if self.dir.button == 'LR':
			self.event_text.text == 'LR'
		if self.dir.button == 'A':
			self.colorA = self.activeColor
			self.event_text.text = "Key_space or A"
		else:
			self.colorA = self.normalColor
		if self.dir.button == 'B':
			self.colorB = self.activeColor
			self.event_text.text = "Key_left_ctrl or B"
		else:
			self.colorB = self.normalColor
		if self.dir.button == 'X':
			self.colorX = self.activeColor
			self.event_text.text = "Key_left_shift or X"
		else:
			self.colorX = self.normalColor
		if self.dir.button == 'Y':
			self.colorY = self.activeColor
			self.event_text.text = "Key_left_alt or Y"
		else:
			self.colorY = self.normalColor
		if self.dir.keys[pygame.K_TAB]:
			self.event_text.text = "Key_Tab"
		if self.dir.button == 'L':
			self.colorL = self.activeColor
			self.event_text.text = 'L'
		else:
			self.colorL = self.normalColor
		if self.dir.button == 'R':
			self.colorR = self.activeColor
			self.event_text.text = 'R'
		else:
			self.colorR = self.normalColor
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
		
		pygame.draw.circle(screen,self.colorA,self.buttonAPosition,10)
		pygame.draw.circle(screen,self.colorB,self.buttonBPosition,10)
		pygame.draw.circle(screen,self.colorX,self.buttonXPosition,10)
		pygame.draw.circle(screen,self.colorY,self.buttonYPosition,10)
		
		pygame.draw.rect(screen,self.colorR, self.buttonRPosition)
		pygame.draw.rect(screen,self.colorL, self.buttonLPosition)
		pygame.draw.rect(screen,self.colorUp, self.dPadUp)
		pygame.draw.rect(screen,self.colorDown, self.dPadDown)
		pygame.draw.rect(screen,self.colorLeft, self.dPadLeft)
		pygame.draw.rect(screen,self.colorRight, self.dPadRight)
		
		self.history_text.draw(screen)
		
		for info in self.info_text_list:
			info.draw(screen)
			
		for hat in self.hat_list:
			hat.draw(screen)
		
		pygame.display.flip()

# ---------------------------------------------------------------------

def main():
	pass

if __name__ == '__main__':
	main()
