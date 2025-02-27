import random
from main import find_highest_reward_coordinates

board = [[0,0,0,0],[0,0,0,0],[0,0,-0.04,0],[0,0,1,-0.1]]
start = (random.randint(0, 3), random.randint(0, 3))

print(find_highest_reward_coordinates(board, start))

board = [[0,0,1,0],[0,0,0,0],[0,0,-0.04,0],[0,0,0,-0.1]]
start = (random.randint(0, 3), random.randint(0, 3))

print(find_highest_reward_coordinates(board, start))

