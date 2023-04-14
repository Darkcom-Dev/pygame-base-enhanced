#!/usr/bin/env python
# -*- coding: utf-8 -*-
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

		
	def __init__ (self, color:pg.Color, rect:pg.Rect, value:int = 0, step:int = 1 , min_val = None, max_val = None, **kwargs):
		""" 
		SpinBox constructor.
		
		args:
		---
		color : tuple # RGB values
		
		rect : pygame.Rect # Used for calculate 2 arrow buttons and rect.
		value : int, float or list # default initial value.
		step : float or int # works like a default index if value is a dict.
		min_val : int # Minimum value to limit the decrement, if value is a list default value is 0.
		max_val : int # Maximum value to limit the increment, if value is a list default value is the maximum item count in list.
		kwargs : dict # Optional values.
		
		return : None
		"""
		self.color = color
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
		
		self.left = btn.Button((self.rect[0],self.rect[1],32 ,self.rect[3]),'◀', self.decrease_value)
		self.right = btn.Button((self.rect[0] + self.rect[2] -32, self.rect[1], 32, self.rect[3]),'▶', self.increase_value)
		
		self.font = pg.font.SysFont('Arial',20)
		
	def draw (self, screen:pg.Surface):
		""" 
		Draw in screen the spinbox widget.
		
		args:
		---
		param screen : Empty canvas for draw widget.
		
		return : None
		"""
		self.box = pg.draw.rect(screen, self.color,(self.rect[0] + 32, self.rect[1], self.rect[2] -64, self.rect[3]), 0, 5)
		self.left.draw(screen)
		self.right.draw(screen)
		
		
		align_x = self.rect[0]
		align_y = self.rect[1]
		fnt_content =''
		if isinstance(self.value, int) or isinstance(self.value, float):
			fnt_content = str(round(self.value, 2))
		elif isinstance(self.value, list):
			fnt_content = self.value[self.step]
		fnt_render = self.font.render(fnt_content,True,(64,64,64))
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
	_rect = (100,100,300,32)
	values = ['800x600', '1024x768', '1366x768', '1280x720']
	spinbox = SpinBox(_color, _rect, values, 0)
	
	_color2 = (0,255,0)
	_rect2 = (100,164,300,32)
	values2 = ['Easy', 'Normal', 'Hard', 'Insane']
	spinbox2 = SpinBox(_color2, _rect2, values2, 1)
	
	while 1:
		for event in pg.event.get():
			if event.type == pg.QUIT:
				sys.exit()
		root.fill((35,35,70))
		spinbox.draw(root)
		spinbox2.draw(root)
		pg.display.update()
	
	return 0

if __name__ == '__main__':
	import sys
	sys.exit(main(sys.argv))
