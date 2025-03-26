import pygame
import random
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
	def __init__(self, x, y, radius):
		super().__init__(x, y, radius)

	def draw(self, screen):
		pygame.draw.circle(screen, (255,255,255), self.position, self.radius, 2)

	def update(self, dt):
		self.position += self.velocity * dt

	def split(self):
		self.kill()

		if self.radius <= ASTEROID_MIN_RADIUS:
			return
		
		rand_angle = random.uniform(20, 50)
		smaller_asteroid_one_velocity = self.velocity.rotate(-rand_angle)
		smaller_asteroid_two_velocity = self.velocity.rotate(rand_angle)
		smaller_asteroid_one_velocity *= 1.2
		smaller_asteroid_two_velocity *= 1.2
		new_radius = self.radius - ASTEROID_MIN_RADIUS

		a_one = Asteroid(self.position.x, self.position.y, new_radius)
		a_two = Asteroid(self.position.x, self.position.y, new_radius)

		a_one.velocity = smaller_asteroid_one_velocity
		a_two.velocity = smaller_asteroid_two_velocity


	