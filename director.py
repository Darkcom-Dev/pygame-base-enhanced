# -*- encoding: utf-8 -*-

# Módulos
import pygame
import sys
import config as cfg
from pygame.constants import HWSURFACE, DOUBLEBUF, RESIZABLE

class Director:
	"""Representa el objeto principal del juego.

	El objeto Director mantiene en funcionamiento el juego, se
	encarga de actualizar, dibuja y propagar eventos.

	Tiene que utilizar este objeto en conjunto con objetos
	derivados de Scene."""

	def __init__(self):
		'''
		HWSURFACE y DOUBLEBUF = Juntos aumentan la velocidad de los fotogramas
		RESIZABLE = Hace que la ventana pueda ser reescalable, pero
		tambien puede dañar la logica del juego y desajustar las imagenes
		por el hecho de usar constantes
		'''
		self.screen = pygame.display.set_mode((cfg.WIDTH, cfg.HEIGHT),HWSURFACE|DOUBLEBUF|pygame.VIDEORESIZE|RESIZABLE)
		pygame.display.set_caption(cfg.Caption)
		pygame.display.set_icon(pygame.image.load(cfg.SpritesDir + cfg.GameIcon)) # .Convert(Deja un recuadro negro muy feo)
		self.scene = None
		self.fullscreen = False
		self.quit_flag = False
		self.clock = pygame.time.Clock()
		
		pygame.mixer.music.set_volume(cfg.BgmVolume)
		
	
		self.J1 = None

		if pygame.joystick.get_count() > 0:
			pygame.joystick.init() # inicializa el modulo de joystick
			self.J1 = pygame.joystick.Joystick(0) # crea una instancia de un joystick
			self.J1.init() # inicializa la instancia de un joystick

		if self.J1 != None:
			if cfg.DebugMode:
				print(f'joysticks: {pygame.joystick.get_count()}')
				
				print(f'Joystick model: {self.J1.get_name()}') 
				print(f'Joystick: {self.J1} get init: {self.J1.get_init()}')
								   
				print(f'num_axes: {self.J1.get_numaxes()}, num_buttons:  {self.J1.get_numbuttons()}')
				print(f'num_hats: {self.J1.get_numhats()}, num_balls: {self.J1.get_numballs()}')
		else:
			if cfg.DebugMode:
				print('No hay joystick conectado!')
		
		# input manager
		self.keys = None
		
		self.button = ''
		
		self.horizontal = 0
		self.vertical = 0

	def loop(self):
		'''Pone en funcionamiento el juego.'''

		while not self.quit_flag:
			time = self.clock.tick(cfg.FrameTicks)
			# Eventos de Salida
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					self.quit()
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_ESCAPE:
						print(f'current volume: {float(pygame.mixer.music.get_volume())}, bgm volume: {cfg.BgmVolume}')
						if float(pygame.mixer.music.get_volume()) != cfg.BgmVolume:
							
							cfg.set_volume(pygame.mixer.music.get_volume())
						
							if cfg.DebugMode:
								print(f'saved volume at: {pygame.mixer.music.get_volume()}')
						
						self.quit()

			self.keys = pygame.key.get_pressed()
			#Aqui es donde se deben hacer los eventos de las teclas
			# Tendrá la configuracion de botones de SNES
			
			if self.J1 != None:
				# Doble boton a la vez
				if self.keys[pygame.K_SPACE] and self.keys[pygame.K_LCTRL]:
					print('AB')
					self.button = 'AB'
				elif self.keys[pygame.K_LSHIFT] and self.keys[pygame.K_LALT]:
					print('XY')
					self.button = 'XY'
				elif self.keys[pygame.K_q] and self.keys[pygame.K_e]:
					print('LR')
					self.button = 'LR'
				
				# Posibilidades de un solo boton
				elif self.keys[pygame.K_SPACE] or self.J1.get_button(2):
					self.button = 'A'
				elif self.keys[pygame.K_LCTRL] or self.J1.get_button(1):
					self.button = 'B'
				elif self.keys[pygame.K_LSHIFT] or self.J1.get_button(3):
					self.button = 'X'
				elif self.keys[pygame.K_LALT] or self.J1.get_button(0):
					self.button = 'Y'
				elif self.keys[pygame.K_q] or self.J1.get_button(4):
					self.button = 'L'
				elif self.keys[pygame.K_e] or self.J1.get_button(5):
					self.button = 'R'
				else:
					self.button = None
				
				# Eje horizontal
				if self.keys[pygame.K_a] or self.keys[pygame.K_LEFT] or self.J1.get_hat(0)[0] == -1:
					self.horizontal = -1
				elif self.keys[pygame.K_d] or self.keys[pygame.K_RIGHT] or self.J1.get_hat(0)[0] == 1:
					self.horizontal = 1
				else:
					self.horizontal = 0
				
				# Eje vertical
				if self.keys[pygame.K_w] or self.keys[pygame.K_UP] or self.J1.get_hat(0)[1] == 1:
					self.vertical = 1
				elif self.keys[pygame.K_s] or self.keys[pygame.K_DOWN] or self.J1.get_hat(0)[1] == -1:
					self.vertical = -1
				else:
					self.vertical = 0
			else:
				# Doble boton a la vez
				if self.keys[pygame.K_SPACE] and self.keys[pygame.K_LCTRL]:
					print('AB')
					self.button = 'AB'
				elif self.keys[pygame.K_LSHIFT] and self.keys[pygame.K_LALT]:
					print('XY')
					self.button = 'XY'
				elif self.keys[pygame.K_q] and self.keys[pygame.K_e]:
					print('LR')
					self.button = 'LR'
				
				# Posibilidades de un solo boton
				elif self.keys[pygame.K_SPACE]:
					self.button = 'A'
				elif self.keys[pygame.K_LCTRL]:
					self.button = 'B'
				elif self.keys[pygame.K_LSHIFT]:
					self.button = 'X'
				elif self.keys[pygame.K_LALT]:
					self.button = 'Y'
				elif self.keys[pygame.K_q]:
					self.button = 'L'
				elif self.keys[pygame.K_e]:
					self.button = 'R'
				else:
					self.button = None
				
				
				# Eje horizontal
				if self.keys[pygame.K_a] or self.keys[pygame.K_LEFT]:
					self.horizontal = -1
				elif self.keys[pygame.K_d] or self.keys[pygame.K_RIGHT]:
					self.horizontal = 1
				else:
					self.horizontal = 0
				
				# Eje vertical
				if self.keys[pygame.K_w] or self.keys[pygame.K_UP]:
					self.vertical = 1
				elif self.keys[pygame.K_s] or self.keys[pygame.K_DOWN]:
					self.vertical = -1
				else:
					self.vertical = 0
			
			# detecta eventos
			self.scene.on_event()

			# actualiza la escena
			self.scene.on_update()

			# dibuja la pantalla
			self.scene.on_draw(self.screen)
			pygame.display.flip()

	def change_scene(self, scene):
		'''Altera la escena actual.'''
		self.scene = scene

	def quit(self):
		self.quit_flag = True
