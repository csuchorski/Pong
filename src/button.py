from typing import Callable
import pygame

class Button():
  def __init__(self, text: str, font: pygame.font.Font, pos_x: int, pos_y: int, width: int, height: int, action: Callable[[], None], mode = None):
    self.rect = pygame.Rect(pos_x, pos_y, width, height)
    self.text = text
    self.font = font
    self.action = action
    self.mode = mode

  def draw(self, screen: pygame.Surface):
    white = (255,255,255)
    black = (0,0,0)
    pygame.draw.rect(screen, white, self.rect)
    text_render = self.font.render(self.text, True, black)
    text_rect = text_render.get_rect(center=self.rect.center)
    screen.blit(text_render, text_rect)

  def check_click(self, event: pygame.event.Event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(event.pos) and self.action:
                print("clicked ", self.mode)
                self.action(self.mode)