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

# ------------------------------------------------------------ Classes
class Button():
	def __init__(self,rect, text = 'text', **kwargs):
		self.in_rect = bool()
		self.enabled = True
		self.rect = rect
		
		self.kwargs = kwargs
		
		# normal_color, enabled and out of bounds
		self.normal_color = (170,170,170)
		# highlight_color, enabled and in range of bounds
		self.highlight_color = (100,100,100)
		# clicked color, enabled, in range of bounds and clicked
		self.clicked_color = (170,170,170)
		# disabled color, disabled
		self.disabled_color = (75,75,75)
		# command in string
		self.command = "print('Hola desde button')"
		# text
		self.text = text
		if self.kwargs != None:
			self.configure(self.kwargs)
		
		self._event = {'clicked': False, 'highlighted' : False}
		
		self.font = pg.font.SysFont('Arial',20)
		
		
	def draw(self,screen):
		
		fnt_render = self.font.render(self.text,True,self.disabled_color)
		
		if self.enabled:
			self.pos = pg.mouse.get_pos()
			self.mouse = pg.mouse.get_pressed()
			self.in_width = self.pos[0] > self.rect[0] and self.pos[0] <= self.rect[0] + self.rect[2]
			self.in_height = self.pos[1] > self.rect[1] and self.pos[1] <= self.rect[1] + self.rect[3]
			self.in_rect = self.in_width and self.in_height
			# ~ print(f'events: {self._event}')
			
			if self.mouse == (1,0,0): # Clicked
				if self.in_rect:
					pg.draw.rect(screen,self.clicked_color,self.rect,3,10)
					fnt_render = self.font.render(self.text,True,self.clicked_color)
					if self._event['clicked'] == False:
						exec(self.command)
					self._event['clicked'] = True
					
			else: # Highlight
				
				self._event['clicked'] = False
				if self.in_rect:
					pg.draw.rect(screen,self.highlight_color,self.rect,3,10)
					fnt_render = self.font.render(self.text,True,self.highlight_color)
					self._event['highlighted'] = True
				else:
					pg.draw.rect(screen,self.normal_color,self.rect,3,10)
					fnt_render = self.font.render(self.text,True,self.normal_color)
					self._event['highlighted'] = False
		else:
			pg.draw.rect(screen,self.disabled_color,self.rect,3,10)
			fnt_render = self.font.render(self.text,True,self.disabled_color)
			
		screen.blit(fnt_render,(self.rect[0] + 10, self.rect[1] + 10, self.rect[2] - 10, self.rect[3] - 10))
			
	def configure (self, kwargs):
		""" Function doc """
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
		elif 'command' in self.kwargs:
			self.command = self.kwargs['command']
		elif 'text' in self.kwargs:
			self.text = self.kwargs['text']
		else:
			pass
# -------------------------------------------------..... Program entry

def holis ():
	""" Function doc """
	print('holis')

def main ():
	""" Entry function program """
	
	pg.init()
	display = pg.display.set_mode((600, 400))
	display.fill((13,17,23))
	pg.display.set_caption('Button test class')
	
	rect = pg.Rect(200,280,150,30)

	test_button = Button(rect,'Hola mundo',command = "holis()")
	test_button.normal_color = (125, 0, 0)
	print(test_button.command)
	test_button.configure({"highlight_color" : (75, 0 , 0), "clicked_color" : (0, 75,75), "disabled_color" : (0, 0, 75)})

	
	while 1:
		
		test_button.draw(display)
		
		for event in pg.event.get():
			if event.type == pg.QUIT:
				sys.exit()
		pg.display.update()
	return 0


if __name__ == '__main__':
	main()
