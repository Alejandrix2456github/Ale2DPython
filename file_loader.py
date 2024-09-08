# ale2d/file_loader.py
import os

class FileLoader:
    @staticmethod
    def load_file(file_path):
        if os.path.exists(file_path):
            with open(file_path, 'r') as file:
                return file.read()
        else:
            raise FileNotFoundError(f"File {file_path} not found.")
