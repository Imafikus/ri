import random
import numpy as np
import math

MAX_VELOCITY = 100
MAX_ANGLE = 90

TOURNAMENT_SIZE = 5
POPULATION_SIZE = 20
CONST_G = 9.81

PROB_MUTATION = 0.05
PROB_SELECTION = 0.9

NUMBER_OF_GENERATIONS = 500
SELECTION_SIZE = 10
CROSSOVER_SIZE = 10



class Projectile:

    def __init__(self, angle, velocity):
        self.chromosome = [angle, velocity]    
        self.fitness = self.calculateDistance(angle, velocity)

    def calculateDistance(self, angle, velocity):
        return velocity*velocity*np.sin(np.deg2rad(2*angle)) / CONST_G
    
    def mutate(self):
        p = random.uniform(0, 1)
        if p > PROB_MUTATION:
            return

        idx = random.randrange(0, len(self.chromosome))
        single_gene = self.chromosome[idx]

        mutation_area = single_gene / 10
        single_gene = random.uniform(single_gene - mutation_area, single_gene + mutation_area)

        self.chromosome[idx] = single_gene
        self.fix_mutations()
    
    def crossover(self, other_proj):
        child = Projectile(1, 1)

        for i in range(len(self.chromosome)):
            child.chromosome[i] = random.choice([self.chromosome[i], other_proj.chromosome[i]])
        return child

    def fix_mutations(self):
        if self.chromosome[0] > MAX_ANGLE:
            self.chromosome[0] = MAX_ANGLE

        elif self.chromosome[0] < 0:
            self.chromosome[0] = 0

        if self.chromosome[1] > MAX_VELOCITY:
            self.chromosome[1] = MAX_VELOCITY

        elif self.chromosome[1] < 0:
            self.chromosome[1] = 0

    def __str__(self):
        return str(self.chromosome)


def generate_population(population):
    for _ in range(POPULATION_SIZE):
        angle = random.uniform(0, MAX_ANGLE)
        velocity = random.uniform(0, MAX_VELOCITY)
        population.append(Projectile(angle, velocity))

def tournament_selection(population):
    ids = list(range(len(population)))
    random.shuffle(ids)
    ids = ids[:TOURNAMENT_SIZE]

    best_fitness = -1
    best_id = None
    for id in ids:
        if population[id].fitness > best_fitness:            
            best_fitness = population[id].fitness
            best_id = id
    
    return population[best_id]

def selection(population):
    new_population = []
    for _ in range(10):
        new_population.append(tournament_selection(population))
    return new_population

def crossover(population):
    new_population = population[:]
    for _ in range(10):
        parent_1 = random.choice(population)
        parent_2 = random.choice(population)
        new_population.append(parent_1.crossover(parent_2))
    
    population = new_population[:]

def mutation(population):
    for unit in population:
        unit.mutate()


def find_best_fitness(population):
    best_unit = population[0]

    for i in range(1, len(population)):
        if population[i].fitness > best_unit.fitness:
            best_unit = population[i]
    return best_unit

def print_population(population):
    for unit in population:
        print(unit)

def main():
    population = []
    generate_population(population)

    # print("Starting population")
    # print_population(population)

    best_sols = []
    for _ in range(NUMBER_OF_GENERATIONS):
        new_population = selection(population)
        # print("After selection")
        # print_population(new_population)

        crossover(new_population)
        # print("After crossover")
        # print_population(new_population)

        mutation(new_population)
        # print("After mutation")
        # print_population(new_population)

        best_sols.append(find_best_fitness(new_population))
        population = new_population[:]
    
    print("Best solutions")
    print_population(best_sols)
 
if __name__ == "__main__":
    main()