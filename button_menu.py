#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  button_menu.py
#  
#  
#  --------------------------------------------------------- Imports
import button as btn
import pygame as pg
import config as cfg
# ---------------------------------------------------------- Classes
class Menu:
	"""
	Class that create a menu based in button
	require button module and pygame.
	
	TODO:
	- make that configure works
	"""
	
	def __init__ (self, kmenu, rect, orientation = 'horizontal', padx = 0, pady = 0, **kwargs):
		""" 
		Constructor of Menu object.
		
		args:
		---
		color : tuple	# rgb color.
		kmenu : dict(label : funtion)
		orientation : str	# 'horizontal' or 'vertical'
		padx : int default 0	# horizontal margin in pixels.
		pady : int default 0	# vertical margin in pixels.
		kwargs : dict	# optional visual values generally.
		"""
		# color for extern frame rect.
		
		# dictionary menu with label and function or method name.
		self._kmenu = kmenu

		# orientation string only 'horizontal' or 'vertical' posible values.
		self.orientation = orientation
		# optional dictionary values
		self._kwargs = kwargs
		if self._kwargs != None:
			self.configure(self._kwargs)
			print(self.orientation)
		
		self.__item_count = len(self._kmenu)
		
		# rect for frame and buttons rect calculations
		self.rect = rect
		# horizontal margin
		self.padx = padx
		# verticla margin
		self.pady = pady
		
		if self.orientation == 'horizontal':
			self.__portion = rect.w // self.__item_count
			self.__item_rects = [pg.Rect(self.rect.x + self.padx + (self.__portion * index), self.rect.y + self.pady, self.__portion - (self.padx * 2), self.rect.h - (self.pady * 2)) for index in range(self.__item_count)]
		if self.orientation == 'vertical':
			self.__portion = rect.h // self.__item_count
			self.__item_rects = [pg.Rect(self.rect.x + self.padx, self.rect.y + self.pady + (self.__portion * index), self.rect.w - (self.padx * 2), self.__portion - (self.pady * 2)) for index in range(self.__item_count)]
			
		# Separate keywords of functions
		self._menu = list(self._kmenu.keys())
		self._commands = list(self._kmenu.values())
		# Create buttons for each keyword dictionary
		self._buttons = [btn.Button(self.__item_rects[i], self._menu[i], self._commands[i]) for i in range(self.__item_count)]
		
		
	def configure (self, kwargs):
		""" 
		Configure dictionary for optional arguments
		
		args:
		---
		kwargs: dict
		
		return:
		---
		None
		"""
		self._kwargs = {**kwargs, **self._kwargs} # Merge various dictionaries
			
		if 'orientation' in self._kwargs:
			self.orientation = self._kwargs['orientation']
			
		
	def draw (self, screen):
		"""
		Draw function
		
		args:
		---
		screen: pygame.Surface	# canvas for draw all buttons.
		
		return:
		---
		None
		"""
		
		pg.draw.rect(screen, cfg.frame_normal_color, self.rect, cfg.frame_width, cfg.frame_radius, cfg.frame_top_left_radius, cfg.frame_top_right_radius, cfg.frame_bottom_left_radius, cfg.frame_bottom_right_radius)
		
		for button in self._buttons:
			button.draw(screen)

# -------------------------------------------------- Program Entry
def new_campaign ():
	""" Test function """
	print("\x1b[31m option test 1\x1b[0m Nueva campaña")

def load_func ():
	""" Test function """
	print("\x1b[32m option test 2\x1b[0m Load")
	
def options_func ():
	""" Test function """
	print("\x1b[33m option test 3\x1b[0m Options")

def credits_function ():
	""" Test function """
	print("\x1b[34m option test 4\x1b[0m Credits")

def main(args):
	""" Entry function program """

	pg.init()
	root = pg.display.set_mode((600,400))
	root.fill((35,35,70))
	pg.display.set_caption('Menu creator Class')
	
	
	# El menu es un diccionario con el nombre del boton y el comando a ejecutar
	menu = {
		'Nueva campaña': new_campaign, 
		'Cargar' : load_func, 
		'Opciones': options_func, 
		'Créditos': credits_function
		}
	
	menu_rect = pg.Rect(10,76,200,314)
	menu_ui = Menu(menu, menu_rect, 'vertical', 10,5)
	
	config = {'orientation':'horizontal'}
	menu_ui.configure(config)
	
	menu2_rect = pg.Rect(10,10,580,56)
	menu2_ui = Menu(menu, menu2_rect, 'horizontal', 5,10)
	
	while 1:
		for event in pg.event.get():
			if event.type == pg.QUIT:
				sys.exit()
				
		menu_ui.draw(root)
		menu2_ui.draw(root)
		pg.display.update()
	
	return 0

if __name__ == '__main__':
	import sys
	sys.exit(main(sys.argv))
