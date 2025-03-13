import pygame
from ball import Ball
from paddle import Paddle

class AIPaddle(Paddle):
  def __init__(self, width:int, height:int, pos_x: int, pos_y: int , speed: int, color: tuple[int,int,int], difficulty: int):
    super().__init__(width,height,pos_x,pos_y,speed,color)
    self.difficulty = difficulty

  def move(self, ball: Ball):
    match self.difficulty:
      case 0:
        self.__move_diff_easy(ball)
      case 1:
        self.__move_diff_normal(ball)
      case 2:
        self.__move_diff_impossible(ball)
    
  def __move_diff_easy(self, ball):
    if self.rect.centery > ball.rect.centery:
      self.direction = -1
    elif self.rect.centery < ball.rect.centery:
      self.direction = 1
    else:
      self.direction = 0

  def __move_diff_normal(self, ball):
    if self.rect.top > ball.rect.centery + ball.speed_y*5:
      self.direction = -1
    elif self.rect.bottom < ball.rect.centery + ball.speed_y*5:
      self.direction = 1
    else:
      self.direction = 0

  def __move_diff_impossible(self, ball):
    ball_target = self.__predict_ball_target(ball)
    if self.rect.top > ball_target:
      self.direction = -1
    elif self.rect.bottom < ball_target:
      self.direction = 1
    else:
      self.direction = 0

  def __predict_ball_target(self, ball: Ball) -> int:
    #while x is smaller than paddle
    #simulate y + yspeed
    #bounce on walls
    sim_pos_x = ball.rect.x
    sim_speed_x = ball.speed_x
    sim_speed_y = ball.speed_y
    target_y = ball.rect.y

    while ball.speed_x > 1 and sim_pos_x < self.rect.x:
      sim_pos_x += sim_speed_x
      target_y += sim_speed_y
      if target_y <= 0 or target_y > 600:
        sim_speed_y *= -1
    
    return target_y


