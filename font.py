#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  text_behaviour.py
#  
#  Copyright 2021 Braulio Madrid <darkcom@darkcom-X455LD>
#  
#  
#  

import sys
import pygame as pg
import config as cfg

"""
estilos fijos
----------------
Encabezado = Jura
H1 = 60
H2 = 48
H3 = 40
H4 = 32
H5 = 24
H6 = 20
Parrafo = Iosevka
P1 = 16
P2 = 14
P3 = 12
	
"""


class Font():
	def __init__(self,font = 'Arial',size = 20, text = 'Text',rect_attr = 'c',position = (0,0), color = (255,255,255), background_color = None, antialias = True, **kwargs):
		"""
		Parameters
		----------------
		screen
		font : str	# ttf SystemFont - Tipografia de la fuente con la que se renderiará el texto
		size : int # Tamaño de la fuente con la que se renderizará el texto
		text : str # Texto a renderizar
		antialiasing : bool # Suavizado antialias, marcar Falso para mejor rendimiento.
		color : tuple(r, g, b) # Color de la fuente.
		background_color: tuple(r, b, g) # Color de los efectos.
		rect_attr : str # Punto de referencia del rectangulo de la fuente (funcion _set_offset para mas informacion)
		position : tuple(x,y) # Posicion en la que se ubicará el rectangulo.
		"""
		self._screen = None
		self._font = font
		
		self._size = size
		self._text = text
		self._antialias = antialias
		self._color = color
		self._background_color = background_color
		self._rect_attr = rect_attr	# Mejorar a futuro el nombre de la variable
		self._position = position
		
		self.kwargs = kwargs
		
		if self.kwargs != None:
			self.configure(self.kwargs)
		
	def configure (self,kwargs):
		
		self.kwargs = {**kwargs, **self.kwargs}
		
		""" Function doc """
		if 'font' in self.kwargs:
			self._font = self.kwargs['font']
		elif 'size' in self.kwargs:
			self._size = self.kwargs['size']
		elif 'antialias' in self.kwargs:
			self._antialias = self.kwargs['antialias']
		elif 'color' in self.kwargs:
			self._color = self.kwargs['color']
		elif 'background_color' in self.kwargs:
			self._background_color = self.kwargs['background_color']
		elif 'FG' in self.kwargs:
			self._color = self.kwargs['FG']
		elif 'BG' in self.kwargs:
			self._background_color = self.kwargs['BG']
		elif 'rect_attr' in self.kwargs:
			self._rect_attr = self.kwargs['rect_attr']
		elif 'position' in self.kwargs:
			self._position = self.kwargs['position']
		else:
			# ~ ['font','size','antialias','color','FG','background_color','BG','rect_attr','position']
			# ~ print(f'No existe el atributo{self.kwargs.get_key()}') # Encontrar el atributo no existente
			pass
		
	@property
	def screen(self):
		return self._screen
		
	@property
	def text(self):
		return self._text
		
	@text.setter
	def text(self, text):
		# TODO: Limitar el tamaño de los textos y asignar
		self._text = text
	
	@property
	def font(self):
		return self._font
	
	@property
	def size(self):
		return self._size
	
	@property
	def antialias(self):
		return self._antialias

	@property
	def color(self):
		return self._color
		
	@color.setter
	def color(self, color):
		# TODO: limitar los valores del color
		self._color = color

	@property
	def background_color(self):
		return self._background_color

	@background_color.setter
	def background_color(self, background_color):
		# TODO: limitar los valores del color
		
		self._background_color = background_color

	@property
	def rect_attr(self):
		return self._rect_attr

	@property
	def position(self):
		return self._position

	@position.setter
	def position(self, position):
		self._position = position

	def _set_offset(self,rect,offset = (0,0)):
		"""
		reference point
		//x,y
		//top = t, left = l, bottom = b, right = r
		topleft = tl, bottomleft = bl, topright = tr, bottomright = br
		midtop = mt, midleft = ml , midbottom = mb, midright = mr
		center = c, centerx = cx, centery = cy
		"""
		position = self.position[0] + offset[0],self.position[1] + offset[1]
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
		return rect
		
	def __str__(self):
		return f'Font: {self.font}, text: {self.text}, pos: {self.position}'
	
	def __del__(self):
		if cfg.DebugMode:
			print(f'Font: {self.font}, text: {self.text}, pos: {self.position}, Fue eliminado')
		else:
			pass
	
	def draw(self,screen,effect = "default",distance = 0):
		"""
		Parameters:
		-----------
		effect:
		--------
		- Chromatic Aberration (distance) = "chromatic" # or "-c"
		- Outline (distance, fx_color) = "outline" # or "-o"
		- Shadow (distance, fx_color) = "shadow" # or "-s"
		- Caption (fx_color) = "caption" # or "-b"
		- Default = "default" or None
		distance: int # Distance in pixels for effect from original position
		
		"""
		font = pg.font.SysFont(self.font,self.size)
		
		if effect == "shadow":
			text_render_sh = font.render(self.text,self.antialias,self.background_color,None)
			t_rect_sh = self._set_offset(text_render_sh.get_rect(),(distance,distance))
						
			screen.blit(text_render_sh, t_rect_sh)
		elif effect == "chromatic":
			rb_component = [self.color[0],0,0]
			text_render_rb = font.render(self.text,self.antialias,rb_component,None)
			t_rect_rb = self._set_offset(text_render_rb.get_rect(),(distance,distance))
			
			screen.blit(text_render_rb, t_rect_rb)
			
			rb_component = [0,0,self.color[2]]
			text_render_rb = font.render(self.text,self.antialias,rb_component,None)
			t_rect_rb = self._set_offset(text_render_rb.get_rect(),(-distance,-distance))
			
			screen.blit(text_render_rb, t_rect_rb)
		elif effect == "outline":
			
			text_render_tl = font.render(self.text,self.antialias,self.background_color,None)
			t_rect_tl = self._set_offset(text_render_tl.get_rect(),(-distance,-distance))
			screen.blit(text_render_tl, t_rect_tl)
			
			t_rect_tl = self._set_offset(text_render_tl.get_rect(),(distance,-distance))
			screen.blit(text_render_tl, t_rect_tl)
						
			t_rect_tl = self._set_offset(text_render_tl.get_rect(),(distance,distance))
			screen.blit(text_render_tl, t_rect_tl)
			
			t_rect_tl = self._set_offset(text_render_tl.get_rect(),(-distance,distance))
			screen.blit(text_render_tl, t_rect_tl)
		
		
		text_render = None
		if effect == "caption":
			text_render = font.render(self.text,False,self._color,self._background_color)
		else:
			text_render = font.render(self.text,self.antialias,self._color)
		t_rect = self._set_offset(text_render.get_rect())
				
		screen.blit(text_render, t_rect)


def main():
	
	pg.init()
	screen = pg.display.set_mode((480, 320))
	screen.fill((13,17,23))
	
	print("Mensaje desde la clase font".center(30,'-'))
	print('Creacion de fuente'.center(30,'-'))
	newFont = Font('Arial',20, position = (240,160),rect_attr = 'br', text = 'Hola mundo') # font = "Arial", size = 20, text = "Hola", rect_attr = "br",position = (240,160)
	newFont.configure({'FG' : (255,0,0)})
	# ~ print('Identificacion de clase'.center(30,'_'))
	# ~ print(newFont)
	# ~ print('Eliminacion de objeto'.center(30,'-'))
	# ~ del newFont
	
	while 1:
		
		for event in pg.event.get():
			if event.type == pg.QUIT:
				sys.exit()
		newFont.draw(screen,'default',20)
		pg.display.update()

if __name__ == '__main__':
	main()
