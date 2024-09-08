# ale2d/physics.py
import pymunk

class PhysicsEngine:
    def __init__(self):
        self.space = pymunk.Space()
        self.space.gravity = (0, -981)

    def add_body(self, body):
        self.space.add(body)

    def step(self, dt):
        self.space.step(dt)
