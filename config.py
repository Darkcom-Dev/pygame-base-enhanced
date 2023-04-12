#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  config.py
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

import configparser

config = configparser.ConfigParser()
config.read("config.cfg")

HeaderFont = config.get("Font","HeaderFont")
ParagraphFont = config.get("Font","ParagraphFont")
H1 = config.getint("Font","H1")
H2 = config.getint("Font","H2")
H3 = config.getint("Font","H3")
H4 = config.getint("Font","H4")
H5 = config.getint("Font","H5")
H6 = config.getint("Font","H6")
P1 = config.getint("Font","P1")
P2 = config.getint("Font","P2")
P3 = config.getint("Font","P3")

WIDTH = config.getint("Settings","Width")
HEIGHT = config.getint("Settings","Height")
FrameTicks = config.getint("Settings","FrameTicks")
Caption = config.get("Settings","Caption")
GameIcon = config.get('Settings', 'GameIcon')

# Color
ScreenFillColor = [int(s) for s in config.get("Settings","ScreenFillColor").split(',')]
DefaultColor = [int(s) for s in config.get("Font","DefaultColor").split(',')]
DefaultBackgroundColor = [int(s) for s in config.get("Font","DefaultBackgroundColor").split(',')]
InfoTextPosition = [int(s) for s in config.get("Font","InfoTextPosition").split(',')]
InfoOutlineColor = [int(s) for s in config.get("Font","InfoOutlineColor").split(',')]
HintShadowColor = [int(s) for s in config.get("Font","HintShadowColor").split(',')]
SubEventColor = [int(s) for s in config.get("Font","SubEventColor").split(',')]
ButtonColorLight = [int(s) for s in config.get("Button","ColorLight").split(',')]
ButtonColorDark = [int(s) for s in config.get("Button","ColorDark").split(',')]

# Cursor
CursorSetVisible = config.getint("Cursor","SetVisible")

# Debug
DebugMode = config.getboolean("Debug","DebugMode")

# Directories
AudioDir = config.get("Directories","Audio")
SpritesDir = config.get('Directories','Sprites')
FontsDir = config.get('Directories','Fonts')

# Audio
AudioTest = config.get('Audio','AudioTest')
BgmVolume = config.getfloat('Audio', 'BgmVolume')

# Sprites
Background = config.get('Sprites','Background')
ControllerBackground = config.get('Sprites', 'ControllerBackground')

# UI

# font
font_family = config.get('UI', 'font_family')
font_size = config.getint('UI', 'font_size')

font_normal_color = [int(s) for s in config.get("UI","font_normal_color").split(',')]
font_highlight_color = [int(s) for s in config.get("UI","font_highlight_color").split(',')]
font_clicked_color = [int(s) for s in config.get("UI","font_clicked_color").split(',')]
font_disabled_color = [int(s) for s in config.get("UI","font_disabled_color").split(',')]

# border
border_radius = config.getint('UI', 'border_radius')
border_width = config.getint('UI', 'border_width')
border_top_left_radius = config.getint('UI', 'border_top_left_radius')
border_top_right_radius = config.getint('UI','border_top_right_radius')
border_bottom_left_radius = config.getint('UI', 'border_bottom_left_radius')
border_bottom_right_radius = config.getint('UI', 'border_bottom_right_radius')

border_normal_color = [int(s) for s in config.get("UI","border_normal_color").split(',')]
border_highlight_color = [int(s) for s in config.get("UI","border_highlight_color").split(',')]
border_clicked_color = [int(s) for s in config.get("UI","border_clicked_color").split(',')]
border_disabled_color = [int(s) for s in config.get("UI","border_disabled_color").split(',')]

frame_radius = config.getint('UI', 'frame_radius')
frame_width = config.getint('UI', 'frame_width')

frame_top_left_radius = config.getint('UI', 'frame_top_left_radius')
frame_top_right_radius = config.getint('UI', 'frame_top_right_radius')
frame_bottom_left_radius = config.getint('UI', 'frame_bottom_left_radius')
frame_bottom_right_radius = config.getint('UI', 'frame_bottom_right_radius')

frame_normal_color = [int(s) for s in config.get("UI","frame_normal_color").split(',')]

def set_volume(volume):
	with open('config.cfg','w') as cfg:
		#if volume != BgmVolume:
		config.set('Audio', 'BgmVolume', str(volume))
		config.write(cfg)
