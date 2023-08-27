import math
import random
import pygame as pg
from ActvFunc import *

pg.init()

SCREEN_SIZE = (800, 800)
screen = pg.display.set_mode(SCREEN_SIZE)
clock = pg.time.Clock()

def calculate(weight, bias, input, actvFunc):
    result = 0
    for i in range(len(input)):
        result = input[i] * weight[i]
    result += bias

    return actvFunc(result)

def number_to_rgb(color):
    r = (int(color) >> 16) & 0xFF
    g = (int(color) >> 8) & 0xFF
    b = int(color) & 0xFF

    return r, g, b

def combine_lists(list1, list2):
    combined_list = []
    for i in range(len(list1)):
        if random.randint(0, 1) == 0:
            combined_list.append(list1[i])
        else:
            combined_list.append(list2[i])
    return combined_list

def tinker_with_list(object, max_offset):
    tinkered_list = []
    for i in range(len(object)):
        tinkered_list.append(object[i] + random.uniform(-max_offset, max_offset))
    return tinkered_list

class Agent:
    def __init__(self, weights, biases) -> None:
        self.weights = weights
        self.biases = biases
        self.rect = [random.randrange(0, SCREEN_SIZE[0]), random.randrange(0, SCREEN_SIZE[0])]
        self.color = []
    
    def move(self):
        self.rect[0] += calculate(self.weights[0:2], self.biases[0], self.rect, tanh) * calculate(self.weights[4:6], self.biases[2], self.rect, relu6)
        self.rect[1] += calculate(self.weights[2:4], self.biases[1], self.rect, tanh) * calculate(self.weights[6:8], self.biases[3], self.rect, relu6)

        if self.rect[0] <= 0:
            self.rect[0] = 0

        if self.rect[1] <= 0:
            self.rect[1] = 0
        
        if self.rect[0] >= SCREEN_SIZE[0]:
            self.rect[0] = SCREEN_SIZE[0]
        
        if self.rect[1] >= SCREEN_SIZE[1]:
            self.rect[1] = SCREEN_SIZE[1]
        
        self.color = number_to_rgb(sigmoid(sum(self.weights)) * 8290687.5 + sigmoid(sum(self.biases)) * 8290687.5)

    def draw(self):
        pg.draw.circle(screen, self.color, self.rect, 20)

    def select(self):
        if self.rect[0] > 250:
            selectedAgentWeights.append(self.weights)
            selectedAgentBiases.append(self.biases)


current_time = 0
last_time = 0

generation = 0
live = 200
agents = [Agent(list((random.randrange(-100, 100) for _ in range(8))), list((random.randrange(-100, 100) for _ in range(4)))) for _ in range(live)]
run = True
while run:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False

    if current_time - last_time > 3000:
        last_time = pg.time.get_ticks()

        selectedAgentWeights = []
        selectedAgentBiases = []

        for agent in agents:
            agent.select()
        
        print("Generation {}".format(generation))
        print("Death: {}".format(live - len(selectedAgentWeights)))

        generation += 1
        agents = [Agent(tinker_with_list(combine_lists(random.choice(selectedAgentWeights), random.choice(selectedAgentWeights)), 5), tinker_with_list(combine_lists(random.choice(selectedAgentBiases), random.choice(selectedAgentBiases)), 5)) for _ in range(live)]

    current_time = pg.time.get_ticks()
    
    screen.fill((0, 0, 0))

    for agent in agents:
        agent.move()
        agent.draw()

    pg.display.update()
    clock.tick(30)
pg.quit()