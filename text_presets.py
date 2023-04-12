#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  text_presets.py
#  
#  Copyright 2021 Braulio Madrid <darkcom@darkcom-X455LD>
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

import font
#import math
#import pygame
import config as cfg
#import random

"""
Text presets, es solo una clase que usa textos predeterminados.
la intension es enviar mensajes por pantalla, pero sin provocar
duplicacion de texto o superposicion de texto para evitar
caidas de rendimiento.

Me veo tentado de usar un singleton, pero trataré de evitarlo
mejor usar algo que pregunte el estado actual del mensaje.

Efectos de posicion:
--------------------
- Shake
- Deslizamiento


"""
	# Es necesario tener una fuente de respaldo del sistema si todo falla
	# TODO: En el futuro hacer que las fuentes se carguen de un archivo de configuracion
	# TODO: Cargar el ancho y el alto desde un archivo de configuracion
	# TODO: En el futuro Agregar un sistema de animacion de textos.

# Cursor text = en el centro de la pantalla o en la posicion del cursor (Skyrim)

# menu Acciones rapidas - midleft (width * 0.1, heitgh/2)
# menu Respuestas rapidas - respuestas del jugador a preguntas hechas por los npc = midright (width * 0.9, height/2)	


center = cfg.WIDTH/2
middle = cfg.HEIGHT/2

# History text = texto de historia o informacion del lore en el loading (Skyrim)
history_text = font.Font(cfg.ParagraphFont,cfg.P1,"history","br",(cfg.WIDTH * 0.9, cfg.HEIGHT * 0.9),cfg.DefaultColor)
#history_text.draw(screen)

info_text = font.Font(cfg.ParagraphFont, cfg.P2,"info","tl",cfg.InfoTextPosition,cfg.DefaultColor,cfg.InfoOutlineColor)
#info_text.draw(screen,"outline",distance = 2)

caption_text = font.Font(cfg.HeaderFont, cfg.H6,"caption","mb",(center,cfg.HEIGHT * 0.8),cfg.DefaultColor,cfg.DefaultBackgroundColor,False)
#caption_text.draw(screen,"caption")

# Hint text = info de acciones asociadas teclas midbottom (width/2, Height * 0.9)
hint_text = font.Font(cfg.HeaderFont, cfg.P2, "hint","mb",(center, cfg.HEIGHT * 0.9),cfg.DefaultColor,cfg.HintShadowColor)
#hint_text.draw(screen, "shadow", 3)

# SubEvent text = info de misiones, pero de eventos repetitivos  (width / 2, Height * 0.5) texto mas pequeño
subevent_text = font.Font(cfg.ParagraphFont, cfg.H5,"sub event","c",(center,cfg.HEIGHT * 0.4),cfg.SubEventColor)
#subevent_text.draw(screen,"chromatic",3) # pygame.time.get_ticks()/1000)*3

# Event text = info de inicio de misiones o lugares descubiertos o subidas de nivel center (width / 2, Height * 0.4)
event_text = font.Font(cfg.ParagraphFont,cfg.H4,"event","c",(center,middle),cfg.SubEventColor,cfg.DefaultColor)
#position = (math.sin(pygame.time.get_ticks()/1000) * cfg.WIDTH/4 + cfg.WIDTH/2, random.randrange((cfg.HEIGHT/2) -2,(cfg.HEIGHT/2) +2))
#event_text.draw(screen,"chromatic",2)




