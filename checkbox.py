#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  checkbox.py
#  
#  Copyright 2022 Braulio Madrid <darkcom@darkcom-X455LD>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
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
	
	def __init__ (self, rect, text = 'text', state = True):
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
				
		self.check = btn.Button(self.rect, self.text, self.change_state)
		
	def draw (self, screen):
		""" 
		Draw the button checkbox
		args:
		---
		screen : pygame.Surface # Empty canvas to draw button.
		return : None
		"""
		
		if self.state != self.temp_check:
			if self.state == True:
				self.check.text = '■ '+ self.text 
			else:
				self.check.text = '□ '+ self.text
			
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
	
	checkbox = CheckBox((255,10,100,32),'Hola', True)
	while 1:
		root.fill((35,35,70))
		for event in pg.event.get():
			if event.type == pg.QUIT:
				sys.exit()
				
		checkbox.draw(root)
		pg.display.update()
	
	return 0

if __name__ == '__main__':
	import sys
	sys.exit(main(sys.argv))
