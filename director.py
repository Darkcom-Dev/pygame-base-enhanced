# -*- encoding: utf-8 -*-

# Módulos
import pygame as pg
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
		self.screen = pg.display.set_mode((cfg.WIDTH, cfg.HEIGHT),HWSURFACE|DOUBLEBUF|pg.VIDEORESIZE|RESIZABLE)
		pg.display.set_caption(cfg.Caption)
		pg.display.set_icon(pg.image.load(cfg.SpritesDir + cfg.GameIcon)) # .Convert(Deja un recuadro negro muy feo)
		self.scene = None
		self.fullscreen = False
		self.quit_flag = False
		self.clock = pg.time.Clock()
		
		pg.mixer.music.set_volume(cfg.BgmVolume)
		
	
		self.J1 = None

		if pg.joystick.get_count() > 0:
			pg.joystick.init() # inicializa el modulo de joystick
			self.J1 = pg.joystick.Joystick(0) # crea una instancia de un joystick
			self.J1.init() # inicializa la instancia de un joystick

		if self.J1 != None:
			if cfg.DebugMode:
				print(f'joysticks: {pg.joystick.get_count()}')
				
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
		self.joybutton_down = False
		self.horizontal = 0
		self.vertical = 0

	

	def loop(self):
		'''Pone en funcionamiento el juego.'''

		while not self.quit_flag:
			time = self.clock.tick(cfg.FrameTicks)
			# Eventos de Salida
			for event in pg.event.get():
				if event.type == pg.QUIT:
					self.quit()
				if event.type == pg.KEYDOWN:
					if event.key == pg.K_ESCAPE:
						print(f'current volume: {float(pg.mixer.music.get_volume())}, bgm volume: {cfg.BgmVolume}')
						if float(pg.mixer.music.get_volume()) != cfg.BgmVolume:
							
							cfg.set_volume(pg.mixer.music.get_volume())
						
							if cfg.DebugMode:
								print(f'saved volume at: {pg.mixer.music.get_volume()}')
						
						self.quit()
				self.joybutton_down = event.type == pg.JOYBUTTONDOWN

			self.keys = pg.key.get_pressed()
			#Aqui es donde se deben hacer los eventos de las teclas
			# Tendrá la configuracion de botones de SNES
			
			# detecta eventos de teclado y joystick
			self.handle_controller_input()
			
			# detecta eventos
			self.scene.on_event()

			# actualiza la escena
			self.scene.on_update()

			# dibuja la pantalla
			self.scene.on_draw(self.screen)
			pg.display.flip()

	
	def handle_controller_input(self):

		if self.J1 is not None:
			horizontal_joystick = self.J1.get_hat(0)[0]
			vertical_joystick = self.J1.get_hat(0)[1]

			self.button = self.get_joystick_button(self.J1)if self.joybutton_down else self.get_keyboard_button(self.keys)
			# Eje horizontal
			self.horizontal = horizontal_joystick if horizontal_joystick != 0 else	self.get_horizontal_direction(self.keys)
			# Eje vertical
			self.vertical = vertical_joystick if vertical_joystick != 0	else self.get_vertical_direction(self.keys)

		else:				
			self.button = self.get_keyboard_button(self.keys)
			
			# Eje horizontal
			self.horizontal = self.get_horizontal_direction(self.keys)

			# Eje vertical
			self.vertical = self.get_vertical_direction(self.keys)
		
			
	def get_keyboard_button(self, keys):
		if keys[pg.K_SPACE] and keys[pg.K_LCTRL]:return 'AB'
		elif keys[pg.K_LSHIFT] and keys[pg.K_LALT]:return 'XY'
		elif keys[pg.K_q] and keys[pg.K_e]:return 'LR'
		elif keys[pg.K_SPACE]:return 'A'
		elif keys[pg.K_LCTRL]:return 'B'
		elif keys[pg.K_LSHIFT]:return 'X'
		elif keys[pg.K_LALT]:return 'Y'
		elif keys[pg.K_q]:return 'L'
		elif keys[pg.K_e]:return 'R'		
		return None

	def get_joystick_button(self, joystick):
		if joystick.get_button(2):return 'A'
		elif joystick.get_button(1):return 'B'
		elif joystick.get_button(3):return 'X'
		elif joystick.get_button(0):return 'Y'
		elif joystick.get_button(4):return 'L'
		elif joystick.get_button(5):return 'R'
		return None
	
	def get_vertical_direction(self, keys):
		# Eje vertical
		vertical_keys = {
		    pg.K_w: 1,
		    pg.K_UP: 1,
		    pg.K_s: -1,
		    pg.K_DOWN: -1
		}

		vertical_direction = 0
		
		for key, value in vertical_keys.items():
			if self.keys[key]:
				vertical_direction = value
				break
		
		return vertical_direction
	
	def get_horizontal_direction(self, keys):
		# Eje horizontal
		horizontal_keys = {
		    pg.K_d: 1,
		    pg.K_RIGHT: 1,
		    pg.K_a: -1,
		    pg.K_LEFT: -1
		}

		horizontal_direction = 0
		
		for key, value in horizontal_keys.items():
			if self.keys[key]:
				horizontal_direction = value
				break
		
		return horizontal_direction
	
	def change_scene(self, scene):
		'''Altera la escena actual.'''
		self.scene = scene

	def quit(self):
		self.quit_flag = True
