import random
import numpy as np
import matplotlib.pyplot as plt


best_solutions_so_far = []

LEFT_BOUNDARY = -10
RIGHT_BOUNDARY = 10
NEIGBOURHOOD = 0.1
MAX_ITER = 1000
EPSILON = 1e-3

def apply_function(x):
    """
    function f(x) = x^2
    """
    return x*x

def temperature_function(x):
    return 1/np.sqrt(x)

def get_random_staring_value():
    return random.uniform(LEFT_BOUNDARY, RIGHT_BOUNDARY)

def get_random_value_near_current_solution(x):
    left = x - NEIGBOURHOOD
    right = x + NEIGBOURHOOD

    if left < LEFT_BOUNDARY:
        left = LEFT_BOUNDARY
    if right > RIGHT_BOUNDARY:
        right = RIGHT_BOUNDARY
    
    return random.uniform(left, right)

def should_choose_new_solution(current_solution, possible_solution, p, q):

    if apply_function(possible_solution) < apply_function(current_solution):
        return True
    elif apply_function(possible_solution) >= apply_function(current_solution) and p > q:
        return True
    else:
        return False

def main():
    current_solution = get_random_staring_value()
    best_solutions_so_far.append(current_solution)
    num_of_iterations = 1

    while num_of_iterations < MAX_ITER:
        print("Current iteration: ", num_of_iterations)
        print("Current best solution: ", current_solution)

        p = temperature_function(num_of_iterations)
        q = random.uniform(0, 1)
        possible_solution = get_random_value_near_current_solution(current_solution)

        if should_choose_new_solution(current_solution, possible_solution, p, q):
            current_solution = possible_solution
        
        best_solutions_so_far.append(current_solution)
        
        num_of_iterations += 1
    
    plt.plot(list(range(1,1001)), best_solutions_so_far)
    plt.xlabel('Number of iterations')
    plt.ylabel('Current minimum')
    plt.show()




if __name__ == "__main__":
    main()