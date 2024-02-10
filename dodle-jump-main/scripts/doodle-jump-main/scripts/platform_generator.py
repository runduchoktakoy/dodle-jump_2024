import pygame
from scripts.platform import Platform
from scripts.functions import load_image
from random import random, randint
from scripts.constants import display_size, CreatePlatformEvent
class PlatformGenerator():
    def __init__(self,step):
        self.step = step
        self.platform_images = [
            load_image("assets","images","platform.png"),
            load_image("assets","images","breaking-platform.png"),
            load_image("assets","images","platform.png"),
            load_image("assets","images","moving-platform.png"),
        ]
        self.create_start_configuration()
    
    def create_start_configuration(self):
        platform=Platform((display_size[0]/2, display_size[1]-50), self.platform_images[0])
        event= pygame.Event(CreatePlatformEvent, {"platform": platform})
        pygame.event.post(event)

        for y in range(int(display_size[1]/self.step), -1, -1):
            self.create_platform(y*self.step)

    
    def create_platform(self, center_y):
        number = round(random() * 3)
        image = self.platform_images[number]
        min_x = image.get_width()//2
        max_x = display_size[0] - image.get_width()//2
        center = (min_x + round(random() * (max_x - min_x)),center_y)

        event= pygame.Event(CreatePlatformEvent, {"platform": Platform(center,image)})
        pygame.event.post(event)



    def update(self, offset_y, platforms):
        if platforms[-1].rect.centery - offset_y >= self.step:
            self.create_platform(offset_y)
            platforms.remove(platforms[0])