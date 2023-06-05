from pygame import transform, Rect
class Car():
    def __init__(self, texture, pos, speed, direction):
        self.direction = direction
        self.pos = pos
        if direction == "right":
            self.texture = transform.flip(texture, True, False)
            self.speed = -speed

        else:
            self.texture = texture
            self.speed = speed
            self.pos[0] -= self.texture.get_width()
        self.hitbox = Rect(self.pos[0], self.pos[1], self.texture.get_width(), self.texture.get_height())
    
    def update(self):
        self.hitbox = Rect(self.pos[0], self.pos[1], self.texture.get_width(), self.texture.get_height())
