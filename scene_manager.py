#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  scene_manager.py
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

"""
- Como hacer una clase estatica en python
- Hacer un sistema que carge las escenas desde el archivo de configuracion
- y que evite ser hardcodeado
"""
import scene_title
import scene_home
import scene_credits
import scene_sound_test
import scene_physics
import director

def change_scene(scene):
	"""
	Cambia la escena del juego
	Prarameters
	-----------
	scene : str # Escena a cambiar.
	"""
	dcr = director.Director()
	scn = None
	if scene == "scene_home":
		scn = scene_home.SceneHome(dcr)
	elif scene == "scene_title":
		scn = scene_title.SceneTitle(dcr)
	elif scene == "scene_credits":
		scn = scene_credits.SceneCredits(dcr)
	elif scene == "scene_sound_test":
		scn = scene_sound_test.SceneSoundTest(dcr)
	elif scene == "scene_physics":
		scn = scene_physics.ScenePhysicsTest(dcr)
	dcr.change_scene(scn)
	dcr.loop()
