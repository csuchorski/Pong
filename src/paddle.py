import pygame

class Paddle:
  def __init__(self, width:int, height:int, pos_x: int, pos_y: int , speed: int, color: tuple[int,int,int]):
    self.rect = pygame.Rect(pos_x, pos_y,width, height)
    self.speed = speed
    self.color = color
    self.direction = 0

  def update(self):
    self.rect.y += self.speed * self.direction

    if self.rect.top <= 0:
      self.rect.top = 0
    if self.rect.bottom >= 600:
      self.rect.bottom = 600
  
  def draw(self, screen: pygame.Surface):
    pygame.draw.rect(screen, self.color, self.rect)