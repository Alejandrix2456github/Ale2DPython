# tests/test_image_handler.py
import unittest
from ale2d.image_handler import ImageHandler
import pygame
import arcade

class TestImageHandler(unittest.TestCase):
    def test_load_image_pygame(self):
        image = ImageHandler.load_image_pygame("path/to/image.png")
        self.assertIsInstance(image, pygame.Surface)

    def test_load_image_arcade(self):
        image = ImageHandler.load_image_arcade("path/to/image.png")
        self.assertIsInstance(image, arcade.Texture)

if __name__ == '__main__':
    unittest.main()
