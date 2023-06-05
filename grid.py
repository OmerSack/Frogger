from time import time
from random import randint
from math import ceil
class LineGrid():
    def __init__(self, texture, height, y):
        self.texture = texture
        self.height = height
        self.y = y
        self.line = list()
        self.timing = randint(3, 5) / 1.2
        self.line_speed = randint(1, 3) * 1.5
        self.last_time = time() - 5
    
    def fill_line(self):
        times = ceil(1000 / self.texture.get_width())
        for i in range(times):
            self.line.append(self.texture.get_width() * i)