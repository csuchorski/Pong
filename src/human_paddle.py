import pygame
from paddle import Paddle

class HumanPaddle(Paddle):
  def __init__(self, width:int, height:int, pos_x: int, pos_y: int , speed: int, color: tuple[int,int,int]):
    super().__init__(width,height,pos_x,pos_y,speed,color)

  def handle_controls(self, keys_pressed: pygame.key.ScancodeWrapper, key_up: int, key_down: int):
    if keys_pressed[key_up]:
      self.direction = -1
    elif keys_pressed[key_down]:
      self.direction = 1
    else:
      self.direction = 0
