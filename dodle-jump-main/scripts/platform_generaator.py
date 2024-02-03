from scripts.functions import load_image
import pygame
from scripts.constants import display_size
from random import randint
from scripts.constants import create_PlatformEvent
from scripts.platform import Platform

class Platform_generator():
    def __init__(self,step):
        self.step = step

        self.platform_images = [
            load_image('assets','images','platform.png'),
            load_image('assets','images','breaking-platform.png'),
            load_image('assets','images','moving-platform.png'),
            load_image('assets','images','platform.png'),
        ]

        self.create_start_configuration()
    def create_start_configuration(self):
        platform = Platform((display_size[0]/2,display_size-50),self.platform_images[0])
        event= pygame.Event(create_PlatformEvent, {'platform':Platform(center,image)})
        pygame.event.post(event)
        for y in range(int(display_size[1]/self.step),-1,-1):
            self.create_platform(y*self.step)
    def create_platform(self,center):
        number = randint(0,3)
        image = self.Platform_image[number]
        min_x = image.get_width()//2
        max_x = display_size[0] - image.get.get_width()//2
        center = (randint(min_x,max_x),center_y)

        event= pygame.Event(create_PlatformEvent, {'platform':Platform(center,image)})
        pygame.event.post(event)
    def update(self,offset_y,platforms):
        if platforms[-1].rect.centry - offset_y >= self.step:
            self.create_platform(offset_y)
            platforms.remove(Platform[0])
    