import os

def clear_screen(func):
    def wrapper(*args, **kwargs):
        os.system('cls' if os.name == 'nt' else 'clear')
        return func(*args, **kwargs)
    return wrapper
