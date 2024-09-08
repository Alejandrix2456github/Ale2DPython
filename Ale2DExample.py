# examples/example_game.py
import pygame
import arcade
from ale2d import PhysicsEngine, FileLoader, ImageHandler

def main():
    # Inicializar Pygame y Arcade
    pygame.init()
    arcade.open_window(800, 600, "Ale2D Example")

    # Crear instancias de los módulos
    physics = PhysicsEngine()
    file_loader = FileLoader()
    image_handler = ImageHandler()

    # Cargar una imagen
    image = image_handler.load_image_pygame("path/to/image.png")

    # Cargar un archivo
    file_content = file_loader.load_file("path/to/file.txt")
    print(file_content)

    # Ejemplo de física
    body = pymunk.Body()
    physics.add_body(body)
    physics.step(0.02)

    # Cerrar Arcade
    arcade.close_window()

if __name__ == "__main__":
    main()
