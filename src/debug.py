import pygame
from settings import *

pygame.init()
font = pygame.font.Font(None, 25)


def debug(info, y=20, x=1060):
    display_surface = pygame.display.get_surface()
    debug_surf = font.render(str(info), True, "White")
    debug_rect = debug_surf.get_rect(topright=(x, y))
    pygame.draw.rect(display_surface, UI_BG_COLOR, debug_rect.inflate(30, 15))
    pygame.draw.rect(display_surface, UI_BORDER_COLOR, debug_rect.inflate(30, 15), 3)
    display_surface.blit(debug_surf, debug_rect)
