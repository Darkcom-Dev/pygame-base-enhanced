#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Efect_inyection_test.xcf
#  

# ------------------------------------------------------------ Imports
import pygame as pg
import sys

class Offset:
	""" Class doc """
	
	def __init__ (self, rect, position, offset = (0,0),rect_attr = 'c'):
		
		"""
		reference point
		//x,y
		//top = t, left = l, bottom = b, right = r
		topleft = tl, bottomleft = bl, topright = tr, bottomright = br
		midtop = mt, midleft = ml , midbottom = mb, midright = mr
		center = c, centerx = cx, centery = cy
		"""
		self.rect = rect # Esto no es necesario, pero si lo borro: invalid destination position for blit
		self.position = position
		self.offset = offset
		self.rect_attr = rect_attr
		
		position = self.position[0] + self.offset[0], self.position[1] + self.offset[1]
		if self.rect_attr == "tl": rect.topleft = position
		elif self.rect_attr == "bl": rect.bottomleft = position
		elif self.rect_attr == "tr": rect.topright = position
		elif self.rect_attr == "br": rect.bottomright = position
		elif self.rect_attr == "mt": rect.midtop = position
		elif self.rect_attr == "ml": rect.midleft = position
		elif self.rect_attr == "mb": rect.midbottom = position
		elif self.rect_attr == "mr": rect.midright = position
		elif self.rect_attr == "c": rect.center = position
		else: rect.center = position
	
	def get (self):
		""" Function doc """
		
		return self.rect

# ------------------------------------------------------------ Classes
class Chromatic_Aberration:
	""" Class doc """
	
	def __init__ (self, font, text, color = (255,255,255), distance = 10, position = (0,0),rect_attr = 'c'):
		""" Class initialiser """
		self.font = font
		self.text = text
		self.color = color # Esto debe ser extraido de la fuente
		self.antialias = True
		
		self.distance = distance # Propia del efecto
		self.position = position # No se si tenga sentido
		self.rect_attr = rect_attr
		
		
	def update (self,screen):
		""" Function doc """
		# ~ if isinstance(self.font, pg.font):			print('Es un tipo fuente')
		rb_component = [self.color[0],0,0]
		font_render = self.font.render(self.text,self.antialias,rb_component)
		rect_offset = Offset(font_render.get_rect(),self.position,(self.distance,self.distance),self.rect_attr)
		
		screen.blit(font_render, rect_offset)
		
		rb_component = [0,0,self.color[2]]
		font_render = self.font.render(self.text,self.antialias,rb_component)
		rect_offset = Offset(font_render.get_rect(),self.position,(-self.distance,-self.distance),self.rect_attr)
		
		screen.blit(font_render, rect_offset)
		
		font_render = self.font.render(self.text, self.antialias, self.color)
		rect_offset = Offset(font_render.get_rect(), self.position, (0,0), self.rect_attr)
		
		screen.blit(font_render, rect_offset)

# ----------------------------------------------------- Program entry
def main(args):
	
	pg.init()
	root = pg.display.set_mode((600,400))
	root.fill((35,35,70))
	pg.display.set_caption('Effect inyection')
	
	font = pg.font.SysFont('Arial',20)
	efect = Chromatic_Aberration(font, 'Hola mundo', (128,255,255),3,(300,200),'br')
	
	# -------------------------
	# Hay que intentar lograr el mismo efecto con un rectangulo
	
	fnt_rect = pg.Rect(100,100,100,50)
	rectangulo = pg.draw.rect(root,(128,255,255),fnt_rect,3,10)
	
	print(type(rectangulo))
	
	
	
	while 1:
		for event in pg.event.get():
			if event.type == pg.QUIT:
				sys.exit()
				
		efect.update(root)
		pg.display.update()
	return 0

if __name__ == '__main__':
	import sys
	sys.exit(main(sys.argv))
