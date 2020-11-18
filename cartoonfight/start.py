import pygame

from . import tools,player

from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    K_a,
    K_d,
    K_w,
    KEYDOWN,
    QUIT,
)


pygame.init()

#Frames Per Second
clock = pygame.time.Clock()
FPS = 27

#Game display
monitor = pygame.display.Info()
DISPLAY_SIZE = (monitor.current_w, monitor.current_h)
DISPLAY = pygame.display.set_mode(DISPLAY_SIZE)
DISPLAY_RECT = DISPLAY.get_rect()

#Game title
CAPTION = "Cartoon Fight"
pygame.display.set_caption(CAPTION)

#load images
_SUB_DIRECTORIES = ['aang','goblin','warrior','backgrounds']
IMAGES = tools.load_images_from_directories(_SUB_DIRECTORIES)

#Scale background
background = pygame.transform.scale(IMAGES['backgrounds']['default'], DISPLAY_SIZE)
	
xOne = 10
xTwo = DISPLAY_SIZE[0]-138
FLOOR = DISPLAY_SIZE[1]-228

playerOne = player.Player([xOne,FLOOR], 100, (128,128), True, DISPLAY)
playerTwo = player.Player([xTwo,FLOOR], 100, (128,128), False, DISPLAY)

def draw_window():
	DISPLAY.blit(background,(0,0))

	playerOne.draw(IMAGES['aang'])
	playerTwo.draw(IMAGES['warrior'])
	
	pygame.display.update()
	

def game_loop():

	run = True

	while run:

		#User hit key
		for event in pygame.event.get():
			#Quit Game
			if event.type == QUIT:
				run = False

		#User press key
		user_press = pygame.key.get_pressed()
                #player 1 actions
		if user_press[K_d]:
			playerOne.mov_right()
		elif user_press[K_a]:
			playerOne.mov_left()
		else:
			playerOne.stand()
		if user_press[K_w] or playerOne.jumping:
			playerOne.jump(FLOOR)

                #player 2 actions
		if user_press[K_RIGHT]:
			playerTwo.mov_right()
		elif user_press[K_LEFT]:
			playerTwo.mov_left()
		else:
			playerTwo.stand()
		if user_press[K_UP] or playerTwo.jumping:
			playerTwo.jump(FLOOR)

		draw_window()
		clock.tick(FPS)

	pygame.quit()
