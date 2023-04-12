#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  scene_credits.py
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
import scene
import font, pygame
import config as cfg
import configparser

class SceneCredits(scene.Scene):

	config = configparser.ConfigParser()
	config.read("credits.cfg")

	#Credits
	GameLevelDesign = config.get("Credits",'GameLevelDesign').split(',')
	LevelArtist = config.get("Credits",'LevelArtist').split(',')
	Programmers = config.get("Credits",'Programmers').split(',')
	Animators = config.get("Credits",'Animators').split(',')
	MotionCapture = config.get("Credits",'MotionCapture').split(',')
	Modeling = config.get('Credits','Modeling').split(',')
	SpecialEffects = config.get("Credits",'SpecialEffects').split(',')
	CharacterDesign = config.get("Credits",'CharacterDesign').split(',')
	FrontEnd = config.get("Credits",'FrontEnd').split(',')
	ExecutiveProducer = config.get("Credits",'ExecutiveProducer').split(',')
	Producer = config.get("Credits",'Producer').split(',')
	Director = config.get("Credits",'Director').split(',')
	ArtDirector = config.get("Credits",'ArtDirector').split(',')
	MusicDirector = config.get("Credits",'MusicDirector').split(',')
	TechnicalDirector = config.get("Credits",'TechnicalDirector').split(',')
	Sound = config.get("Credits",'Sound').split(',')
	SoundProgrammers = config.get("Credits",'SoundProgrammers').split(',')
	SessionMusicians = config.get("Credits",'SessionMusicians').split(',')
	Writers = config.get("Credits",'Writers').split(',')
	VoiceOver = config.get("Credits",'VoiceOver').split(',')
	QualityAssurance = config.get("Credits",'QualityAssurance').split(',')
	AditionalQA = config.get("Credits",'AditionalQA').split(',')
	TestingSupervisor = config.get("Credits",'TestingSupervisor').split(',')
	Publisher = config.get("Credits",'Publisher').split(',')
	ComercialDirector = config.get("Credits",'ComercialDirector').split(',')
	ProductAnalisis = config.get("Credits",'ProductAnalisis').split(',')
	SpecialThanks = config.get("Credits",'SpecialThanks').split(',')

	def __init__(self, director):
		print("Hola desde Scene Credits")
		# Producer
		self.dir = director
		self.velocity = -1
		y_position = 400

		

		level_design, y_position = SceneCredits._credit_group_data(y_position,'Game level design',30,SceneCredits.GameLevelDesign,20,30)
		level_artist, y_position = SceneCredits._credit_group_data(y_position,'Level Artist',30,SceneCredits.LevelArtist,20,30)
		programmers, y_position = SceneCredits._credit_group_data(y_position,'Programmers',30,SceneCredits.Programmers,20,30)
		animators, y_position = SceneCredits._credit_group_data(y_position,'Animators',30,SceneCredits.Animators,20,30)
		motion_capture, y_position = SceneCredits._credit_group_data(y_position,'Motion capture',30,SceneCredits.MotionCapture,20,30)
		special_effecs, y_position = SceneCredits._credit_group_data(y_position,'Special Effects',30,SceneCredits.SpecialEffects,20,30)
		character_design, y_position = SceneCredits._credit_group_data(y_position,'Character Design',30,SceneCredits.CharacterDesign,20,30)
		modeling, y_position = SceneCredits._credit_group_data(y_position,'Modeling',30,SceneCredits.Modeling,20,30)
		front_end, y_position = SceneCredits._credit_group_data(y_position,'Front End',30,SceneCredits.FrontEnd,20,30)
		executive_producer, y_position = SceneCredits._credit_group_data(y_position,'Executive Producer',30,SceneCredits.ExecutiveProducer,20,30)
		producer, y_position = SceneCredits._credit_group_data(y_position,'Producer',30,SceneCredits.Producer,20,30)
		director, y_position = SceneCredits._credit_group_data(y_position,'Director',30,SceneCredits.Director,20,30)
		art_director, y_position = SceneCredits._credit_group_data(y_position,'Art director',30,SceneCredits.ArtDirector,20,30)
		music_director, y_position = SceneCredits._credit_group_data(y_position,'Music director',30,SceneCredits.MusicDirector,20,30)
		technical_director, y_position = SceneCredits._credit_group_data(y_position,'Technical director',30,SceneCredits.TechnicalDirector,20,30)
		sound, y_position = SceneCredits._credit_group_data(y_position,'Sound',30,SceneCredits.Sound,20,30)
		sound_programmers, y_position = SceneCredits._credit_group_data(y_position,'Sound programmers',30,SceneCredits.SoundProgrammers,20,30)
		session_musicians, y_position = SceneCredits._credit_group_data(y_position,'Session musicians',30,SceneCredits.SessionMusicians,20,30)
		writers, y_position = SceneCredits._credit_group_data(y_position,'Writers',30,SceneCredits.Writers,20,30)
		voice_over, y_position = SceneCredits._credit_group_data(y_position,'Voice over',30,SceneCredits.VoiceOver,20,30)
		quality_assurance, y_position = SceneCredits._credit_group_data(y_position,'Quality assurance',30,SceneCredits.QualityAssurance,20,30)
		aditional_QA, y_position = SceneCredits._credit_group_data(y_position,'Aditional QA',30,SceneCredits.AditionalQA,20,30)
		testing_supervisor, y_position = SceneCredits._credit_group_data(y_position,'Testing supervisor',30,SceneCredits.TestingSupervisor,20,30)
		publisher, y_position = SceneCredits._credit_group_data(y_position,'Publisher',30,SceneCredits.Publisher,20,30)
		comercial_director, y_position = SceneCredits._credit_group_data(y_position,'Comercial director',30,SceneCredits.ComercialDirector,20,30)
		product_analisis, y_position = SceneCredits._credit_group_data(y_position,'Product analisis',30,SceneCredits.ProductAnalisis,20,30)
		special_thanks, y_position = SceneCredits._credit_group_data(y_position,'Special thanks',30,SceneCredits.SpecialThanks,20,30)

		self.credit_list = level_design + level_artist + programmers + animators + motion_capture + special_effecs + character_design + modeling
		self.credit_list += front_end + executive_producer + producer + director + art_director + music_director + technical_director + sound
		self.credit_list += sound_programmers + session_musicians + writers + voice_over + quality_assurance + aditional_QA + testing_supervisor
		self.credit_list += publisher + comercial_director + product_analisis + special_thanks


	def on_update(self):
		for s in self.credit_list:
			s.position = (s.position[0],s.position[1] + self.velocity)
	def on_event(self):

		# Directions
		if self.dir.button == 'A':
			self.velocity = -5
		else:
			self.velocity = -1

	def on_draw(self, screen):
		screen.fill(cfg.ScreenFillColor)
		for s in self.credit_list:
			s.draw(screen, 'shadow',3)
		pygame.display.flip()

	def _credit_group_data(initial_y_position,section_name,section_offset,personal,personal_offset,indentation = 0):
		y_position = initial_y_position
		font_list = list()
		font_list.append(font.Font(cfg.HeaderFont, cfg.H4,str(section_name),"tr",(cfg.WIDTH/2,10 + y_position),cfg.SubEventColor,cfg.InfoOutlineColor))
		y_position += section_offset
		for p in personal:
			font_list.append(font.Font(cfg.ParagraphFont, cfg.P2,str(p),"tl",(cfg.WIDTH/2 + indentation,10 + y_position),cfg.DefaultColor,cfg.InfoOutlineColor))
			y_position += personal_offset
		return font_list, y_position

def main(args):
	lista, position = SceneCredits._credit_group_data(0,"Game level design",30,SceneCredits.GameLevelDesign,20,30)
	print(f'{len(lista)}, position: {position}')
	return 0

if __name__ == '__main__':
	import sys
	sys.exit(main(sys.argv))
