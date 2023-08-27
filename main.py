import pygame as pg
from random import uniform, choice, randint
import math
from tkinter import *
from tkinter import messagebox
from ActvFunc import *

win = Tk()

win.geometry("625x50")

live = 0
selectionMethod = ""
time = 0
mutationChance = 0
mutationOffset = 0

def input():
   global live, selectionMethod, time, mutationChance, mutationOffset
   live = entryVar1.get()
   live = int(live)
   selectionMethod = entryVar2.get()
   time = entryVar3.get()
   time = int(time)
   mutationOffset = entryVar4.get()
   mutationOffset = int(mutationOffset)
   mutationChance = entryVar5.get()
   mutationChance = int(mutationChance)
   close_win()

def close_win():
    win.destroy()

label1 = Label(win, text="Lives Count",
font=('Poppins bold', 10))

entryVar1 = StringVar()
entry1 = Entry(win, bd = 2, textvariable = entryVar1)

label2 = Label(win, text="Selection Method",
font=('Poppins bold', 10))

entryVar2 = StringVar()
entry2 = Entry(win, bd = 2, textvariable = entryVar2)

label3 = Label(win, text="Timer",
font=('Poppins bold', 10))

entryVar3 = StringVar()
entry3 = Entry(win, bd = 2, textvariable = entryVar3)

label4 = Label(win, text="Mutation Offset",
font=('Poppins bold', 10))

entryVar4 = StringVar()
entry4 = Entry(win, bd = 2, textvariable = entryVar4)

label5 = Label(win, text="Mutation Chance",
font=('Poppins bold', 10))

entryVar5 = StringVar()
entry5 = Entry(win, bd = 2, textvariable = entryVar5)

label1.grid(row=0, column=0)
entry1.grid(row=1, column=0)
label2.grid(row=0, column=1)
entry2.grid(row=1, column=1)
label3.grid(row=0, column=2)
entry3.grid(row=1, column=2)
label4.grid(row=0, column=3)
entry4.grid(row=1, column=3)
label5.grid(row=0, column=4)
entry5.grid(row=1, column=4)
win.protocol("WM_DELETE_WINDOW", input)

win.mainloop()

pg.init()

SCREEN_SIZE = 800, 800
screen = pg.display.set_mode(SCREEN_SIZE)
clock = pg.time.Clock()

# The line `normalize = lambda value, divider: value / divider` is defining a lambda function named
# `normalize`. This lambda function takes in two arguments `value` and `divider` and returns the
# result of dividing `value` by `divider`.
normalize = lambda value, divider: value / divider

def tinker_with_list(input_list, max_offset):
    """
    The function takes a list and a maximum offset value, and returns a modified list where each element
    has been randomly offset within the given range.
    
    :param input_list: A list of elements that will be modified by adding a random offset to each
    element
    :param max_offset: The maximum amount by which each element in the input_list can be modified. The
    modification is done by adding a random offset value between -max_offset and max_offset to each
    element
    :return: The function `tinker_with_list` is returning a modified list where each element of the
    input list has been randomly offset by a value between `-max_offset` and `max_offset`.
    """
    modified_list = []

    for element in input_list:
        offset = uniform(-max_offset, max_offset)
        modified_element = element + offset
        modified_list.append(modified_element)

    return modified_list

def average_list(input_list):
    modified_list = []
    
    for i in range(len(input_list[0])):
        average = 0
        for list in input_list:
            average += list[i]
        average /= len(input_list)
        modified_list.append(average)

    return modified_list

def average(input_list):
    average = 0
    
    for i in input_list:
        average += i
    average /= len(input_list)
        

    return average

def find_largest_variable(**kwargs):
    """
    The function finds the variable with the largest value among a set of variables passed as keyword
    arguments.
    :return: The function `find_largest_variable` returns the name of the variable with the largest
    value among the variables passed as keyword arguments.
    """
    largest_variable = None
    largest_value = float('-inf')

    for var_name, var_value in kwargs.items():
        if var_value > largest_value:
            largest_value = var_value
            largest_variable = var_name

    return largest_variable

def number_to_rgb(number):
    """
    The function takes a number and returns its corresponding RGB values.
    
    :param number: The input number that represents a color in RGB format. The function extracts the
    red, green, and blue components from this number and returns them as separate values
    :return: a tuple of three integers representing the red, green, and blue values of a color in the
    RGB color model.
    """
    red = (int(number) >> 16) & 0xFF
    green = (int(number) >> 8) & 0xFF
    blue = int(number) & 0xFF

    return red, green, blue
    
def calculate(weight, bias, input, actvfunc = lambda x: x):
    x = 0
    for i in range(len(weight)):
        x += input[i] * weight[i]
    x += bias
    return actvfunc(x)

def combine_list(list1, list2):
    new_list = []

    for i in range(len(list1)):
        if randint(0, 1) == 0:
            new_list.append(list1[i])
        else:
            new_list.append(list2[i])
    return new_list


