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
	
"""

class Button(widget.Widget):
	"""
	Create a functional button using pygame.draw.rect and pygame.font
	require import pygame
	"""		
	style = {
        'font': 'System',
        'font_size': 20,
		'font_align': 'center',
		'font_valign': 'middle',
        'text_color': 'black',
		'font_clicked_color' : 'blue',
		'font_disabled_color': 'gray',
		'font_highlight_color': 'white',
        'bg_color': 'white',
		'bg_clicked_color': '#f5f5ff',
		'bg_disabled_color': '#fff5cc',
		'bg_highlight_color': 'gray',
		'stroke': 0,
		'border_radius': 0,
		'top_left_radius': -1,
		'top_right_radius': -1,
		'bottom_left_radius': -1,
		'bottom_right_radius': -1

    }
	def __init__(self, rect, text = 'text', onclickFunction = None, style = None, **kwargs):
		"""
		Constructor fucntion for the class
		
		### Args:
		rect: pygame.Rect
		text: str : text for show in button font
		onclickFunction: any Python function or method name
		kwargs: dict
		
		### Return:
		None
		"""
		
		# Rect for rect frame, also used for text aligment
		self.rect = rect
		# text aligment
		self.style = style or Button.style
		
		# On Click Function
		self.onclickFunction = onclickFunction

		# Optional arguments for button class
		self.kwargs = kwargs
				
		# private boolean variable events, posible read only return 
		self.in_rect = bool()
		self.enabled = True
		self._event = {'clicked': False, 'highlighted' : False}
		
		# text content for button label
		self.text = text
		# font for text label
		font = self.style.get('font',Button.style['font'])
		font_size = self.style.get('font_size',Button.style['font_size'])
		self.font = pg.font.SysFont(font, font_size)
		
	
	def handle_events(self):
		"""
		Handle button events.	
		### Return:
		None
		"""
		if not self.enabled:    return	
		
		self.pos = pg.mouse.get_pos()
		self.mouse = pg.mouse.get_pressed()
		self.in_rect = self.rect.collidepoint(self.pos)	
		if self.mouse == (1, 0, 0):
			if self.in_rect:
				if not self._event['clicked'] and self.onclickFunction is not None:	self.onclickFunction()
			self._event['clicked'] = self.in_rect
		    
		# Highlight
		else:
			self._event['highlighted'] = self.in_rect
			self._event['clicked'] = False
		    

	    
	def draw(self, surface):
		"""
	    Draw a rect frame and text label for button.

	    ### Args:
	    `surface` : pygame.Surface

	    ### Return:
	    None
	    """
		# Simplification of style variables
		style_vars = ['text_color', 'font_clicked_color', 'font_disabled_color', 'font_highlight_color', 'bg_color',
	                  'bg_clicked_color', 'bg_disabled_color', 'bg_highlight_color', 'border_radius', 'top_left_radius',
	                  'top_right_radius', 'bottom_left_radius', 'bottom_right_radius', 'stroke']
		
		style_values = {var: self.style.get(var, Button.style[var]) for var in style_vars}
		font_color, font_clicked_color, font_disabled_color, font_highlight_color, bg_color, bg_clicked_color, \
	    bg_disabled_color, bg_highlight_color, border_radius, top_left_radius, top_right_radius, bottom_left_radius, \
	    bottom_right_radius, stroke = [style_values[var] for var in style_vars]

	    # Colors
		event_color = font_disabled_color
		bg_event_color = bg_disabled_color

	    # Events
		self.handle_events()
		if self.enabled:
			if self._event['clicked']:
				bg_event_color = bg_clicked_color
				event_color = font_clicked_color
			elif self._event['highlighted']:
				bg_event_color = bg_highlight_color
				event_color = font_highlight_color
			else:
				bg_event_color = bg_color
				event_color = font_color
				
		pg.draw.rect(surface,bg_event_color,self.rect, stroke, border_radius, top_left_radius, top_right_radius, bottom_left_radius, bottom_right_radius)
		font_render = self.font.render(self.text, True, event_color)

	    # Alinear texto en rectangulo
		align = self.style.get('font_align',Button.style['font_align'])
		valign = self.style.get('font_valign',Button.style['font_valign'])
	    # Dibuja la fuente en pantalla
		surface.blit(font_render,widget.Widget.align(self.rect, font_render, align, valign, border_radius=border_radius))

	
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
		"font": "G15",
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
