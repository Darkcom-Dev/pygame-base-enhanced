#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  button.py
#  
#  Copyright 2021 Braulio Madrid <darkcom@darkcom-X455LD>
#  

# ------------------------------------------------------------ Imports
import sys
import pygame as pg
import config as cfg

# ------------------------------------------------------------ Classes
class Button():
	"""
	Create a functional button using pygame.draw.rect and pygame.font
	require import pygame
			
	TODO:
	- Separate color rect out of color font.
	- Separate colors generate very amount of arguments, considere use a style dict.
	- Integrate effects from outline, shadow and chromatic classes.
	- Make that configure method apply changes.
	"""
	def __init__(self, rect, text = 'text', onclickFunction = None, **kwargs):
		"""
		Constructor fucntion for the class
		
		args:
		---
		rect: pygame.Rect
		text: str # better name label
		onclickFunction: any Python function or method name
		kwargs: dict
		
		return:
		---
		None
		"""
		

		# Rect for rect frame, also used for text aligment
		self.rect = rect
		# text aligment
		self.align = 'center'
		self.valign = 'mid'
		

		# On Click Function
		self.onclickFunction = onclickFunction

		# Optional arguments for button class
		self.kwargs = kwargs
		if self.kwargs != None:
			self.configure(self.kwargs)
		
		# private boolean variable events, posible read only return 
		self.in_rect = bool()
		self.enabled = True
		self._event = {'clicked': False, 'highlighted' : False}
		
		# text content for button label
		self.text = text
		self.font = pg.font.SysFont(cfg.font_family, cfg.font_size)
		
		
	def draw(self, screen):
		"""
		Draw a rect frame and text label for button
		
		args:
		---
		screen : pygame.Surface
		
		return:
		---
		None
		"""
		
		fnt_render = self.font.render(self.text, True, cfg.font_disabled_color)
		
		if self.enabled:
			self.pos = pg.mouse.get_pos()
			self.mouse = pg.mouse.get_pressed()
			self.in_width = self.pos[0] > self.rect[0] and self.pos[0] <= self.rect[0] + self.rect[2]
			self.in_height = self.pos[1] > self.rect[1] and self.pos[1] <= self.rect[1] + self.rect[3]
			self.in_rect = self.in_width and self.in_height
			# ~ print(f'events: {self._event}')
			
			if self.mouse == (1,0,0): # Clicked
				if self.in_rect:
					pg.draw.rect(screen, cfg.border_clicked_color,self.rect, cfg.border_width, cfg.border_radius, cfg.border_top_left_radius, cfg.border_top_right_radius, cfg.border_bottom_left_radius, cfg.border_bottom_right_radius)
					fnt_render = self.font.render(self.text, True, cfg.font_clicked_color)
					if self._event['clicked'] == False:
						
						if self.onclickFunction != None: self.onclickFunction()
					self._event['clicked'] = True
					
			else: # Highlight
				
				self._event['clicked'] = False
				if self.in_rect:
					pg.draw.rect(screen, cfg.border_highlight_color,self.rect, cfg.border_width, cfg.border_radius, cfg.border_top_left_radius, cfg.border_top_right_radius, cfg.border_bottom_left_radius, cfg.border_bottom_right_radius)
					fnt_render = self.font.render(self.text,True, cfg.font_highlight_color)
					self._event['highlighted'] = True
				else:
					pg.draw.rect(screen,cfg.border_normal_color,self.rect, cfg.border_width, cfg.border_radius, cfg.border_top_left_radius, cfg.border_top_right_radius, cfg.border_bottom_left_radius, cfg.border_bottom_right_radius)
					fnt_render = self.font.render(self.text,True, cfg.font_normal_color)
					self._event['highlighted'] = False
		else:
			pg.draw.rect(screen,cfg.border_disabled_color,self.rect, cfg.border_width, cfg.border_radius, cfg.border_top_left_radius, cfg.border_top_right_radius, cfg.border_bottom_left_radius, cfg.border_bottom_right_radius)
			fnt_render = self.font.render(self.text,True, cfg.border_disabled_color)
		
		# Dibuja la fuente en pantalla
		# Alinear texto en rectangulo
		
		align_x = self.rect[0]
		if self.align == 'left':
			align_x += 10 # 10 es el border radius
		elif self.align == 'center':
			align_x += self.rect[2] // 2 - fnt_render.get_width() // 2
		elif self.align == 'right':
			align_x += (self.rect[2] - fnt_render.get_width() - 10)
		
		align_y = self.rect[1]
		if self.valign == 'top':
			align_y += 10 # 10 es el border radius
		elif self.valign == 'mid':
			align_y += self.rect[3] // 2 - fnt_render.get_height() // 2
		elif self.valign == 'bottom':
			align_y += (self.rect[3] - fnt_render.get_height() - 10)
		
		screen.blit(fnt_render,(align_x, align_y, self.rect[2] - 10, self.rect[3] - 10))
			
	def configure (self, kwargs):
		""" 
		Method that configure arguments from a dictionary
		
		args:
		---
		kwargs: dict
		
		return:
		---
		None
		"""
		self.kwargs = {**kwargs, **self.kwargs} # Merge various dictionaries
		
		if 'normal_color' in self.kwargs:
			self.normal_color = self.kwargs['normal_color']
		elif 'highlight_color' in self.kwargs:
			self.highlight_color = self.kwargs['highlight_color']
		elif 'clicked_color' in self.kwargs:
			self.clicked_color = self.kwargs['clicked_color']
		elif 'disabled_color' in self.kwargs:
			self.disabled_color = self.kwargs['disabled_color']
		elif 'enabled' in self.kwargs:
			self.enabled = self.kwargs['enabled']
		elif 'onclickFunction' in self.kwargs:
			self.onclickFunction = self.kwargs['onclickFunction']
		elif 'text' in self.kwargs:
			self.text = self.kwargs['text']
		elif 'align' in self.kwargs:
			self.align = self.kwargs['align']
		elif 'valign' in self.kwargs:
			self.valign = self.kwargs['valign']
		else:
			pass
# -------------------------------------------------..... Program entry

def default_test ():
	""" Test Function for button command, return none"""
	print('\x1b[96mMessage from default test function in button module for Button class.\x1b[0m')

def main ():
	""" Entry function program """
	
	pg.init()
	display = pg.display.set_mode((600, 400))
	
	pg.display.set_caption('Button test class')
	
	# Button creation
	rect = pg.Rect(200,300,250,75)
	test_button = Button(rect, 'Hola mundo', default_test)
	# Changing color directly
	test_button.normal_color = (125, 0, 0)
	# Changing style from configure function - NOT FUNCTIONAL
	# ~ test_button.enabled = False
	
	
	new_config = {	"highlight_color" : (0, 75 , 0), 
					"clicked_color" : (0, 75,75), 
					"disabled_color" : (0, 0, 75), 
					"align" : "right", 
					"valign" : "bottom"}
	test_button.configure(new_config)
	test_button.configure({"highlight_color" : (0,0,75)})
	
	
	"""
	En conclusion permite un solo cambio
	"""
	
	while 1:
		
		test_button.text = str(pg.mouse.get_pos())
		display.fill((13,17,23))
		test_button.draw(display)
		
		for event in pg.event.get():
			if event.type == pg.QUIT:
				sys.exit()
		pg.display.update()
	return 0

if __name__ == '__main__':
	main()
