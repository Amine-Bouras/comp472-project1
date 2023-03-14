import numpy as np
from copy import deepcopy


def main():

    start_state_puzzle = list("7421B5863")
    goal_state_puzzle = list("12345678B")
    goal_state_puzzle_array = np.array(goal_state_puzzle).reshape((3,3))
    start_state_puzzle_array = np.array(start_state_puzzle).reshape((3,3))
    general_search(start_state_puzzle_array, goal_state_puzzle_array, best_first, manhattan)

def general_search(start_state, goal_state, search_type, heuristics = None):

    if heuristics == None:
        search_type(start_state, goal_state)
    if heuristics != None:
        search_type(start_state, goal_state, heuristics)

def a_star(start_state, goal_state, heuristics):
    open_list = [start_state]
    closed_list = []

    while open_list:
        current_state = np.array(open_list.pop(0))
        closed_list.append(current_state)
        print(current_state)
        print("\n")

        if np.array_equal(current_state, goal_state):
            print(current_state)
            print("\n")
            return current_state

        for values in successor_generator(current_state):
            not_in_closed_list = True
            not_in_open_list = True

            for state in closed_list:
                if np.array_equal(values, state):
                    not_in_closed_list = False
                    
            for state in open_list:
                if np.array_equal(values,state):
                    not_in_open_list = False
                    
            if not_in_closed_list and not_in_open_list:
                open_list.append(values)
        
        open_list = sorted(open_list, key = lambda h: heuristics(h, goal_state))


def best_first(start_state, goal_state, heuristics):

    open_list = [start_state]
    closed_list = []

    while open_list:
        current_state = np.array(open_list.pop(0))
        closed_list.append(current_state)
        print(current_state)
        print("\n")

        if np.array_equal(current_state, goal_state):
            print(current_state)
            print("\n")
            return current_state

        for values in successor_generator(current_state):
            not_in_closed_list = True
            not_in_open_list = True

            for state in closed_list:
                if np.array_equal(values, state):
                    not_in_closed_list = False
                    
            for state in open_list:
                if np.array_equal(values,state):
                    not_in_open_list = False
                    
            if not_in_closed_list and not_in_open_list:
                open_list.append(values)
        
        open_list = sorted(open_list, key = lambda h: heuristics(h, goal_state))
        

def depth_first(start_state, goal_state):

    open_list = [start_state]
    closed_list = []

    while open_list:
        current_state = np.array(open_list.pop())
        closed_list.append(current_state)
        print(current_state)
        print("\n")
        if np.array_equal(current_state, goal_state):
            print(current_state)
            return current_state
        for values in successor_generator(current_state):
            not_in_closed_list = True
            not_in_open_list = True

            for state in closed_list:
                if np.array_equal(values, state):
                    not_in_closed_list = False
                    
            for state in open_list:
                if np.array_equal(values,state):
                    not_in_open_list = False
                    
            if not_in_closed_list and not_in_open_list:
                open_list.append(values)

            

def breadth_first(start_state, goal_state):

    open_list = [start_state]
    closed_list = []

    while open_list:
        current_state = np.array(open_list.pop(0))
        closed_list.append(current_state)
        print(current_state)
        print("\n")

        if np.array_equal(current_state, goal_state):
            # print(current_state)
            return current_state
        for values in successor_generator(current_state):
            not_in_closed_list = True
            not_in_open_list = True

            for state in closed_list:
                if np.array_equal(values, state):
                    not_in_closed_list = False
                    
            for state in open_list:
                if np.array_equal(values,state):
                    not_in_open_list = False
                    
            if not_in_closed_list and not_in_open_list:
                open_list.append(values)

def manhattan(current_state, goal_state):
    
    all_values = "12345678"
    totalsum = 0
    
    for values in all_values:
        temp_position_x_final = np.argwhere(goal_state == values)[0][0]
        temp_position_y_final = np.argwhere(goal_state == values)[0][1]
        temp_position_x_start = np.argwhere(current_state == values)[0][0]
        temp_position_y_start = np.argwhere(current_state == values)[0][1]
        delta_y = abs(temp_position_y_final - temp_position_y_start)
        delta_x = abs(temp_position_x_final - temp_position_x_start)
        sum = delta_x + delta_y
        totalsum = totalsum + sum

    return totalsum

def hamming(start_state, goal_state):

    count = 0
    for i in range(len(start_state)):
        for j in range(len(start_state)):
            if start_state[i][j] != goal_state[i][j]:
                count += 1          
    return count

def successor_generator(current_state):
    temp_position_y = np.argwhere(current_state == "B")[0][0]
    temp_position_x = np.argwhere(current_state == "B")[0][1]
    state_list = []

    if temp_position_x < 2:
        temp_state = deepcopy(current_state)
        temp_string = temp_state[temp_position_y][temp_position_x + 1]
        temp_state[temp_position_y][temp_position_x + 1] = "B"
        temp_state[temp_position_y][temp_position_x] = temp_string
        state_list.append(temp_state)

    if temp_position_x > 0:
        temp_state = deepcopy(current_state)
        temp_string = temp_state[temp_position_y][temp_position_x - 1]
        temp_state[temp_position_y][temp_position_x - 1] = "B"
        temp_state[temp_position_y][temp_position_x] = temp_string
        state_list.append(temp_state)
        
    if temp_position_y < 2:

        temp_state = deepcopy(current_state)
        temp_string = temp_state[temp_position_y + 1][temp_position_x]
        temp_state[temp_position_y + 1][temp_position_x] = "B"
        temp_state[temp_position_y][temp_position_x] = temp_string
        state_list.append(temp_state)

    if temp_position_y > 0:

        temp_state = deepcopy(current_state)
        temp_string = temp_state[temp_position_y - 1][temp_position_x]
        temp_state[temp_position_y - 1][temp_position_x] = "B"
        temp_state[temp_position_y][temp_position_x] = temp_string
        state_list.append(temp_state)
    
    return state_list
        

if __name__ == '__main__':
    main()

    



