import pygame
from paddle import Paddle

class HumanPaddle(Paddle):
  def __init__(self, width:int, height:int, pos_x: int, pos_y: int , speed: int, color: tuple[int,int,int], key_up: int, key_down: int):
    super().__init__(width,height,pos_x,pos_y,speed,color)
    self.key_up = key_up
    self.key_down = key_down

  def handle_movement(self, keys_pressed: pygame.key.ScancodeWrapper, _):
    if keys_pressed[self.key_up]:
      self.direction = -1
    elif keys_pressed[self.key_down]:
      self.direction = 1
    else:
      self.direction = 0
