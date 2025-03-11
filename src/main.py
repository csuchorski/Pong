import pygame
from ball import Ball

def main():
  pygame.init()
  screen_w, screen_h = 800, 600
  background_color = (0,0,0)

  screen = pygame.display.set_mode((screen_w, screen_h))
  pygame.display.set_caption('Pong Game') 
  screen.fill(background_color)  
  pygame.display.flip()

  clock = pygame.time.Clock()
  objects = []
  ball = Ball(screen_w//2, screen_h//2, 5, 5, 10, (255,255,255))
  objects.append(ball)

  running = True
  while running:
    clock.tick(60)
    screen.fill(background_color)

    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        running = False
    update_objects(objects)
    draw_objects(objects, screen)

    pygame.display.flip()



def update_objects(objects):
  for obj in objects:
    obj.update()

def draw_objects(objects, screen: pygame.Surface):
  for obj in objects:
    obj.draw(screen)


if __name__ == "__main__":
  main()