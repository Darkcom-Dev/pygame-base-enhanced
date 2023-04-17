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
import widget

# ------------------------------------------------------------ Classes

"""
	TODO:	
	- Integrate effects from outline, shadow and chromatic classes.
	- Make that configure method apply changes.
	- To habilitate make Rect from a tuple.
	
"""

class Button(widget.Widget):
	"""
	Create a functional button using pygame.draw.rect and pygame.font
	require import pygame
	"""		
	
	def __init__(self, rect, text = 'text', onclickFunction = None, style = None):
		"""
		Constructor fucntion for the class
		
		### Args:
		rect: pygame.Rect
		text: str : text for show in button font
		onclickFunction: any Python function or method name
		
		### Return:
		None
		"""
		
		super().__init__(rect, text, onclickFunction, style)		
		
		# font for text label
		self.pgFont = pg.font.SysFont(self.font_family, self.font_size)

		
	def draw(self, surface):
		"""
	    Draw a rect frame and text label for button.

	    ### Args:
	    `surface` : pygame.Surface

	    ### Return:
	    None
	    """
		

	    # Colors
		event_color = self.font_disabled_color
		bg_event_color = self.bg_disabled_color

	    # Events
		self.handle_events()
		if self.enabled:
			if self._event['clicked']:
				bg_event_color = self.bg_clicked_color
				event_color = self.font_clicked_color
			elif self._event['highlighted']:
				bg_event_color = self.bg_highlight_color
				event_color = self.font_highlight_color
			else:
				bg_event_color = self.bg_color
				event_color = self.font_color
				
		pg.draw.rect(surface,bg_event_color,self.rect, self.stroke, self.border_radius, self.top_left_radius, self.top_right_radius, self.bottom_left_radius, self.bottom_right_radius)
		font_render = self.pgFont.render(self.text, True, event_color)

	    # Dibuja la fuente en pantalla
		surface.blit(font_render,self.align(self.rect, font_render, self.style['font_align'], self.style['font_valign'], self.style['border_radius']))

	
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
	new_config = {	
		"font_highlight_color" : (0, 75 , 0), 
		"font_clicked_color" : (0, 75,75), 
		"font_disabled_color" : (0, 0, 75), 
		"bg_disabled_color" : "red",
		"font_family": "G15",
		"font_align" : "right", 
		"font_valign" : "bottom",
		"border_radius" : 15,
		}
	test_button = Button(rect, 'Hola mundo', default_test, style=new_config)
	test_button.enabled = True
	
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
