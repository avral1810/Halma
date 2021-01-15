import copy
import time
import math
from Game import Game
from DataHolder import DataHolder



inputData = DataHolder("input.txt")
game = Game(inputData)
game.play()