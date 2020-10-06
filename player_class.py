import pygame
import sys
from settings import *
from graph import *
from searchProblem import *
import time
vec = pygame.math.Vector2

class Player:
    def __init__(self, app, pos):
        self.app = app
        self.grid_pos = pos
        self.pix_pos = vec(self.grid_pos[0]*self.app.cell_width+self.app.cell_width//2, self.grid_pos[1]*self.app.cell_height+self.app.cell_height//2)
        self.direction = vec(0,0)
        self.stored_direction = None
        self.able_to_move = True
        self.speed = 7
        start_time = time.time()
        self.path = SearchProblem.depthFirstSearch(getGraph(), (self.app.p_pos[0],self.app.p_pos[1]), (self.app.coins[0][0], self.app.coins[0][1]))
        print(self.path)
        print("Time spent for search: %s seconds" % (time.time() - start_time))
        print("Steps done during search: ", len(self.path))
        print ("Memory spent: ", sys.getsizeof(SearchProblem.depthFirstSearch(getGraph(), (self.app.p_pos[0],self.app.p_pos[1]), (self.app.coins[0][0], self.app.coins[0][1]))), " bytes")
        self.current = 0
        self.aim = self.path[self.current]
         
    def update(self):
        self.move()
        if self.able_to_move:
            self.pix_pos += self.direction*self.speed
        if self.time_to_move(): 
            if self.stored_direction != None:
                self.direction = self.stored_direction
            self.able_to_move = self.can_move()

        self.grid_pos[0] = self.pix_pos[0] // self.app.cell_width
        self.grid_pos[1] = self.pix_pos[1] // self.app.cell_height

        if (self.grid_pos[0] == self.aim[0] and self.grid_pos[1] == self.aim[1]):
            self.pix_pos = vec(self.grid_pos[0]*self.app.cell_width+self.app.cell_width//2, self.grid_pos[1]*self.app.cell_height+self.app.cell_height//2)
            if (self.grid_pos[0]==self.app.coins[0] and self.grid_pos[1]==self.app.coins[1]):
                self.app.state = "game over"
            else:
                self.current+=1
                if self.current<len(self.path):
                    self.aim = self.path[self.current]

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


    def move(self):
        if (self.grid_pos[0] - 1 == self.aim[0]):
            self.direction = vec(-1,0)
        if (self.grid_pos[0] + 1 == self.aim[0]):
            self.direction = vec(1,0)
        if (self.grid_pos[1] - 1 == self.aim[1]):
            self.direction = vec(0,-1)
        if (self.grid_pos[1] + 1 == self.aim[1]):
            self.direction = vec(0,1)
        self.stored_direction = self.direction
        

    def time_to_move(self):
        if (int(self.pix_pos.x+self.app.cell_width//2) % self.app.cell_width) == 0:
            if self.direction == vec(1, 0) or self.direction == vec(-1, 0) or self.direction == vec(0, 0):
                return True
        if (int(self.pix_pos.y+self.app.cell_height//2) % self.app.cell_height) == 0:
            if self.direction == vec(0, 1) or self.direction == vec(0, -1) or self.direction == vec(0, 0):
                return True


    def can_move(self):
        for wall in self.app.walls:
            if vec(self.grid_pos+self.direction) == wall:
                return False
        return True
