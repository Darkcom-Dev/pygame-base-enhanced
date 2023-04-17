#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  
# ------------------------------------------------------------ Imports
import pygame as pg
import button as btn
import widget

# ------------------------------------------------------------ Classes
class CheckBox(widget.Widget):
	""" 
	Create a Check box button.
	require button module and pygame.
	
	TODO:
	- Make that return a boolean.
	"""
		
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

		super().__init__(rect, text, style)
	
		self.state = state
		self.temp_check = not self.state
		
		self.check = btn.Button(self.rect, self.text, self.change_state, self.style)
		
	def draw (self, surface):
		""" 
		Draw the button checkbox
		args:
		---
		surface : pygame.Surface # Empty canvas to draw button.
		return : None
		"""
		
		if self.state != self.temp_check:
						
			self.check.text = f'{self.check_char} ' if self.state == True else f'{self.uncheck_char} '
			self.check.text += self.text			
			self.temp_check = self.state
		
		self.check.draw(surface)
		
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
		"font_family": "G15",
		"font_align" : "right", 
		"font_valign" : "bottom",
		"border_radius" : 15,
		"check_char" : "X",
		"uncheck_char" : "O",
		}
	
	_rect = pg.Rect(255,30,100,50)
	checkbox = CheckBox(_rect,'Hola', state=True, style=style)
	while 1:
		root.fill((35,35,70))
		for event in pg.event.get():
			if event.type == pg.QUIT:
				sys.exit()
				
		checkbox.draw(root)
		#print(checkbox.state)
		pg.display.update()
	
	return 0

if __name__ == '__main__':
	import sys
	sys.exit(main(sys.argv))
