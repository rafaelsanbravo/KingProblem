import random

def get_possible_moves(x, y):
    moves = []
    for x_move in [-1, 0, 1]:
        for y_move in [-1, 0, 1]:
            if (x_move, y_move) != (0, 0):
                moves.append((x + x_move, y + y_move))
                
    possible_moves = []
    for new_x, new_y in moves:
        if 0 <= new_x < 4 and 0 <= new_y < 4:
            possible_moves.append((new_x, new_y))
            
    return possible_moves

    
board = [[0,0,0,0],[0,0,0,0],[0,0,-0.04,0],[0,0,1,-0.1]]
start = (random.randint(0, 3), random.randint(0, 3))


print(f"board {board}")
print(f"start {start}")

print(get_possible_moves(start[0], start[1]))