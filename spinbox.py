#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  spinbox.py
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

class SpinBox:
	""" 
	Create Spin box widget. 
	
	TODO:

	- enable the posibility to increment value based in list items.
	- make that return the value.
	"""

		
	def __init__ (self, color, kmenu, rect, value = 0, step = 1 , min_val = None, max_val = None, **kwargs):
		""" 
		SpinBox constructor.
		
		args:
		---
		color : tuple # RGB values
		kmenu : dict 	# Dictionary of spin box items ???
		rect : pygame.Rect # Used for calculate 2 arrow buttons and rect.
		
		return : None
		"""
		self.color = color
		self.kmenu = kmenu
		self.rect = rect
		
		self.kwargs = kwargs
		if self.kwargs != None:
			self.configure(kwargs)
		
		if isinstance(value, int) or isinstance(value, float):
			self.value = value
			self.step = step
			self.min_val = min_val
			self.max_val = max_val
		elif isinstance(value, list):
			self.value = value
			self.step = step
			self.min_val = 0
			self.max_val = len(self.value) -1
		
		self.left = btn.Button((self.rect[0],self.rect[1],self.rect[2] * 0.2,self.rect[3]),'◀', self.decrease_value)
		self.right = btn.Button((self.rect[0] + self.rect[2] * 0.8, self.rect[1], self.rect[2] * 0.2, self.rect[3]),'▶', self.increase_value)
		
		self.font = pg.font.SysFont('Arial',20)
		
	def draw (self, screen):
		""" 
		Draw in screen the spinbox widget.
		
		args:
		---
		screen : pygame.Surface # Empty canvas for draw widget.
		
		return : None
		"""
		self.box = pg.draw.rect(screen, (0,0,0),(self.rect[0] + self.rect[2] * 0.2, self.rect[1], self.rect[2] * 0.6, self.rect[3]), 0, 5)
		self.left.draw(screen)
		self.right.draw(screen)
		
		
		align_x = self.rect[0]
		align_y = self.rect[1]
		fnt_render = self.font.render(str(round(self.value, 2)),True,(64,64,64),(0,0,0))
		align_x += self.rect[2] // 2 - fnt_render.get_width() // 2
		align_y += self.rect[3] // 2 - fnt_render.get_height() // 2
		
		screen.blit(fnt_render,(align_x , align_y, self.rect[2] * 0.6, self.rect[3]))
		
	def configure (self, kwargs):
		""" 
		Modify with a dict lately the object args.
		
		args:
		---
		kwargs : dict # optional values
		"""
		self.kwargs = {**self.kwargs, **kwargs}
		
		
	
	def increase_value(self):
		"""
		Increase value one point.
		"""
		if isinstance(self.value, int) or isinstance(self.value, float):
			if self.max_val != None:
				if self.value < self.max_val:
					self.value += self.step
			else:
				self.value += self.step

		elif isinstance(self.value, list):
			if self.step < self. max_val:
				self.step += 1
				print(self.value[self.step]) 
	
	def decrease_value(self):
		"""
		Decrease value one point.
		"""
		if isinstance(self.value, int) or isinstance(self.value, float):
			if self.min_val != None:
				if self.min_val < self.value:
					self.value -= self.step
			else:
				self.value -= self.step

		elif isinstance(self.value, list):
			if self.step > self.min_val:
				self.step -= 1
				print(self.value[self.step])

# ------------------------------------------------------- Program Entry
def main(args):
	"""
	Program Entry for test spinbox
	"""
	pg.init()
	root = pg.display.set_mode((600,400))
	
	pg.display.set_caption('Spin Box Class')
	
	_color = (255,0,0)
	_rect = (100,100,200,64)
	
	values = ['Option 1','Option 2', 'Option 3','Option 4']
	
	spinbox = SpinBox(_color,{1,2,3,4},_rect, 0.125, 0.125)
	while 1:
		for event in pg.event.get():
			if event.type == pg.QUIT:
				sys.exit()
		root.fill((35,35,70))
		spinbox.draw(root)
		pg.display.update()
	
	return 0

if __name__ == '__main__':
	import sys
	sys.exit(main(sys.argv))
