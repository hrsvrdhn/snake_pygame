import random
from settings import *

def randAppleGeneration():
	randAppleX = round(random.randrange(0,display_width-AppleThickness)/20.0)*20.0
	randAppleY = round(random.randrange(0,display_height-AppleThickness)/20.0)*20.0
	return randAppleX,randAppleY