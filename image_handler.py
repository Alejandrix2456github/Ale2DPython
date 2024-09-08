# ale2d/image_handler.py
import pygame
import arcade

class ImageHandler:
    @staticmethod
    def load_image_pygame(image_path):
        return pygame.image.load(image_path)

    @staticmethod
    def load_image_arcade(image_path):
        return arcade.load_texture(image_path)
