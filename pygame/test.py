#! /usr/bin/env python

import pygame
import sys
import random

class Ball(object):
	def __init__(self, resource, pos):
		self.Image = pygame.image.load(resource)
		self.BallRect = self.Image.get_rect()
		self.Speed = [random.randint(1,100), random.randint(1,100)]
		self.BallRect.move_ip(pos[0], pos[1])

	def draw(self, screen):
		screen.blit(self.Image, self.BallRect)

	def move(self):
		self.BallRect.move_ip(self.Speed)

		if self.BallRect.left < 0 or self.BallRect.right > width:
			self.Speed[0] = -self.Speed[0]
		if self.BallRect.top < 0 or self.BallRect.bottom > height:
			self.Speed[1] = -self.Speed[1]


pygame.init();

size = width, height = 1440, 900

speed = [2, 2]

screen = pygame.display.set_mode(size, pygame.FULLSCREEN)

balls = []

for x in xrange(1000):
	balls.append(Ball("ball.png", [x*200, x*100]))

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT: sys.exit()

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE:
				sys.exit()

	for ball in balls:
		ball.move()

	screen.fill((0,0,0))

	for ball in balls:
		ball.draw(screen)

	pygame.display.flip()
