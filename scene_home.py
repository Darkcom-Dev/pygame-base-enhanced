#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Módulos
import scene

import pygame as pg

import math
import random
import text_presets as preset
import config as cfg
import button_menu as menu
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
		self.clock = pg.time.Clock()
		self.fps = self.clock.get_fps()
		self.info = str()
		self.ticks = 0
		self.scene_ticks = 0
		self.event = str()

		self.history_text = preset.history_text
		self.info_text = preset.info_text
		self.info_text.color = (255,255,255)

		self.caption_text = preset.caption_text
		self.hint_text = preset.hint_text
		self.subevent_text = preset.subevent_text
		self.subevent_text.text = "Sub Event 1"
		self.event_text = preset.event_text
		
		#button_rect = pg.Rect(cfg.WIDTH/2, cfg.HEIGHT, 140, 40)
		#self.button = btn.Button(button_rect)

		self.subevent_dict = {3:"Press 1 go to Input Test Scene",
							 5:"Press 2 go to Credit Test Scene",
							 7:"Press 3 go to Sound Test Scene",
							 8:"Press 4 go to Physics Test Scene"}
		
		self.caption_dict = {2.5:"Esta es la primera escena",
							 3.5:"Comprende de varias escenas de prueba",
							 4.5:"Creado con pygame",
							 6.5:"Creado por braulio madrid"}
		self.menu_dict = {
			'Input':lambda: scene_manager.change_scene("scene_title"),
			'Credits':lambda:scene_manager.change_scene("scene_credits"),
			'Sound':lambda:scene_manager.change_scene("scene_sound_test"),
			'Physics':lambda:scene_manager.change_scene("scene_physics")}
		
		self.menu_rect = pg.Rect(10,76,200,314)
		self.menu_ui = menu.Menu(self.menu_dict, self.menu_rect, 'vertical', 10,5)


	def on_update(self):
		""" on_update funciona exactamente igual que el metodo Update de Unity """
		self.mouse = pg.mouse.get_pos()
		self.clock = pg.time.Clock()
		self.fps = self.clock.get_fps()
		self.ticks = pg.time.get_ticks()
		self.scene_ticks += 1
		self.info = f"ticks: {str(self.ticks)} mouse pos: {str(self.mouse)} fps: {str(self.fps)} scene ticks: {str(self.scene_ticks)}"


	def on_event(self):
		""" on_event funciona como Update, pero para efectos de teclado """

		if self.dir.keys[pg.K_1]:		scene_manager.change_scene("scene_title")
		if self.dir.keys[pg.K_2]:		scene_manager.change_scene("scene_credits")
		if self.dir.keys[pg.K_3]:		scene_manager.change_scene("scene_sound_test")
		if self.dir.keys[pg.K_4]:		scene_manager.change_scene("scene_physics")

		self.event_text.text= str(pg.mouse.get_pressed())

		self.menu_rect = pg.Rect(cfg.WIDTH/2, cfg.HEIGHT, 140, 40)
	def secuential_text(self, dictionary, default_text):

		for key, value in dictionary.items():
			if self.ticks < key * 1000:
				return value
			else:
				pass
		
	def on_draw(self, screen):
		""" on_draw funciona como Update de Unity, pero para el dibujado."""

		screen.fill(cfg.ScreenFillColor)
				
		self.event_text.position = (math.sin(pg.time.get_ticks()/1000) * cfg.WIDTH/4 + cfg.WIDTH/2, random.randrange((cfg.HEIGHT/2) -2,(cfg.HEIGHT/2) +2))
		self.event_text.draw(screen, "chromatic",2)
		
		sintime = math.sin(pg.time.get_ticks()/1000)*128 + 128
		costime = math.cos(pg.time.get_ticks()/1000)*128 + 128		
		distance = math.sin(pg.time.get_ticks()/1000)*3		

		self.history_text.draw(screen)
		self.hint_text.draw(screen)

		# subevent text
		self.subevent_text.draw(screen, "chromatic", distance)
		self.subevent_text.text = self.secuential_text(self.subevent_dict,'Sub Event 1')
		
		# caption text
		self.caption_text.draw(screen, "caption",0)
		self.caption_text.text = self.secuential_text(self.caption_dict,'Caption 1')

		# surface, color, rect(),width,border_radius,
		posicion = pg.Rect(screen.get_width()/2, screen.get_height()/2, 140, 40)
		pg.draw.rect(screen,(255,costime,sintime),posicion,3,10)

		self.menu_ui.draw(screen)

		self.ticks -= pg.time.get_ticks()
		self.info_text.text = self.info + str(self.ticks) + "\n" +str(self.event)
		self.info_text.draw(screen, "outline", 2)

		# por alguna razon la pantalla permanece sucia cuando se actualiza la ventana
		pg.display.flip()


	
			
# ---------------------------------------------------------------------

# Funciones
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------

def main():
	SceneHome

if __name__ == '__main__':
	main()
