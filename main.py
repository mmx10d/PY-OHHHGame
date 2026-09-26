import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 800, 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("OHHGame")

# تصحيح الـ Clock بحرف كبير
clock = pygame.time.Clock()

try:
  ball_image = pygame.image.load("Ball.png")
  ball_image = pygame.transform.scale(ball_image, (50, 50))
except:
  print("No Ball Photo Found.")
  pygame.quit()
  sys.exit()


#Ball Proberties:
ball_x = 100
ball_y = 400
ball_speed_x = 6


#Ball Physics:
is_jumping = False
jump_speed = -16
gravity = 1
velocity_y = 0
FLOOR_Y = 450


#Ball FireSystem
bullets = []
bullet_speed = 10
can_shoot = True


#Rect
## her im do copy past from Ai i dnt wnt to write more of someting i dont understand it
obstacles = [
    pygame.Rect(400, 450, 50, 50),
    pygame.Rect(600, 420, 50, 80),
    pygame.Rect(750, 450, 50, 50)
]


running = True

while running:
  clock.tick(60)
  #Innputs here:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

  #game code here:

  #Controll
  ##Move and Controll
  keys = pygame.key.get_pressed()
  if keys[pygame.K_LEFT] or keys[pygame.K_a]:
      ball_x -= ball_speed_x
  if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
      ball_x += ball_speed_x
  ##Jump
  if not is_jumping:
    if keys[pygame.K_UP] or keys[pygame.K_SPACE] or keys[pygame.K_w]:
        is_jumping = True
        velocity_y = jump_speed
  ##Shoot system
  if keys[pygame.K_f]:
    if can_shoot:
        new_bullet = pygame.Rect(ball_x + 40, ball_y + 20, 15, 8)
        bullets.append(new_bullet)
        can_shoot = False
  else:
    can_shoot = True
    
  ###Shot movement
  for bullet in bullets[:]:
    bullet.x += bullet_speed
    if bullet.x > WIDTH:
        bullets.remove(bullet)
  
  #Velocity
  if is_jumping or ball_y < FLOOR_Y:
    velocity_y += gravity
    ball_y += velocity_y

  if ball_y >= FLOOR_Y:
    ball_y = FLOOR_Y
    is_jumping = False
    velocity_y = 0

  #Checker
  for bullet in bullets[:]:
    for obs in obstacles[:]:
        if bullet.colliderect(obs):
            if bullet in bullets:
                bullets.remove(bullet)
            if obs in obstacles:
                obstacles.remove(obs)

  #Others
  screen.fill((30, 30, 30))

  pygame.draw.rect(screen, (34, 139, 34), (0, FLOOR_Y + 50, WIDTH, HEIGHT - FLOOR_Y))

  #Img drawing use program
  for obs in obstacles:
    pygame.draw.rect(screen, (220, 20, 60), obs)

  ##FIre
  for bullet in bullets:
    pygame.draw.rect(screen, (255, 215, 0), bullet)

  ##Ball
  screen.blit(ball_image, (ball_x, ball_y))

  #screen refresch
  pygame.display.flip()

pygame.quit()
sys.exit()
