#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
""" 
	Create a functional Entry Widget with pygame module
	Require import pygame
	
	TODO:
	- Limitate text string length or auto limitate with rect width
	- Hide text with asterisk or other character, neccesary for passwords
	- self.text is real text to get data and self.show_text will be text to show in screen, necesary for passwords
	
	- Create a style set for widgets
"""

"""
Este código define una clase llamada "Entry" que representa una caja de entrada de texto. 
Utiliza el módulo Pygame para dibujar la caja en la pantalla y para procesar las entradas de teclado.

El método init define los atributos iniciales de la caja de entrada de texto, 
como su posición y tamaño (rect), el color de fondo (color), la longitud máxima del texto (limit), 
y el carácter de relleno a usar en caso de estar en modo de contraseña (password).

El método draw dibuja la caja de entrada de texto en la pantalla, 
y renderiza el texto que ha sido ingresado hasta el momento en la caja.

El método input se encarga de procesar las entradas de teclado. 
Si la tecla presionada es la tecla "borrar", elimina el último carácter del texto. 
De lo contrario, busca la tecla presionada en el diccionario key_mappings y 
agrega el carácter correspondiente al texto.

En resumen, esta clase proporciona una forma sencilla de agregar una caja de entrada de 
texto a una aplicación de Pygame y procesar las entradas de teclado.
"""

import pygame as pg

class Entry:
	"""
	A class to create an input box with Pygame.

	Attributes:
		rect (pg.Rect): Rectangle object that defines the position and dimensions of the input box.
		color (pg.Color): Pygame Color object that defines the color of the input box.
		limit (int): An integer that defines the maximum length of the input box. Default is 40.
		password (str): A string to set a password character to mask the input. Default is empty.

	Methods:
		draw(screen): Draws the input box on the screen.
		input(key): Receives a key press and adds it to the input text or deletes the last character.
	"""

	def __init__ (self, rect: pg.Rect, color: pg.Color, limit: int = 40, password:str = ''):
		"""
		Initializes the Entry object.

		Args:
			rect (pg.Rect): Rectangle object that defines the position and dimensions of the input box.
			color (pg.Color): Pygame Color object that defines the color of the input box.
			limit (int, optional): An integer that defines the maximum length of the input box. Default is 40.
			password (str, optional): A string to set a password character to mask the input. Default is empty.
		"""
		self.rect = rect
		self.color = color
		self.text = ''
		
		self.limit = limit
		self.password = password # Fillchar
		self.font_size = 20 # Size of char
		self.max_limit = self.rect[2] // (12) # 12 is fixed char_size, find other formula
		
		# Creates a font object for rendering the text.
		self.font = pg.font.SysFont('Arial',self.font_size)
			
	def draw (self, screen: pg.Surface):
		"""
		Draws the input box on the screen.

		Args:
			screen (pg.Surface): Pygame surface object that represents the window to draw on.
		"""
		pg.draw.rect(screen, self.color, self.rect, 1)
		
		# Limits the text length to the maximum length or the box size, whichever is smaller.
		text_to_render = self.text[0:self.limit] if self.font.size(self.text)[0] <= self.rect[2] else self.text[0:self.max_limit]

		# If the password attribute is set, replaces the input text with the password character.
		if self.password:
			text_to_render = len(text_to_render) * self.password
		# Renders the text and blits it on the screen.
		rendered_text = self.font.render(text_to_render, True, self.color)
		screen.blit(rendered_text,(self.rect[0] + 3, self.rect[1] + 3, self.rect[2] - 10, self.rect[3] - 10))
		
	def input (self, key):
		"""
		Receives a key press and adds it to the input text or deletes the last character.

		Args:
			key (int): An integer representing the key pressed.
		"""		
		self.max_limit = self.rect[2] // (12)
		
		# Dictionary that maps keys to characters.
		key_mappings = {
			97: 'A', 98: 'B', 99: 'C', 100: 'D', 101: 'E',
			102: 'F', 103: 'G', 104: 'H', 105: 'I',	106: 'J',
			107: 'K', 108: 'L',	109: 'M', 110: 'N',	111: 'O',
			112: 'P', 113: 'Q',	114: 'R', 115: 'S',	116: 'T',
			117: 'U', 118: 'V',	119: 'W', 120: 'X',	121: 'Y',
			122: 'Z', 32: ' ',	48: '0', 49: '1', 50: '2',
			51: '3', 52: '4', 53: '5', 54: '6', 55: '7',
			56: '8', 57: '9', 8: '', 13: '\n'
		}
		
		if key == 8:
			self.text = self.text[0:-1]
		elif key in key_mappings:
			self.text += key_mappings[key]

def main(args):
	# Inicializar pygame
	pg.init()

	# Crear una pantalla
	display = pg.display.set_mode((600, 400))
	pg.display.set_caption('Entry test class')
	
	# Crear una caja de entrada
	_rect = pg.Rect(200,200,200,50)
	test_entry = Entry(_rect, (255,0,0),20,password='\n')
	
	# Bucle principal
	while True:
		# Dibujar el objeto Entry en la pantalla
		display.fill((13,17,23))
		test_entry.draw(display)
		
		# Manejar eventos
		for event in pg.event.get():
			if event.type == pg.QUIT:
				# Terminar la aplicación
				sys.exit()
			if event.type == pg.KEYDOWN:
				# Manejar la entrada de texto del usuario / Entrada de teclado
				test_entry.input(event.key)

		# Actualizar la pantalla		
		pg.display.update()
	
	# Finalizar la aplicación
	return 0

if __name__ == '__main__':
	import sys
	# Ejecuta la funcion main() y salir con el codigo de exito.
	sys.exit(main(sys.argv))
