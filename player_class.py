import pygame
from settings import *
vec = pygame.math.Vector2

class Player:
    def __init__(self, app, pos):
        self.app = app
        self.grid_pos = pos
        self.pix_pos = vec(self.grid_pos.x*self.app.cell_width+self.app.cell_width//2, self.grid_pos.y*self.app.cell_height+self.app.cell_height//2)
        self.direction = vec(0,0)
        self.stored_direction = None
        self.able_to_move = True
        self.speed = 5
     


    def update(self):
        if self.able_to_move:
            self.pix_pos += self.direction*self.speed
        if self.time_to_move(): 
            if self.stored_direction != None:
                self.direction = self.stored_direction
            self.able_to_move = self.can_move()

  
        self.grid_pos[0] = self.pix_pos[0] // self.app.cell_width
        self.grid_pos[1] = self.pix_pos[1] // self.app.cell_height


        if self.on_coin():
            self.eat_coin()


    def draw(self):
        pygame.draw.circle(self.app.screen, PLAYER_COLOR, (int(self.pix_pos.x), int(self.pix_pos.y)), self.app.cell_width//2-2)
        pygame.image.load('pacmanSprites/pacman.gif')
        pygame.transform.scale(self.app.screen, (self.app.cell_width ,self.app.cell_height))

    def on_coin(self):
        if self.grid_pos in self.app.coins:
            if (int(self.pix_pos.x+self.app.cell_width//2) % self.app.cell_width) == 0:
                if self.direction == vec(1, 0) or self.direction == vec(-1, 0) or self.direction == vec(0, 0):
                    return True
            if (int(self.pix_pos.y+self.app.cell_height//2) % self.app.cell_height) == 0:
                if self.direction == vec(0, 1) or self.direction == vec(0, -1) or self.direction == vec(0, 0):
                    return True
        return False


    def eat_coin(self):
        self.app.coins.remove(self.grid_pos)
        self.app.state = 'game over'


    def move(self, direction):
        self.stored_direction = direction
    


    def time_to_move(self):
        if (int(self.pix_pos.x+self.app.cell_width//2) % self.app.cell_width) == 0:
            if self.direction == vec(1, 0) or self.direction == vec(-1, 0) or self.direction == vec(0, 0):
                return True
        if (int(self.pix_pos.y+self.app.cell_height//2) % self.app.cell_height) == 0:
            if self.direction == vec(0, 1) or self.direction == vec(0, -1) or self.direction == vec(0, 0):
                return True

    def doMove(self):
        self.pix_pos.x+=direction*self.app.cell_width


    def can_move(self):
        for wall in self.app.walls:
            if vec(self.grid_pos+self.direction) == wall:
                return False
        return True
