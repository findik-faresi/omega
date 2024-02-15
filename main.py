import pygame 
from settings import * 
from sys import exit
from game import Game 
from menu import Menu 

class Main():
    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH,HEIGHT))
        self.clock = pygame.time.Clock()

        self.game = Game()
        self.menu = Menu()

    def run(self):
        while True:
            self.clock.tick(FPS)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                    
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.menu.gameOn = False 

            self.screen.fill('black')
            if self.menu.gameOn:
                self.game.run()
            else:
                self.menu.run()
            pygame.display.update()

if __name__ == "__main__":
    main = Main()
    main.run()