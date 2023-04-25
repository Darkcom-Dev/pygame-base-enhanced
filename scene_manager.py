#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  

"""
- Como hacer una clase estatica en python
- Hacer un sistema que carge las escenas desde el archivo de configuracion
- y que evite ser hardcodeado
"""
import scene_joystick_display
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
	scene_map = {
        "scene_home": scene_home.SceneHome,
        "scene_title": scene_joystick_display.SceneJoystickDisplay,
        "scene_credits": scene_credits.SceneCredits,
        "scene_sound_test": scene_sound_test.SceneSoundTest,
        "scene_physics": scene_physics.ScenePhysicsTest
    }
	scn = scene_map.get(scene)
	if scn is not None:
		dcr.change_scene(scn(dcr))
		dcr.loop()
