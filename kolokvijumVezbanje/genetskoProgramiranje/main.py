import random
import matplotlib.pyplot as plt

# solving (a op_1 b) op_2 (c op_3 d) = s
# we need to find a, b, c, d, op_n for the given s
# a, b, c, d e [-20, 20]
# op_1/2/3 e [+, -, *]
TARGET_FITNESS = 5000
POPULATION_SIZE = 200
MAX_ITERATIONS = 5000
NUMBER_OF_BEST_UNITS = 40

class Unit:
    def __init__(self):
        self.code = []
        for i in range(3):
            self.code.append(self.get_random_operator())
        
        for i in range(4):
            self.code.append(self.get_random_value())
        
        self.fitness = self.fitness_function()

    def __lt__(self, other):
        selfDiff = abs(self.fitness - TARGET_FITNESS)
        otherDiff = abs(other.fitness - TARGET_FITNESS)
        return selfDiff <= otherDiff
    
    def __str__(self):
        op_1 = str(self.code[0])
        op_2 = str(self.code[1])
        op_3 = str(self.code[2])
        a = str(self.code[3])
        b = str(self.code[4])
        c = str(self.code[5])
        d = str(self.code[6])

        left = '(' + a + ' ' + op_2 + ' ' + b + ')'
        right = '(' + c + ' ' + op_3 + ' ' + d + ')'
        middle = ' ' + op_1 + ' '

        return left + middle + right

    def fitness_function(self):
        return eval(self.__str__())

    def get_random_operator(self):
        return random.choice(["+", "-", "*"])
    
    def get_random_value(self):
        return random.randrange(-20, 20)
        

def mutation(unit):
    for i in range(7):
        if random.random() > 0.1:
            continue
        if i < 3:
            unit.code[i] = unit.get_random_operator()
        else:
            n = unit.code[i]
            unit.code[i] = random.randrange(n - 10, n + 10)
    
    unit.fitness = unit.fitness_function()

def calculateSubTree(i, subtree):
    if i < 7:
        subtree.append(i)
        calculateSubTree(2*i + 1, subtree)
        calculateSubTree(2*i + 2, subtree)

def crossover(parent_1, parent_2):
    subtree = []
    child_1 = Unit()
    child_2 = Unit()

    idx = random.randrange(7)
    calculateSubTree(idx, subtree)

    for i in range(7):
        child_1.code[i] = parent_2.code[i] if i in subtree else parent_1.code[i]
        child_2.code[i] = parent_1.code[i] if i in subtree else parent_2.code[i]
    child_1.fitness_function()
    child_2.fitness_function()

    return child_1, child_2

def selection(population):
    best_idx = -1
    best_fitness = float('-inf')

    for i in range(6):
        random_idx = random.randrange(POPULATION_SIZE)
        if(abs(population[random_idx].fitness - TARGET_FITNESS) < best_fitness):
            best_fitness = abs(population[random_idx].fitness - TARGET_FITNESS)
            best_idx = random_idx
    return best_idx

def main():
    population = []
    for i in range(POPULATION_SIZE):
        population.append(Unit())

    best_fitness_so_far = []

    for it in range(MAX_ITERATIONS):
        print("Current iteration: ", it)

        population.sort()
        new_population = []
        
        best_fitness_so_far.append(population[0].fitness)
        if(population[0].fitness == TARGET_FITNESS):
            break
    
        for i in range(NUMBER_OF_BEST_UNITS):
            new_population.append(population[i])
        
        for i in range(NUMBER_OF_BEST_UNITS, POPULATION_SIZE, 2):
            idx_1 = selection(population)
            idx_2 = selection(population)

            child_1, child_2 = crossover(population[idx_1], population[idx_2])
            mutation(child_1)
            mutation(child_2)

            new_population.append(child_1)
            new_population.append(child_2)
        
        population = new_population
            

    print("Best unit: ", population[0])
    print("Best fitness: ", population[0].fitness)


    plt.plot(list(range(1,len(best_fitness_so_far)+1)), best_fitness_so_far)
    plt.xlabel('Number of iterations')
    plt.ylabel('Fitness')
    plt.yscale('log')
    plt.show()

if __name__ == "__main__":
    main()