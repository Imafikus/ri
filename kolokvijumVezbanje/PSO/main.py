import random

# finding a given number which should be the result of adding 3 values
# X + Y + Z = SUM, we are finding X, Y, Z
MAX_ITERATIONS = 2000
MAX_VELOCITY = 10
TARGET_VALUE = 100

NUM_OPERANDS = 3
NUM_PARTICLES = 5

MIN_RANGE = 149
MAX_RANGE = 190

class Particle:
    def __init__(self):
        self.position = self.generate_position()
        self.velocity = 0.0
        self.current_value = self.calculate_value()
        self.best_value = self.calculate_value()

    def generate_position(self):
        position = []
        for i in range(NUM_OPERANDS):
            position.append(random.randrange(MIN_RANGE, MAX_RANGE))
        return position

    def calculate_value(self):
        value = 0
        for c in self.position:
            value += c
        return value

    def is_better_than_provided_value(self, value):
        if abs(self.current_value - TARGET_VALUE) < (value - TARGET_VALUE):
            return True
        else:
            return False

    def update_velocity(self, global_best):
        self.velocity += 2.0 * random.random() * (self.best_value - self.current_value) + 2.0 * random.random() * (global_best - self.current_value)

        if self.velocity > MAX_VELOCITY:
            self.velocity = MAX_VELOCITY
        
        if self.velocity < -MAX_VELOCITY:
            self.velocity = -MAX_VELOCITY

    def update_position(self, global_best):
        for i in range(NUM_OPERANDS):
            self.position[i] += int(self.velocity)
        
        self.current_value = self.calculate_value()

        if self.is_better_than_provided_value(self.best_value):
            self.best_value = self.current_value

        if self.is_better_than_provided_value(global_best):
            global_best = self.current_value
        
        return global_best

    def __str__(self):
        to_str = str(self.position[0]) + ' + ' + str(self.position[1]) +  ' + ' + str(self.position[2]) + ' = ' + str(self.current_value)
        return to_str
        
def update_all_velocities(particles,global_best):
    for p in particles:
        p.update_velocity(global_best)

def update_all_positions(particles,global_best):
    for p in particles:
        global_best = p.update_position(global_best)

    return global_best

def print_particles(particles):
    for p in particles:
        print(p)

def main():
    global_best = 100000
    particles = []

    for i in range(NUM_PARTICLES):
        particles.append(Particle())
        if particles[i].is_better_than_provided_value(global_best):
            global_best = particles[i].current_value

    for i in range(MAX_ITERATIONS):
        if global_best == TARGET_VALUE:
            break
        
        update_all_velocities(particles, global_best)
        global_best = update_all_positions(particles, global_best)
    
    print("Final iteration: ")
    print_particles(particles)

    

if __name__ == "__main__":
    main()
