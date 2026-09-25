import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 800, 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.set_caption("OHHGame")

running = True

while running:
  #Innputs here:
  for event in pygame.event.get():
    if event.type == pygame.QUIT():
      running = False


  #game code here:



  #Others
  screen.fill(0,0)
  pygame.display.flip()

pygame.quit()
sys.exit()