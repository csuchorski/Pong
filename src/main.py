import pygame
from ball import Ball
from button import Button
from human_paddle import HumanPaddle
from AI_paddle import AIPaddle

def main():
  pygame.display.set_caption('Pong Game') 
  screen.fill(BLACK)  
  pygame.display.flip()
  show_main_menu()

def update_objects(objects: list):
  for obj in objects:
    obj.update()

def draw_objects(objects: list):
  for obj in objects:
    obj.draw(screen)

def start_game(mode: int):
  clock = pygame.time.Clock()
  ball = Ball(SCREEN_W//2, SCREEN_H//2, 3, 5, 10, WHITE)
  left_paddle, right_paddle = None, None
  match mode:
    case 0:
      left_paddle = HumanPaddle(10, 50, 0, SCREEN_H//2, 5, WHITE, pygame.K_w, pygame.K_s)
      right_paddle = HumanPaddle(10, 50, SCREEN_W-10, SCREEN_H//2, 5, WHITE, pygame.K_UP, pygame.K_DOWN)
    case 1:
      left_paddle = HumanPaddle(10, 50, 0, SCREEN_H//2, 5, WHITE, pygame.K_w, pygame.K_s)
      right_paddle = AIPaddle(10, 50, SCREEN_W-10, SCREEN_H//2, 5, WHITE, 2)
    case 2:
      left_paddle = AIPaddle(10, 50, 0, SCREEN_H//2, 5, WHITE, 2)
      right_paddle = AIPaddle(10, 50, SCREEN_W-10, SCREEN_H//2, 5, WHITE, 2)
    case _:
      quit_game()
  objects = [ball, left_paddle, right_paddle]

  while True:
    clock.tick(60)
    screen.fill(BLACK)

    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        quit_game()

    keys = pygame.key.get_pressed()
    left_paddle.handle_movement(keys, ball)
    right_paddle.handle_movement(keys, ball)

    ball.handle_collision_paddle(left_paddle)
    ball.handle_collision_paddle(right_paddle)

    if ball.check_loss():
      break

    update_objects(objects)
    draw_objects(objects)

    pygame.display.flip()

def quit_game(_):
  pygame.quit()
  exit()

def show_main_menu():
  running = True
  while running:
    screen.fill(BLACK)
    for button in buttons:
      button.draw(screen)

    for event in pygame.event.get():
      if event.type == pygame.QUIT:
          running = False
      for button in buttons:
        button.check_click(event)

    pygame.display.flip()
    

if __name__ == "__main__":
  pygame.init()
  SCREEN_W, SCREEN_H = 800, 600
  screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))
  BLACK = (0,0,0)
  WHITE = (255,255,255)

  button_start_PvP = Button("Player vs Player", pygame.font.Font(None, 20), SCREEN_W//2, SCREEN_H//2-200, 200, 50, start_game, 0)
  button_start_PvAI = Button("Player vs AI", pygame.font.Font(None, 20), SCREEN_W//2, SCREEN_H//2-100, 200, 50, start_game, 1)
  button_start_AIvAI = Button("AI vs AI", pygame.font.Font(None, 20), SCREEN_W//2, SCREEN_H//2, 200, 50, start_game, 2)
  button_quit = Button("Quit", pygame.font.Font(None, 20), SCREEN_W//2, SCREEN_H//2 + 100, 200, 50, quit_game)
  buttons = [button_start_PvP, button_start_PvAI, button_start_AIvAI, button_quit]

  main()