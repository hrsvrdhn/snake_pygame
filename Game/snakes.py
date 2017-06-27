import pygame
import time
import random
from apple_generator import randAppleGeneration
from settings import *
# IS IMPORTANT
pygame.init()



img = pygame.image.load('images/snake_head.png')
appleimg = pygame.image.load('images/apple.png')


# pygame.display.flip() 
# pygame.display.update()

smallfont = pygame.font.SysFont("comicsansms", 25)
medfont = pygame.font.SysFont("comicsansms", 50)
largefont = pygame.font.SysFont("comicsansms", 80)

def text_objects(text, color, size):
	if size == "small":
		textSurface = smallfont.render(text, True, color)
	if size == "medium":
		textSurface = medfont.render(text, True, color)
	if size == "large":
		textSurface = largefont.render(text, True, color)

	return textSurface, textSurface.get_rect()
def message_to_screen(msg, color, y_displace=0, size = "small"):
	textSurf, textRect = text_objects(msg, color, size)
	# screen_text = font.render(msg, True, color)
	# gameDisplay.blit(screen_text, [display_width/2, display_height/2])
	textRect.center = (display_width/2), (display_height/2)+y_displace
	gameDisplay.blit(textSurf, textRect)


def game_intro():
	intro = True
	highscore = None
	try:
		file = open("highscore.txt",'r')
		highscore = file.read()
		file.close()
	except:
		pass
	while intro:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_c:
					intro = False
				elif event.key == pygame.K_q:
					pygame.quit()
					quit()

		gameDisplay.fill(white)

		message_to_screen("Welcome to SnakeLand", green, -100, "large")
		message_to_screen("The objective of the game is to eat red apples", black, 0)
		message_to_screen("The more you eat , the longer you get", black, 30)
		message_to_screen("If you run into yourself, or the edges, you die !", black, 60)
		message_to_screen("Press C to start,P to Pause,  Q to Quit", black, 90)
		if not highscore == None:
			message_to_screen("Current HighScore :" + highscore , black, 120)
		pygame.display.update()
		clock.tick(15)
		
def snake(block_size, snakelist):
	if direction == "right":
		head = pygame.transform.rotate(img,270)
	if direction == "left":
		head = pygame.transform.rotate(img,90)
	if direction == "up":
		head = img
	if direction == "down":
		head = pygame.transform.rotate(img,180)
	
	gameDisplay.blit(head, (snakelist[-1][0], snakelist[-1][1]))

	for XnY in snakelist[:-1]:
		pygame.draw.rect(gameDisplay, green, [XnY[0],XnY[1],block_size,block_size])


def score(score):
	text = smallfont.render("Score :"+str(score), True, black)
	gameDisplay.blit(text, [0,0])



def pause():
	paused = True
	while paused:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_c:
					paused = False
				elif event.key == pygame.K_q:
					pygame.quit()
					quit()					
		gameDisplay.fill(white)
		message_to_screen("Paused", black, -100, "large")
		message_to_screen("Press C to Continue , or Q to Quit", black, 50, "medium")
		pygame.display.update()
		clock.tick(5)


def game_loop():
	global direction
	gameExit = False
	gameOver = False
	lead_x = display_width/2
	lead_y = display_height/2

	snakelist = []
	snakeLength = 1

	lead_x_change = 0
	lead_y_change = 0
	is_highscore = False
	randAppleX,randAppleY = randAppleGeneration()

	while not gameExit:

		while gameOver == True:
			gameDisplay.fill(white)
			message_to_screen("Game Over", red, -100, "large")
			message_to_screen("Your Score :" + str(snakeLength-1), red, 0 , "medium")
			message_to_screen(" Press C to play again or Q to quit ",black, 50, "medium")
			pygame.display.update()
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					gameOver = False
					gameExit = True
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_q:
						gameExit = True
						gameOver = False
					if event.key == pygame.K_c:
						game_loop()

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				gameExit = True
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					direction = "left"
					lead_x_change = -block_size
					lead_y_change = 0
				elif event.key == pygame.K_RIGHT:
					direction = "right"
					lead_x_change = block_size
					lead_y_change = 0
				elif event.key == pygame.K_UP:
					direction = "up"
					lead_y_change = -block_size
					lead_x_change = 0
				elif event.key == pygame.K_DOWN:
					direction = "down"
					lead_y_change = block_size
					lead_x_change = 0
				elif event.key == pygame.K_p:
					pause()

		if lead_x >= display_width or lead_x<0 or lead_y >= display_height or lead_y<0:
			gameOver = True
			try:
				file = open("highscore.txt",'r')
				HighScore = int(file.read())
				file.close()
				print HighScore
				if snakeLength-1>HighScore:
					is_highscore = True
				file = open("highscore.txt",'w')
				file.write(str(snakeLength-1))
				file.close()
			except:
				pass

		lead_x += lead_x_change
		lead_y += lead_y_change

		gameDisplay.fill(white)

		# pygame.draw.rect(gameDisplay, red, [randAppleX,randAppleY,AppleThickness,AppleThickness])
		gameDisplay.blit(appleimg, (randAppleX,randAppleY))

		snakeHead = []
		snakeHead.append(lead_x)
		snakeHead.append(lead_y)
		snakelist.append(snakeHead)

		if len(snakelist) > snakeLength:
			del snakelist[0]

		for eachSegment in snakelist[:-1]:
			if eachSegment == snakeHead:
				gameOver = True

		snake(block_size, snakelist)
		score(snakeLength-1)

		pygame.display.update()

		if lead_x == randAppleX and lead_y == randAppleY:
			randAppleX,randAppleY = randAppleGeneration()
			snakeLength += 1

		# 30 FRAMES PER SECOND
		clock.tick(FPS)

	pygame.quit()
	quit()