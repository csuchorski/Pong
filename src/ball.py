import pygame


class Ball():
  def __init__(self, pos_x, pos_y, speed_x, speed_y, radius, color):
    self.rect = pygame.Rect(pos_x, pos_y, radius*2, radius*2)

    self.speed_x = speed_x
    self.speed_y = speed_y
    self.radius = radius
    self.color = color

  def update(self):
    self.rect.x += self.speed_x
    self.rect.y += self.speed_y

    if self.rect.top <= 0 or self.rect.bottom >= 600:
      self.speed_y *= -1
    if self.rect.left <= 0 or self.rect.right >= 800:
      self.speed_x *= -1

  def draw(self, screen):
    pygame.draw.ellipse(screen, self.color, self.rect)