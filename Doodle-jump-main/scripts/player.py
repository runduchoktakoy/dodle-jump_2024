from scripts.sprite import Sprite
from scripts.constants import display_size
class Player(Sprite):
    def __init__(self,center,image,jump_power,speed,gravity):
        super().__init__(center,image)
        self.original_image = image.copy()
        self.jump_power = jump_power
        self.speed = speed
        self.gravity = gravity
        self.is_walking_right = False
        self.is_walking_left = False
        self.velocity_y = 0
        self.on_platform = False
    def update(self):
        self.velocity_y = min(self.velocity_y + self.gravity,15)
        self.rect.y += self.velocity_y
        if self.is_walking_left != self.is_walking_right:
            if self.is_walking_left:
                self.rect.x -= self.speed
            else:
                self.rect.x += self.speed
        if self.on_platform:
            self.velocity_y = -self.jump_power
            self.on_platform = False
        if self.rect.right < 0:
            self.rect.left = display_size[0]
        if self.rect.left > display_size[0]:
            self.rect.right = 0
    def collide_sprite(self,other):
        return super().collide_sprite(other) and self.velocity_y > 0
    def reset(self,center):
        super().__init__(center,self.original_image)
        self.is_walking_right = False
        self.is_walking_left = False
        self.velocity_y = 0
        self.on_platform = False