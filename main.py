"""
In this script I attempt to solve the Data Science / AI Challenge
 
I decided to use A* Search to find the highest reward
f = g + h
f: total cost
g: actual cost
h(heuristic): estimated cost

The main function uses the following logic:
Explore all the adjacent cells for the current position, 
if not visited before calculate f for that position,
next iteration get the position with the lowest f,
if the reward is better update the optimal position,
finish the loop when the list is empty or the counter reaches the specified steps.

"""
def get_possible_moves(x, y):
    moves = []
    for x_move in [-1, 0, 1]:
        for y_move in [-1, 0, 1]:
            moves.append((x + x_move, y + y_move))
                
    possible_moves = []
    for new_x, new_y in moves:
        if 0 <= new_x < 4 and 0 <= new_y < 4:
            possible_moves.append((new_x, new_y))
            
    return possible_moves

    
def find_highest_reward_coordinates(chess_board:list[list[float]], starting_point:tuple, steps=30):
    visited = []
    optimal_position = starting_point
    main_list = [(0, starting_point, 0)]
    counter = 0

    while main_list and counter < steps:
        main_list.sort(key=lambda x: x[0])
        f, (x, y), g = main_list.pop(0)

        if (x, y) in visited:
            continue
        
        visited.append((x, y))
        

        if chess_board[x][y] > chess_board[optimal_position[0]][optimal_position[1]]:
            optimal_position = (x, y)
            counter = 0
            
        else:
            counter += 1

        for adjacent_x, adjacent_y in get_possible_moves(x, y) + [(x, y)]:
            if (adjacent_x, adjacent_y) not in visited:
                new_g = g + chess_board[adjacent_x][adjacent_y]
                new_f = new_g - chess_board[adjacent_x][adjacent_y]
                main_list.append((new_f, (adjacent_x, adjacent_y), new_g))

    return optimal_position