# The Agent class defines the behavior and attributes of an agent in a simulation, including its
# position, movement, and selection.
class Agent:
    def __init__(self, weight : tuple, bias : tuple) -> None:
        """
        The function initializes an object with weight, bias, id, position, color, speed, and direction
        attributes.
        
        :param weight: The `weight` parameter is a tuple that represents the weights associated with the
        object. It is used in calculations or operations involving the object's weight
        :type weight: tuple
        :param bias: The `bias` parameter is a tuple that represents the bias values for the object. In
        machine learning, bias is an additional parameter that is added to the weighted sum of inputs to
        determine the output of a neuron. It allows the model to adjust the output even when all the
        input values are zero
        :type bias: tuple
        :param id: The `id` parameter is an optional integer that represents the identifier of the
        object being initialized. It is set to 0 by default, defaults to 0
        :type id: int (optional)
        """
        self.weight = weight
        self.bias = bias
        self.x = uniform(0, SCREEN_SIZE[0])
        self.y = uniform(0, SCREEN_SIZE[1])
        self.rect = [self.x, self.y]
        self.color = (255, 255, 255)
        self.dir = 0
        self.speedx = 0
        self.speedy = 0
        self.speed = 0
    
    def run(self) -> None:
        """
        The function updates the position and direction of an object based on its weight, bias, and
        current position, and also updates its color and rectangle coordinates.
        """
        self.speed += calculate(self.weight[0:3], self.bias[0], (normalize(self.x, 800), normalize(self.y, 800), normalize(self.dir, 360)), tanh)
        self.dir += calculate(self.weight[3:6], self.bias[1], (normalize(self.x, 800), normalize(self.y, 800), normalize(self.dir, 360)), tanh)

        self.speed *= 0.9

        if self.dir >= 360:
            self.dir = 360
        
        if self.dir <= -360:
            self.dir = -360

        self.x += self.speed * math.sin(self.dir)
        self.y += self.speed * math.cos(self.dir)
        
        # self.x += calculate(self.weight[0:2], self.bias[0], (self.x, self.y), tanh) * calculate(self.weight[4:6], self.bias[2], (self.x, self.y), relu6)
        # self.y += calculate(self.weight[2:4], self.bias[1], (self.x, self.y), tanh) * calculate(self.weight[6:8], self.bias[3], (self.x, self.y), relu6)

        # self.speedx *= 0.9
        # self.speedy *= 0.9


        # self.x += self.speedy
        # self.y += self.speedx

        if (self.x >= 800):
            self.x = 0
        
        if (self.y >= 800):
            self.y = 0
        
        if (self.x <= 0):
            self.x = 800
        
        if (self.y <= 0):
            self.y = 800
        self.color = number_to_rgb(sigmoid(sum(self.weight) * 8290687.5) + (sigmoid(sum(self.bias)) * 8290687.5))
        self.rect = [self.x ,self.y]
        
    
    def select(self):
        """
        The select function appends the weight and bias of an agent to their respective lists if their
        y-coordinate is less than or equal to 400.
        """
        if eval(selectionMethod) :
            selectedAgentWeight.append(self.weight)
            selectedAgentBias.append(self.bias)

    def draw(self):
        """
        This function draws a circle on the screen with a given color and size.
        """
        pg.draw.circle(screen, self.color, self.rect, 20)
    
    def iferror(self, error):
        if error == IndexError:
            selectedAgentWeight.append(self.weight)
            selectedAgentBias.append(self.bias)

color = 0
generation = 0
print("Generation {}".format(generation))
agents  = [Agent(list(uniform(-100, 100) for _ in range(6)), list(uniform(-100, 100) for _ in range(2))) for _ in range(live)]
# agents  = [Agent(tinker_with_list([-986.20374217813, -444.26044688792985, 739.5841680922665, -1149.1187791257114, 156.8011866739828, 104.36413993738942, -486.2733554874085, 423.07512852853745, 310.46407767584367, -351.30259920757857, -748.8394129907994, -205.47428015859109], 1), tinker_with_list([-233.21585985290824, -478.39176290818534, 1039.7193442582477, -301.0004826147329, 49.32655662691883], 1)) for _ in range(live)]

current_time = 0
last_time = 0

selectedAgentWeight = []
selectedAgentBias = []
temp = []

while True:
    # The code block `for event in pg.event.get(): if event.type == pg.QUIT: pg.quit(); break` is
    # responsible for handling the event of the user closing the game window.
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit(); break
    
    current_time = pg.time.get_ticks()
    if current_time - last_time > time * 1000:
        selectedAgentWeight = []
        selectedAgentBias = []
        temp = []
        for agent in agents:
            agent.select()
        death = 0
        try:
            agents  = [Agent(tinker_with_list(combine_list(choice(selectedAgentWeight), choice(selectedAgentWeight)), mutationOffset), tinker_with_list(combine_list(choice(selectedAgentBias), choice(selectedAgentBias)), mutationOffset)) for _ in range(live)]
            death = live - len(selectedAgentBias)
        except IndexError:
            for agent in agents:
                agent.iferror(IndexError)
            if randint(0, 100) > mutationChance:
                agents  = [Agent(tinker_with_list(combine_list(choice(selectedAgentWeight), choice(selectedAgentWeight)), mutationOffset), tinker_with_list(combine_list(choice(selectedAgentBias), choice(selectedAgentBias)), mutationOffset)) for _ in range(live)]
            death = live
        
        generation += 1
        print("Generation {}".format(generation))
        print("Weight Average = {}".format(average_list(selectedAgentWeight)))
        print("Bias Average = {}".format(average_list(selectedAgentBias)))
        print("Death = {}".format(death))
        print("Death Percent = {}%".format(death / live * 100))
        last_time = pg.time.get_ticks()
        
    
    for agent in agents:
        agent.run()

    screen.fill((0, 255, 255))

    for agent in agents:
        agent.draw()

    pg.display.update()
    clock.tick(60)
