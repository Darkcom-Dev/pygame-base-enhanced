import pygame as pg

class Widget:
    """
    Create a functional widget using pygame.draw.rect and pygame.font
    require import pygame
    """		
    style = {
        'text_align' : 'center',
        'text_valign' : 'mid',
    }
    def __init__(self, rect, text = 'text', onclickFunction = None, **kwargs):
        """
        Constructor fucntion for the class
        
        args:
        ---
        rect: pygame.Rect
        text: str # better name label
        onclickFunction: any Python function or method name
        kwargs: dict
        """

    
    def align(rect: pg.rect, font: pg.font, align='center', valign='middle', border_radius=0) -> pg.Rect:
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
