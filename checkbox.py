#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  
# ------------------------------------------------------------ Imports
import pygame as pg
import button as btn

# ------------------------------------------------------------ Classes
class CheckBox:
	""" 
	Create a Check box button.
	require button module and pygame.
	
	TODO:
	- Make that return a boolean.
	"""
	style = {
        'font': 'System',
        'font_size': 20,
		'font_align': 'center',
		'font_valign': 'middle',
        'text_color': 'black',
		'check_char': '\u2714',
		'uncheck_char': '\u2716',
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
	
	
	def __init__ (self, rect, text = 'text', state = True, style = None):
		""" 
		Checkbox constructor
		
		args:
		---
		rect: pygame.Rect # rect limits for button
		text: str # string label
		state: bool # initial state
		
		return : None
		"""
		self.rect = rect
		self.text = text # Label is better varible name
		self.state = state
		self.temp_check = not self.state
		self.style = style or CheckBox.style

		self.check = btn.Button(self.rect, self.text, self.change_state, self.style)
		
	def draw (self, screen):
		""" 
		Draw the button checkbox
		args:
		---
		screen : pygame.Surface # Empty canvas to draw button.
		return : None
		"""
		
		if self.state != self.temp_check:
			check_char = self.style.get('check_char',CheckBox.style['check_char'])
			uncheck_char = self.style.get('uncheck_char',CheckBox.style['uncheck_char'])
			self.check.text = f'{check_char} ' if self.state == True else f'{uncheck_char} '
			self.check.text += self.text			
			self.temp_check = self.state
		
		self.check.draw(screen)
		
	def change_state(self):
		"""
		Switch boolean state and modify the label text
		return: None
		"""
		self.state = not self.state
		
		
# ---------------------------------------------------- Program Entry
def main(args):
	"""
	Entry of program to test CheckBox class
	"""
	pg.init()
	root = pg.display.set_mode((600,400))
	
	pg.display.set_caption('Check Box Class')
	
	style = {	
		"font_highlight_color" : (0, 75 , 0), 
		"font_clicked_color" : (0, 75,75), 
		"font_disabled_color" : (0, 0, 75), 
		"bg_disabled_color" : "red",
		"font": "G15",
		"font_align" : "right", 
		"font_valign" : "bottom",
		"border_radius" : 15,
		"check_char" : "X",
		"uncheck_char" : "O",
		}
	
	_rect = pg.Rect(255,30,100,50)
	checkbox = CheckBox(_rect,'Hola', True, style)
	while 1:
		root.fill((35,35,70))
		for event in pg.event.get():
			if event.type == pg.QUIT:
				sys.exit()
				
		checkbox.draw(root)
		print(checkbox.state)
		pg.display.update()
	
	return 0

if __name__ == '__main__':
	import sys
	sys.exit(main(sys.argv))
