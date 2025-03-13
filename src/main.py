import pygame
from ball import Ball
from human_paddle import HumanPaddle
from AI_paddle import AIPaddle


def main():
  pygame.init()
  screen_w, screen_h = 800, 600
  BLACK = (0,0,0)
  WHITE = (255,255,255)

  screen = pygame.display.set_mode((screen_w, screen_h))
  pygame.display.set_caption('Pong Game') 
  screen.fill(BLACK)  
  pygame.display.flip()

  clock = pygame.time.Clock()
  ball = Ball(screen_w//2, screen_h//2, 3, 5, 10, WHITE)
  left_paddle = HumanPaddle(10, 50, 0, screen_h//2, 5, WHITE)
  AI_paddle = AIPaddle(10, 50, screen_w-10, screen_h//2, 5, WHITE, 2)
  objects = [ball, left_paddle, AI_paddle]

  running = True
  while running:
    clock.tick(60)
    screen.fill(BLACK)

    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        running = False

    keys = pygame.key.get_pressed()
    left_paddle.handle_controls(keys, pygame.K_w, pygame.K_s)
    AI_paddle.move(ball)

    ball.handle_collision_paddle(left_paddle)
    ball.handle_collision_paddle(AI_paddle)

    if ball.check_loss():
      running = False

    update_objects(objects)
    draw_objects(objects, screen)

    pygame.display.flip()

  display_end_screen()


def update_objects(objects: list):
  for obj in objects:
    obj.update()

def draw_objects(objects: list, screen: pygame.Surface):
  for obj in objects:
    obj.draw(screen)

def display_end_screen():
  pass

if __name__ == "__main__":
  main()