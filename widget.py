import pygame as pg

"""
Si estás creando una biblioteca o marco de interfaz de usuario (UI) personalizado, 
es una buena práctica tener una clase base común para todos los widgets. 

En este caso, una clase base común podría ser Widget. La clase Widget puede 
contener propiedades y métodos comunes a todos los widgets, como la posición, 
el tamaño, el color, etc.

La clase Widget también puede contener un método draw que se encarga de 
dibujar el widget en la pantalla. Cada widget que hereda de la clase Widget 
puede entonces personalizar el método draw para que se adapte a su 
comportamiento específico.

En resumen, podrías crear una clase base Widget y hacer que todos los 
widgets hereden de ella, y luego definir el método draw en la clase 
Widget para que sea utilizado por todos los widgets.
"""

class Widget:
    """
    Create a functional widget using pygame.draw.rect and pygame.font
    require import pygame
    """		
    style = {
        'font_family': 'System',
        'font_size': 20,
		'font_align': 'center',
		'font_valign': 'middle',
        'text_color': 'black',
		'font_clicked_color' : 'blue',
		'font_disabled_color': 'gray',
		'font_highlight_color': 'white',
        'bg_color': 'white',
		'bg_clicked_color': '#f5f5ff',
		'bg_disabled_color': '#fff5cc',
		'bg_highlight_color': 'gray',
		'stroke': 0,
		'border_radius': 0,
		'top_left_radius': -1,
		'top_right_radius': -1,
		'bottom_left_radius': -1,
		'bottom_right_radius': -1,
        'check_char': '[x]',
		'uncheck_char': '[ ]',
    }
    def __init__(self, rect, text = '', onclickFunction = None, style = None):
        """
        Constructor fucntion for the class
        
        args:
        ---
        rect: pygame.Rect
        text: str # better name label
        onclickFunction: any Python function or method name
        """
        # Rect for rect frame, also used for text aligment
        self.rect = rect
        # Text content for the widget
        self.text = text
        # Function to be called when the widget is clicked
        self.onclickFunction = onclickFunction
        # Generic style for the widgets
        self.style = style or Widget.style

        # private boolean variable events, posible read only return
        self.in_rect = bool()
        self.enabled = True
        self._event = {'clicked': False, 'highlighted' : False}

        # Simplification of style variables
        style_vars = ['font_family','font_size','text_color', 'font_clicked_color', 'font_disabled_color', 'font_highlight_color', 'bg_color',
	                  'bg_clicked_color', 'bg_disabled_color', 'bg_highlight_color', 'border_radius', 'top_left_radius',
	                  'top_right_radius', 'bottom_left_radius', 'bottom_right_radius', 'stroke', 'check_char', 'uncheck_char']
        
        style_values = {var: self.style.get(var, Widget.style[var]) for var in style_vars}
        self.font_family, self.font_size, self.font_color, self.font_clicked_color, self.font_disabled_color, self.font_highlight_color, self.bg_color, self.bg_clicked_color, \
	    self.bg_disabled_color, self.bg_highlight_color, self.border_radius, self.top_left_radius, self.top_right_radius, self.bottom_left_radius, \
	    self.bottom_right_radius, self.stroke, self.check_char, self.uncheck_char = [style_values[var] for var in style_vars]
        
    def handle_events(self):
        """
		Handle button events.	
		### Return:
		None
		"""
        if not self.enabled:    return
        self.pos = pg.mouse.get_pos()
        self.mouse = pg.mouse.get_pressed()
        self.in_rect = self.rect.collidepoint(self.pos)
        
        if self.mouse == (1, 0, 0):
            if self.in_rect:
                if not self._event['clicked'] and self.onclickFunction is not None:	self.onclickFunction()
            self._event['clicked'] = self.in_rect
        # Highlight
        else:
            self._event['highlighted'] = self.in_rect
            self._event['clicked'] = False


    def align(self, rect: pg.Rect, font: pg.font, align='center', valign='middle', border_radius=0) -> pg.Rect:
        """
        Align a rectangle to a given position.
        ### Args:
        ---
        :param rect: The rectangle to be aligned.
        :param font: The font to be used for alignment.
        :param align: The horizontal alignment. Can be 'left', 'center', or 'right'.
        :param valign: The vertical alignment. Can be 'top', 'middle', or 'bottom'.
        :param border_radius: The radius of the border.
        ### Returns:
        ---
        :return: The aligned rectangle.
        """

        aligns = {
			'left': rect[0] + border_radius,
			'center': rect[0] + rect[2]//2 - font.get_width()//2,
			'right': rect[0] + rect[2] - border_radius - font.get_width()
		}
		
        valigns = {
			'top': rect[1] + border_radius,
			'middle': rect[1] + rect[3]//2 - font.get_height()//2,
			'bottom': rect[1] + rect[3] - border_radius - font.get_height()
		}

        x = aligns[align]
        y = valigns[valign]
        return pg.Rect(x, y, font.get_width(), font.get_height())
    
    def draw(self, screen: pg.Surface) -> None:
        """
        Draw the widget to the screen.
        ### Args:
        ---
        screen: pygame.Surface
        """
        self.rect = self.align(self.rect, self.font, self.style['font_align'], self.style['font_valign'], self.style['border_radius'])
