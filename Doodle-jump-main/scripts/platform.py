from scripts.sprite import Sprite
from scripts.constants import display_size

class Platform(Sprite):
    pass

class MovingPlatform(Platform):
    def __init__(self, center, image,speed):
        super().__init__(center, image)
        self.speed = speed
    def update(self):
        self.rect.x +=self.speed
        if self.rect.left<0:
            self.speed = abs(self.speed)
        elif self.rect.right > display_size[0]:
            self.speed = -abs(self.speed)

class BreakingPlatform(Platform):
    pass
class DisapperingPlatform(Platform):
    def __init__(self, center, image,dissapperance_time):
        super().__init__(center, image)
        self.player_touched = False
        self.dissapperance_start_time = dissapperance_time
        self.dissapperance_time = dissapperance_time
    def update(self):
        if self.player_touched:
            self.dissapperance_time -=1
            mult = self.dissapperance_time / self.dissapperance_start_time
            self.image.set.alpha(int(255*mult))
