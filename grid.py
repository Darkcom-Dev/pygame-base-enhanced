#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  grid.py
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

class Grid:
	""" Class doc """
	
	def __init__ (self, surface, color, size):
		""" Class initialiser """
		self.size = size
		
		self.surface = surface
		self.color = color
		
		length_x = self.surface.get_width() // self.size
		length_y = self.surface.get_height() // self.size
		
		for x in range(1,length_x + 1):
			pg.draw.aaline(self.surface, self.color, (x * self.size, 0), (x * self.size, self.surface.get_height())) # Verticals
		for y in range(1,length_y + 1):
			pg.draw.aaline(self.surface, self.color, (0, y * self.size), (self.surface.get_width(), y * self.size)) # Horizontals
		

def main(args):
	pg.init()
	display = pg.display.set_mode((600, 400))
	display.fill((13,17,23))
	pg.display.set_caption('Grid test class')
	
	grid = Grid(display, (32,16,64), 64)
	
	while 1:
		for event in pg.event.get():
			if event.type == pg.QUIT:
				sys.exit()
				
		# ~ spinbox.draw(root)
		pg.display.update()
	return 0

if __name__ == '__main__':
	import sys
	sys.exit(main(sys.argv))
