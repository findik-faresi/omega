import pygame 
from settings import * 
from tile import Tile 
from player import Player 
from laser import Laser 
pygame.init()

class Game():
    def __init__(self):
        self.display_surface = pygame.display.get_surface()
        self.level_number = 1
        self.setup(level_dic[self.level_number])
        self.game_over_img = pygame.image.load('game-aseprite/game-over.jpg').convert_alpha()
        self.game_over_img = pygame.transform.scale(self.game_over_img , (WIDTH, HEIGHT))

    def setup(self,level_data):

        self.tile = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
        self.laser = pygame.sprite.Group()

        for row_index,row in enumerate(level_data):
            for column_index,cell in enumerate(row):
                x = column_index * SIZE
                y = row_index * SIZE 

                if cell == '0':
                    tile = Tile((x,y))
                    self.tile.add(tile)

                if cell == 'P':
                    player = Player((x,y))
                    self.player.add(player)

                if cell in laser_direction.keys():
                    laser = Laser((x,y),laser_direction[cell])
                    self.laser.add(laser)

    def game_finish_screen(self):
        self.display_surface.blit(self.game_over_img,(0,0))

    def run(self):

        if self.level_number <= len(level_dic.keys()):
            self.tile.draw(self.display_surface) 

            self.player.draw(self.display_surface)
            self.player.update(self.tile,self.laser)

            self.laser.draw(self.display_surface)
            self.laser.update(self.tile)

        if self.level_number > len(level_dic.keys()):
            self.game_finish_screen()

        if self.player.sprite.levelUp:
            self.level_number += 1

            if self.level_number <= len(level_dic.keys()):
                self.setup(level_dic[self.level_number])
