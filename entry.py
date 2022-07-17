#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  entry.py
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

import pygame as pg

class Entry:
	""" 
	Create a functional Entry Widget with pygame module
	Require import pygame
	
	TODO:
	- Limitate text string length or auto limitate with rect width
	- Hide text with asterisk or other character, neccesary for passwords
	- self.text is real text to get data and self.show_text will be text to show in screen, necesary for passwords
	
	- Create a style set for widgets
	"""
	
	def __init__ (self, rect, color, limit = 40, password = ''):
		""" Class initialiser """
		self.rect = rect
		self.color = color
		self.text = ''
		
		self.limit = limit
		self.password = password # Fillchar
		self.font_size = 20
		self.max_limit = 0
		
		self.font = pg.font.SysFont('Arial',self.font_size)
		
		
	def draw (self, screen):
		""" Function doc """
		pg.draw.rect(screen, self.color, self.rect, 1)
		
		show_text = ''
		# ~ if len(self.text) < self.limit and self.limit > 0:
		if self.password == '':
			if self.font.size(self.text)[0] <= self.rect[2]:
				show_text = self.text[0:self.limit]
			else:
				show_text = self.text[0:self.max_limit]
		else:
			if self.font.size(self.text)[0] <= self.rect[2]:
				show_text = len(self.text[0:self.limit]) * self.password
			else:
				show_text = len(self.text[0:self.max_limit]) * self.password
			
		
		fnt_render = self.font.render(show_text, True, self.color)
		
		
		
		screen.blit(fnt_render,(self.rect[0] + 3, self.rect[1] + 3, self.rect[2] - 10, self.rect[3] - 10))
		
	def input (self, key):
		""" Function doc """
		print(key)
		
		self.max_limit = self.rect[2] // (12)
		
		if key == 97:		self.text += 'A'
		elif key == 98:		self.text += 'B'
		elif key == 99:		self.text += 'C'
		elif key == 100:	self.text += 'D'
		elif key == 101:	self.text += 'E'
		elif key == 102:	self.text += 'F'
		elif key == 103:	self.text += 'G'
		elif key == 104:	self.text += 'H'
		elif key == 105:	self.text += 'I'
		elif key == 106:	self.text += 'J'
		elif key == 107:	self.text += 'K'
		elif key == 108:	self.text += 'L'
		elif key == 109:	self.text += 'M'
		elif key == 110:	self.text += 'N'
		elif key == 111:	self.text += 'O'
		elif key == 112:	self.text += 'P'
		elif key == 113:	self.text += 'Q'
		elif key == 114:	self.text += 'R'
		elif key == 115:	self.text += 'S'
		elif key == 116:	self.text += 'T'
		elif key == 117:	self.text += 'U'
		elif key == 118:	self.text += 'V'
		elif key == 119:	self.text += 'W'
		elif key == 120:	self.text += 'X'
		elif key == 121:	self.text += 'Y'
		elif key == 122:	self.text += 'Z'
		elif key == 32:		self.text += ' '
		elif key == 48:		self.text += '0'
		elif key == 49:		self.text += '1'
		elif key == 50:		self.text += '2'
		elif key == 51:		self.text += '3'
		elif key == 52:		self.text += '4'
		elif key == 53:		self.text += '5'
		elif key == 54:		self.text += '6'
		elif key == 55:		self.text += '7'
		elif key == 56:		self.text += '8'
		elif key == 57:		self.text += '9'
		elif key == 8:		self.text = self.text[0:-1]
		elif key == 13:		self.text += '\n'


def main(args):
	
	pg.init()
	display = pg.display.set_mode((600, 400))
	
	pg.display.set_caption('Entry test class')
	
	_rect = pg.Rect(200,200,200,50)
	test_entry = Entry(_rect, (255,0,0),20,'*')
	
	while 1:
		
		display.fill((13,17,23))
		test_entry.draw(display)
		
		for event in pg.event.get():
			if event.type == pg.QUIT:
				sys.exit()
			if event.type == pg.KEYDOWN:
				test_entry.input(event.key)
				
		pg.display.update()
	
	return 0

if __name__ == '__main__':
	import sys
	sys.exit(main(sys.argv))
