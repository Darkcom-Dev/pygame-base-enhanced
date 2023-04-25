#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Importante para mejorar un poco mas el joystick
# https://nerdparadise.com/programming/pygamejoystick

# Módulos
import scene
import config as cfg
import text_presets as preset
import font
import math
import pygame
import random

# Constantes


# Clases
# ---------------------------------------------------------------------

class SceneJoystickDisplay(scene.Scene):
	"""
	Joystick controller demo scene

	he class is used to create a demo scene for joystick controllers 
	that displays information about the joystick's buttons, hats, 
	and axes on the screen.
	"""

# ---------------------------------------------------------------------

# Funciones
# ---------------------------------------------------------------------

	def __init__(self, director):
		"""
    	Initializes an instance of the class.

    	Args:
    	- director: an instance of a class that is used as an argument to initialize this class

    	Attributes:
    	- dir: the director instance passed as an argument to initialize this class
    	- event_text: an instance of a text object that is used to display event text
    	- history_text: an instance of a text object that is used to display history text
    	- background: an instance of a Pygame image that is used as the background of the controller
    	- info_text_list: a list of instances of text objects that are used to display info for each axis
    	- hat_list: a list of instances of text objects that are used to display info for each hat
    	- activeColor: a tuple representing the RGB values of the active color
    	- normalColor: a tuple representing the RGB values of the normal color
		- color_dict: a dictionary of color names and RGB values
    	- mouse: a list of mouse coordinates
    	"""
		
		self.dir = director
		
		self.event_text = preset.event_text
		self.event_text.text = "Hola desde scene_title"
		
		self.history_text = preset.history_text
		# Imagen de fondo de un joystick de SNES
		self.background = pygame.image.load(cfg.SpritesDir + cfg.ControllerBackground).convert()
		
		
		self.info_text_list = list()
		self.hat_list = list()
		
		self.initialize_controller()
		# Colores
		color_names = ['colorA', 'colorB', 'colorX', 'colorY', 'colorL', 'colorR', 'colorUp', 'colorDown', 'colorLeft', 'colorRight']
		self.activeColor = (255,0,0)
		self.normalColor = (128, 128, 128)		
		self.color_dict = {name: self.normalColor for name in color_names}
		# Colores de los botones
		for name in color_names:
			setattr(self, name, self.color_dict[name])

		# Coordenadas del mouse
		self.mouse = list()

	def initialize_controller(self):
		"""
    	Initialize the controller by setting the number of axes and hats, and creating
    	info text and hat list for each axis and hat respectively.

    	### Args:
    	    self: the instance of the controller class

    	### Returns:
    	    None
    	"""
		if self.dir.J1:
			self.num_axes = self.dir.J1.get_numaxes()
			self.info_text_list = []
			for i in range(self.num_axes):
				self.info_text_list.append(font.Font(cfg.ParagraphFont, cfg.P2,f'info {i}',"tl",(10,10 + (20*i)),cfg.DefaultColor,cfg.InfoOutlineColor))
			
			self.num_hats = self.dir.J1.get_numhats()
			self.hat_list = []
			for i in range(self.num_hats):
				self.hat_list.append(font.Font(cfg.ParagraphFont, cfg.P2,f'info {i}',"tl",(100,10 + (20*i)),cfg.DefaultColor,cfg.InfoOutlineColor))
		

	def on_update(self):
		"""
		Update the mouse position and the history text.
		
		Gets the current mouse position using `pygame.mouse.get_pos()` and updates 
		`self.mouse` with the new position. Then, updates the text of `self.history_text` 
		with the new mouse position in string format.
		
		Args:
		- self: An instance of the class that has the `on_update` method.
		
		Returns:
		- None
		"""
		self.mouse = pygame.mouse.get_pos()
		self.history_text.text = f'{str(self.mouse)}'
	
	def button_colors(self):
		"""Set button colors based on current direction and active button.
		
		Assigns self.activeColor to buttons that correspond to the active
		direction or button, and self.normalColor to all other buttons.
		
		Args:
		- self: An instance of the class containing the button colors and direction data.
		
		Returns:
		- None.
    	"""
		# Buttons
		self.colorLeft = self.activeColor if self.dir.horizontal == -1 else self.normalColor
		self.colorRight = self.activeColor if self.dir.horizontal == 1 else self.normalColor
		self.colorUp = self.activeColor if self.dir.vertical == 1 else self.normalColor
		self.colorDown = self.activeColor if self.dir.vertical == -1 else self.normalColor
		self.colorA = self.activeColor if self.dir.button == 'A' or self.dir.button == 'AB' else self.normalColor
		self.colorB = self.activeColor if self.dir.button == 'B' or self.dir.button == 'AB' else self.normalColor
		self.colorX = self.activeColor if self.dir.button == 'X' or self.dir.button == 'XY' else self.normalColor
		self.colorY = self.activeColor if self.dir.button == 'Y' or self.dir.button == 'XY' else self.normalColor
		self.colorL = self.activeColor if self.dir.button == 'L' or self.dir.button == 'LR' else self.normalColor
		self.colorR = self.activeColor if self.dir.button == 'R' or self.dir.button == 'LR' else self.normalColor

	def on_event(self):
		"""
		- Update button and color attributes based on input direction.		
		- Also updates the event text and tag buttons. 
		
		If J1 joystick is active,
		updates the event text to reflect which button has been pressed, the hat
		values, and the axis values.
		
		### Returns:
		None
    	"""
		# Update color buttons
		self.button_colors()

		self.tag_directions()

		self.tag_buttons()
		
		# Get joystick info
		self.joystick_info()
		
	def tag_directions(self):
		"""
		Updates the event text and tag buttons based on input direction.
		
		If J1 joystick is active,
		updates the event text to reflect which button has been pressed, the hat
		values, and the axis values.
		
		### Returns:
		None
		"""
		if self.dir.horizontal == -1:self.event_text.text = "Key_left"		
		if self.dir.horizontal == 1:self.event_text.text = "Key_right"
		if self.dir.vertical == 1:self.event_text.text = "Key_up"
		if self.dir.vertical == -1:	self.event_text.text = "Key_down"
		
	def joystick_info(self):
		"""
		Prints information about the joystick's buttons, hats, and axes to the screen.
		
		If the joystick's J1 direction is pressed, the function loops through
		each button on the joystick and prints a message to the screen indicating
		which button was pressed. Next, the function loops through each hat on the
		joystick and prints the position of each hat to the screen. Finally, the
		function loops through each axis on the joystick and prints the current
		value of each axis to the screen rounded to 2 decimal places.
		
		Parameters:
		- self (Joystick): An instance of the Joystick class.
		
		Returns:
		- None
    	"""
		if self.dir.J1:
			for i in range(self.dir.J1.get_numbuttons()):
				if self.dir.J1.get_button(i):	self.event_text.text = f'Joy button {i}'
			
			for i in range(self.num_hats):
				self.hat_list[i].text = f'hat {i}: {self.dir.J1.get_hat(i)}'
			
			for i in range(self.num_axes):
				self.info_text_list[i].text = f'Axis {i}: {round(self.dir.J1.get_axis(i),2)}'

	def on_draw(self, screen):
		"""
		Draw the game screen on the given Pygame screen object.
		
		The function draws the background image, the event text with a sine
		wave motion and a chromatic effect, the circle and rectangle buttons,
		the history text, the info texts, and the hats on the screen. Finally,
		it updates the display to show the changes.
		
		Args:
		- screen `pygame.Surface`: The Pygame screen object to draw on.
    	"""
		screen.blit(self.background, (0,0))
		self.event_text.draw(screen)
		self.event_text.position = (math.sin(pygame.time.get_ticks()/1000) * cfg.WIDTH/4 + cfg.WIDTH/2, random.randrange((cfg.HEIGHT/2) -2,(cfg.HEIGHT/2) +2))
		self.event_text.draw(screen, "chromatic",2)
		
		self.draw_circle_buttons(screen)
		
		self.draw_rectangle_buttons(screen)
		
		self.history_text.draw(screen)
		
		for info in self.info_text_list:
			info.draw(screen)
			
		for hat in self.hat_list:
			hat.draw(screen)
		
		pygame.display.flip()

	def tag_buttons(self):
		"""
		Set the event text to show the button tag associated with the current 
		direction button, if any.
		
		The function looks up the button tag for the current direction button in 
		a dictionary of known button tags. If a match is found, it sets the text of
		the event display to the corresponding button tag description.
		
		### Args:
		- self: The instance of the class that calls the function.
		
		Returns:
		- None.
    	"""
		button_tags = {
			'A':'Key_space or A',
			'B':'Key_left_ctrl or B',
			'X':'Key_left_shift or X',
			'Y':'Key_left_alt or Y',
			'L':'Key_Q or L',
			'R':'Key_E or R',
			'AB':'AB',
			'XY':'XY',
			'LR':'LR'
		}

		for tag in button_tags:
			if self.dir.button == tag:
				self.event_text.text = button_tags[tag]

	def draw_circle_buttons(self, screen):
		"""
    	Draws circular buttons on the given Pygame screen object at the specified
    	coordinates with the corresponding colors. 

    	### Args:
    	- self: instance of the class containing the function
    	- screen: Pygame screen object to draw the buttons on

    	Returns:
    	- None
    	"""
		circles = [
			((314,382),self.colorA),
			((285,406),self.colorB),
			((256,382),self.colorX),
			((285,358),self.colorY)
		]
		for circle in circles:
			pygame.draw.circle(screen,circle[1],circle[0],10)

	def draw_rectangle_buttons(self, screen):
		"""
		Draws rectangular buttons on the given Pygame screen.

    	### Args:
    	- self: The object instance.
    	- screen: A Pygame display surface.

    	Returns:
    	- None.
		"""
		rectangles = [
			((280,290,10,10),self.colorR),
			((95,290,10,10),self.colorL),
			((90,360,10,10),self.colorUp),
			((90,396,10,10),self.colorDown),
			((70,378,10,10),self.colorLeft),
			((108,378,10,10),self.colorRight)
		]
		for rectangle in rectangles:
			pygame.draw.rect(screen,rectangle[1],rectangle[0])
# ---------------------------------------------------------------------

def main():
	pass

if __name__ == '__main__':
	main()
