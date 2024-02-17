import pygame
import os
from scripts.functions import load_image
from scripts.player import Player
from scripts.constants import display_size
from scripts.platform import Platform
from scripts.platform_generator import PlatformGenerator
class Game:
    def __init__(self):
        self.background = load_image("assets","images","background.png")
        self.platform_generator = PlatformGenerator(200)
        self.offset_y = 0
        self.player = Player(
            (240,600),
            load_image("assets","images","player.png"),
            50,20,0.65
        )
        self.losed = False

        self.tring = 1

        self.platforms = list()

        self.font = pygame.Font(os.path.join("assets","fonts","pixel.ttf"),32)

    def update(self):
        self.losed = self.player.rect.top - self.offset_y >= display_size[1]
        if self.platforms:
            self.platform_generator.update(self.offset_y,self.platforms)

        self.player.update()
        for st in self.platforms:
            if st.collide_sprite(self.player):
                self.player.on_platform = True
        if self.player.rect.bottom - self.offset_y < display_size[1] / 3:
            self.offset_y = self.player.rect.bottom - display_size[1] / 3
        self.platform_generator.update(self.offset_y,self.platforms)


    def render(self,surface):
        surface.blit(self.background,(0,0))
        for pl in self.platforms:
            pl.render(surface, self.offset_y)
        self.player.render(surface, self.offset_y)

        score = round(- self.offset_y / 10)

        if self.losed:
            score_text = self.font.render(f"Ваш рекорд:{score}", True, (1,1,1))
            hint_text = self.font.render("Нажмите любую клавишу", True, (1,1,1))
            tt = self.font.render(f"попытка{self.tring}", True, (1,1,1))


            score_rect = score_text.get_rect(
                centerx = display_size[0]/2,
                centery= display_size[1]/2 - 25
            )
            hint_rect = hint_text.get_rect(
                centerx = display_size[0]/2,
                centery= display_size[1]/2 + 25
            )
            tt_rect = tt.get_rect(
                centerx = display_size[0]/2,
                centery= display_size[1]/2 + 50
            )

            surface.blit(score_text,score_rect)
            surface.blit(hint_text,hint_rect)
            
            return
        else:
            text = self.font.render(str(score),True,(1,1,1))
            rect = text.get_rect(midtop=(display_size[0]/2,10))
            surface.blit(text,rect)

    def handle_key_down_event(self,key):
        if self.losed:
            self.restart()
        if key == pygame.K_a:
            self.player.is_walking_left = True
        elif key == pygame.K_d:
            self.player.is_walking_right = True
    def handle_key_up_event(self,key):
        if key == pygame.K_a:
            self.player.is_walking_left = False
        elif key == pygame.K_d:
            self.player.is_walking_right = False
    def handle_create_platforms_event(self,platform):
        self.platforms.append(platform)
    def restart(self):
        self.losed = False
        self.offset_y = 0
        self.platforms = list()
        self.platform_generator.create_start_configuration()
        self.tring +=1

    
