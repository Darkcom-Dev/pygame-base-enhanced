#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Módulos
import scene

import pygame

import math
import random
import text_presets as preset
import font
import config as cfg
import button as btn
import scene_manager
# Constantes


# Clases
# ---------------------------------------------------------------------

class SceneHome(scene.Scene):
	"""Escena inicial del juego, esta es la primera que se carga cuando inicia"""

	def __init__(self, director):
		""" Aqui la funcion init de las escenas funciona como el metodo Start o Awake en Unity"""

		# ~ scene.Scene.__init__(self, director)

		self.dir = director

		self.mouse = tuple()
		self.clock = pygame.time.Clock()
		self.fps = self.clock.get_fps()
		self.info = str()
		self.ticks = int()
		self.event = str()

		self.history_text = preset.history_text
		self.info_text = preset.info_text
		self.caption_text = preset.caption_text
		self.hint_text = preset.hint_text
		self.subevent_text = preset.subevent_text
		self.subevent_text.text = "Sub Event 1"
		self.event_text = preset.event_text
		
		self.button = btn.Button([cfg.WIDTH/2, cfg.HEIGHT, 140, 40])

	def on_update(self):
		""" on_update funciona exactamente igual que el metodo Update de Unity """
		self.mouse = pygame.mouse.get_pos()
		self.clock = pygame.time.Clock()
		self.fps = self.clock.get_fps()
		self.ticks = pygame.time.get_ticks()
		
		self.info = "ticks: " + str(self.ticks) + " mouse pos: " + str(self.mouse) + " fps: " + str(self.fps)


	def on_event(self):
		""" on_event funciona como Update, pero para efectos de teclado """

		if self.dir.keys[pygame.K_LEFT]:
			self.event_text.text = "Key_left"
		if self.dir.keys[pygame.K_RIGHT]:
			self.event_text.text = "Key_right"
		if self.dir.keys[pygame.K_1]:
			self.event_text.text = "KEY1 from home"
			scene_manager.change_scene("scene_title")
		if self.dir.keys[pygame.K_2]:
			scene_manager.change_scene("scene_credits")
		if self.dir.keys[pygame.K_3]:
			scene_manager.change_scene("scene_sound_test")
		if self.dir.keys[pygame.K_4]:
			scene_manager.change_scene("scene_physics")
		mouse = pygame.mouse.get_pressed()

		if mouse == (1,0,0):
			self.event_text.text= "Click Izquierdo"

	def on_draw(self, screen):
		""" on_draw funciona como Update de Unity, pero para el dibujado."""

		screen.fill(cfg.ScreenFillColor)
		
		self.button.draw(screen)
		
		self.event_text.position = (math.sin(pygame.time.get_ticks()/1000) * cfg.WIDTH/4 + cfg.WIDTH/2, random.randrange((cfg.HEIGHT/2) -2,(cfg.HEIGHT/2) +2))
		self.event_text.draw(screen, "chromatic",2)
		
		sintime = math.sin(pygame.time.get_ticks()/1000)*128 + 128
		costime = math.cos(pygame.time.get_ticks()/1000)*128 + 128
		self.color = (255,costime,sintime)
		distance = math.sin(pygame.time.get_ticks()/1000)*3
		self.subevent_text.draw(screen, "chromatic", distance)

		self.history_text.draw(screen)

		self.hint_text.draw(screen)
		if 10000 < self.ticks < 20000:
			self.subevent_text.text = "Press 1 go to Input Test Scene"
			self.subevent_text.color = (255,80,80)
		elif 20000 < self.ticks < 30000:
			self.subevent_text.text = "Press 2 go to Credit Test Scene"
		elif 30000 < self.ticks < 40000:
			self.subevent_text.text = "Press 3 go to Sound Test Scene"
		elif 40000 < self.ticks < 50000:
			self.subevent_text.text = "Press 4 go to Physics Test Scene"
		else:
			self.subevent_text.text = "Sub Event 1"

		self.caption_text.draw(screen, "caption",0)

		if 1000 < self.ticks < 2000:
			self.caption_text.text= "Hola... Quien está ahi"
			self.caption_text.color = (255,80,80)
		elif 2000 < self.ticks < 3000:
			self.caption_text.text = "Ahh... Hola!"
			self.caption_text.color = (80, 80, 255)
		elif 3000 < self.ticks < 4000:
			self.caption_text.text = "¿Qué es este lugar?"
			self.caption_text.color = (255,80,80)
		else:
			self.caption_text.text = "Esto es un caption text"
			self.caption_text.color = (80,80,255)

		# surface, color, rect(),width,border_radius,
		posicion = screen.get_width()/2, screen.get_height()/2, 140, 40
		pygame.draw.rect(screen,(175,41,15),posicion,3,10)

		self.ticks -= pygame.time.get_ticks()
		self.info_text.text = self.info + str(self.ticks) + "\n" +str(self.event)
		self.info_text.color = (255,255,255)
		self.info_text.draw(screen, "outline", 2)

		# por alguna razon la pantalla permanece sucia cuando se actualiza la ventana
		pygame.display.flip()

# ---------------------------------------------------------------------

# Funciones
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------

def main():
	SceneHome

if __name__ == '__main__':
	main()
