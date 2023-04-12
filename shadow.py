#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  shadow.py
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


def rect (surface, color,rect,distance, shadow_color,
			width = 0, border_radius = 0,border_top_left_radius = 0, 
			border_top_right_radius = 0, border_bottom_left_radius = 0, 
			border_bottom_right_radius = 0):
	""" Function doc """
	
	shadow_rect = pg.Rect(rect.x + distance, rect.y + distance, rect.w, rect.h)
	
	pg.draw.rect(surface,shadow_color,shadow_rect,
				width, border_radius,
				border_top_left_radius, border_top_right_radius,
				border_bottom_left_radius, border_bottom_right_radius)
				
	return pg.draw.rect(surface,color,rect,
				width,border_radius,
				border_top_left_radius,border_top_right_radius,
				border_bottom_left_radius, border_bottom_right_radius)
	
def polygon (surface, color,points,distance, shadow_color, width = 0):
	""" Function doc """
	
	shadow_points = []
	for point in points:
		shadow_points.append((point[0] + distance, point[1] + distance))
	
	pg.draw.polygon(surface,shadow_color,shadow_points, width)

	return pg.draw.polygon(surface,color,points, width)

def circle (surface, color,center,radius,distance, shadow_color,
			width = 0, draw_top_left = False, draw_top_right = False, 
			draw_bottom_left = False, draw_bottom_right = False):
	""" Function doc """
	shadow_center = (center[0] + distance, center[1] + distance)
	
	pg.draw.circle(surface,shadow_color,shadow_center, radius,
				width, draw_top_left, draw_top_right,
				draw_bottom_left, draw_bottom_right)
				
	return pg.draw.circle(surface,color,center, radius,
				width, draw_top_left, draw_top_right,
				draw_bottom_left, draw_bottom_right)

def ellipse (surface, color,rect,distance, shadow_color,
			width = 0):
	""" Function doc """
	shadow_rect = pg.Rect(rect.x + distance, rect.y + distance, rect.w, rect.h)
	pg.draw.ellipse(surface,shadow_color,shadow_rect, width)
				
	return pg.draw.ellipse(surface,color,rect, width)
	
def arc (surface, color,rect, start_angle, stop_angle, distance, shadow_color, width = 0):
	""" Function doc """
	shadow_rect = pg.Rect(rect.x + distance, rect.y + distance, rect.w, rect.h)

	pg.draw.arc(surface,shadow_color,shadow_rect, start_angle, stop_angle, width)
				
	return pg.draw.arc(surface,color,rect, start_angle, stop_angle, width)

def line (surface, color, start_pos, end_pos, distance, shadow_color, width = 0):
	""" Function doc """
	shadow_start_pos = (start_pos[0] + distance, start_pos[1] + distance)
	shadow_end_pos = (end_pos[0] + distance, end_pos[1] + distance)
	
	pg.draw.line(surface,shadow_color, shadow_start_pos, shadow_end_pos, width)
				
	return pg.draw.line(surface,color, start_pos, end_pos, width)

def lines (surface, color, close, points, distance, shadow_color, width = 0):
	""" Function doc """
	shadow_points = []
	for point in points:
		shadow_points.append((point[0] + distance, point[1] + distance))

	pg.draw.lines(surface,shadow_color, close, shadow_points, width)
				
	return pg.draw.lines(surface,color, close, points, width)

def aalines (surface, color, close, points, distance, shadow_color, width = 0):
	""" Function doc """
	shadow_points = []
	for point in points:
		shadow_points.append((point[0] + distance, point[1] + distance))

	pg.draw.aalines(surface,shadow_color, close, shadow_points, width)
				
	return pg.draw.aalines(surface,color, close, points, width)

def aaline (surface, color, start_pos, end_pos, distance, shadow_color, width = 0):
	""" Function doc """
	
	shadow_start_pos = (start_pos[0] + distance, start_pos[1] + distance)
	shadow_end_pos = (end_pos[0] + distance, end_pos[1] + distance)

	pg.draw.aaline(surface,shadow_color, shadow_start_pos, shadow_end_pos, width)
				
	return pg.draw.aaline(surface,color, start_pos, end_pos, width)

def main(args):
	pg.init()
	root = pg.display.set_mode((600,400))
	root.fill((35,35,70))
	pg.display.set_caption('Chormatic Abrerration Draw')
	
	fnt_rect = pg.Rect(100,100,100,50)
	rectangulo = rect(root,(128,255,255),fnt_rect,3,(128,128,128),3,10)
	
	poligon_points = [(10,30),(50,240),(200,200),(123,240),(120,180)]
	poligon = polygon(root,(255,128,128),poligon_points,3,(128,128,128),3)
	
	_circle = circle(root,(128,128,255),(300,200),100,3,(128,128,128),3)
	
	ellipse_rect = pg.Rect(200,200,100,50)
	_ellipse = ellipse(root,(128,255,128),ellipse_rect,3,(128,128,128),3)
	
	arc_rect = pg.Rect(323,200,120,180)
	_arc = arc(root,(64,128,128),arc_rect,0,3.14,3,(128,128,128),3)
	
	_line = line(root,(128,64,255),(320,240),(0,0),3,(128,128,128),3)
	
	_aaline = aaline(root,(128,64,255),(345,240),(15,0),3,(128,128,128),3)
	
	lines_points = [(30,10),(250,40),(400,200),(240,120),(180,120)]
	_lines = lines(root,(128,64,255),False,lines_points,3,(128,128,128),3)
	
	aalines_points = [(50,30),(270,60),(420,220),(260,140),(200,140)]
	_aalines = aalines(root,(128,64,255),False,aalines_points,3,(128,128,128),3)
	
	while 1:
		for event in pg.event.get():
			if event.type == pg.QUIT:
				sys.exit()
				
		pg.display.update()
	return 0

if __name__ == '__main__':
	import sys
	sys.exit(main(sys.argv))
