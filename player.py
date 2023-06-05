from pygame import Rect
class Player():
    def __init__(self, texture, pos, direction):
        self.texture = texture
        self.pos = pos
        self.direction = direction
        self.hitbox = Rect(self.pos[0], self.pos[1], self.texture.get_width(), self.texture.get_height())
    
    def update(self):
        self.hitbox = Rect(self.pos[0], self.pos[1], self.texture.get_width(), self.texture.get_height())
