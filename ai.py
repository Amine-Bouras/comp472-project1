import numpy as np

def manhattan(start_state, goal_state):
    
    all_values = "12345678"

    for values in all_values:
        temp_position_x_final = np.argwhere(goal_state == values)[0][0]
        temp_position_y_final = np.argwhere(goal_state == values)[0][1]
        temp_position_x_start = np.argwhere(start_state == values)[0][0]
        temp_position_y_start = np.argwhere(start_state == values)[0][1]
        delta_y = temp_position_y_final - temp_position_y_start
        delta_x = temp_position_x_final - temp_position_x_start
        totalsum = delta_x +delta_y

    return totalsum

def hamming(start_state, goal_state):

    count = 0
    for i in range(len(start_state)):
        if start_state[i] != goal_state[i]:
            count += 1          
    return count

def successor_generator(current_state):
    temp_position_x = np.argwhere(current_state == "B")[0][0]
    temp_position_y = np.argwhere(current_state == "B")[0][1]
    state_list = []

    if temp_position_x < 2:
        
        temp_string = current_state[temp_position_x + 1][temp_position_y]
        current_state[temp_position_x + 1][temp_position_y] = "B"
        current_state[temp_position_x][temp_position_y] = temp_string

    return current_state
    # if temp_position_x > 0:
        
    # if temp_position_y < 2:

    # if temp_position_y > 0:
        

def main():

    start_state_puzzle = list("182365B47")
    goal_state_puzzle = list("1238B4765")
    goal_state_puzzle_array = np.array(goal_state_puzzle).reshape((3,3))
    start_state_puzzle_array = np.array(start_state_puzzle).reshape((3,3))
    print(successor_generator(start_state_puzzle_array))
    


if __name__ == '__main__':
    main()

    



