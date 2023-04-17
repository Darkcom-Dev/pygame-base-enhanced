#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# ------------------------------------------------------------ Imports
import pygame as pg
import button as btn
import widget
# ------------------------------------------------------------ Classes

class SpinBox(widget.Widget):
	""" 
	Create Spin box widget. 
	
	TODO:
	- enable the posibility to increment value based in list items.
	- make that return the value.
	- hacer que los estilos funcionen correctamente.
	"""
			
	def __init__ (self, rect:pg.Rect, value:int = 0, range:range = None, style = None):
		""" 
		SpinBox constructor.
		
		### args:
		---
		color : tuple # RGB values
		
		rect : pygame.Rect # Used for calculate 2 arrow buttons and rect.
		value : int, float or list # default initial value.
		step : float or int # works like a default index if value is a dict.
		range : range # works like a default index if value is a dict.
		
		### returns

		return : None
		"""
		super().__init__(rect,style)
		# self.style = style or SpinBox.style
		
		if isinstance(value, int) or isinstance(value, float):
			self.value = value
			self.range = range if range != None else 1
			
		elif isinstance(value, list):
			self.value = value
			self.step = 1
			self.min_val = 0
			self.max_val = len(self.value) -1
		
		left_rect = pg.Rect((self.rect[0],self.rect[1],32 ,self.rect[3]))
		right_rect = pg.Rect((self.rect[0] + self.rect[2] -32, self.rect[1], 32, self.rect[3]))
		
		self.left = btn.Button(left_rect,self.decrement_char, self.decrease_value)
		self.right = btn.Button(right_rect,self.increment_char, self.increase_value)
		
		self.font = pg.font.SysFont(self.style['font_family'],20)
		
	def draw (self, surface:pg.Surface):
		""" 
		Draw in screen the spinbox widget.
		
		args:
		---
		param screen : Empty canvas for draw widget.
		
		return : None
		"""
		box_rect = pg.Rect((self.rect[0] + 32, self.rect[1], self.rect[2] -64, self.rect[3]))
		self.box = pg.draw.rect(surface, self.font_color,box_rect, 0, 5)
		self.left.draw(surface)
		self.right.draw(surface)		
		
		text =''
		if isinstance(self.value, int) or isinstance(self.value, float):
			text = str(round(self.value, 2))
		elif isinstance(self.value, list):
			text = self.value[self.step]

		font_render = self.font.render(text,True,(64,64,64))

		align_x = self.rect[0]
		align_y = self.rect[1]
		align_x += self.rect[2] // 2 - font_render.get_width() // 2
		align_y += self.rect[3] // 2 - font_render.get_height() // 2
		
		surface_rect = pg.Rect(align_x, align_y, self.rect[2] * 0.6, self.rect[3] * 0.6)
		surface.blit(font_render,surface_rect)		
	
	def increase_value(self):
		"""
		Increase value one point.
		"""
		if isinstance(self.value, int) or isinstance(self.value, float):
			if self.range != None:
				if self.value < self.range.stop:
					self.value += self.range.step
			else:
				self.value += self.range

		elif isinstance(self.value, list):
			if self.step < self. max_val:
				self.step += 1
				print(self.value[self.step]) 
	
	def decrease_value(self):
		"""
		Decrease value one point.
		"""
		if isinstance(self.value, int) or isinstance(self.value, float):
			if self.range != None:
				if self.range.start < self.value:
					self.value -= self.range.step
			else:
				self.value -= self.range

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
	
	_style = {
		'increment_char': '>>',
		'decrement_char': '<<',
		'font_family': 'G15',
		'font_size': 20
	}
	_rect = pg.Rect(100,100,300,32)
	values = ['800x600', '1024x768', '1366x768', '1280x720']
	spinbox = SpinBox(_rect, values, style =_style)
	
	_rect2 = pg.Rect(100,164,300,32)
	values2 = ['Easy', 'Normal', 'Hard', 'Insane']
	spinbox2 = SpinBox(_rect2, values2, style =_style)

	_rect3 = pg.Rect(100,228,300,32)
	spinbox3 = SpinBox(_rect3, 1, range(1,100,3), style =_style)
	
	while 1:
		for event in pg.event.get():
			if event.type == pg.QUIT:
				sys.exit()
		root.fill((35,35,70))
		spinbox.draw(root)
		spinbox2.draw(root)
		spinbox3.draw(root)
		pg.display.update()
	
	return 0

if __name__ == '__main__':
	import sys
	sys.exit(main(sys.argv))
