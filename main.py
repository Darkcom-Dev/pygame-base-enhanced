#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Módulos
import pygame
import director
from scene_manager import change_scene

"""
Lo primero es entender como es la estructura de clases

				main.py
				- main
					|
					|
scene_home(scene)<--|------> Director
	- __init__				- __init__
	- on_update				- loop
	- on_event				- change_scene
	- on_draw				- quit
		^
		|
		|
	interfaz_scene
	- __init__
	- on_update
	- on_event
	- on_draw
"""

def main():
	change_scene("scene_home")

if __name__ == '__main__':
	pygame.init()
	main()
