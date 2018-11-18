from fishing_simulator.models.fish import Fish

import random

class Shoal:
    def __init__(self, population, ocean):
        self.fish=[Fish(random.randint(0,100),
                        random.randint(0,10),
                        [random.randint(ocean.min_x, ocean.max_x), random.randint(ocean.min_y, ocean.max_y)])
                   for fish in range(population)]
        self.ocean_side_length = ocean.side_length

    def move(self, distance):
        x_move_percent = random.randint(0,100)/100
        x_pos_or_negative = random.choice ([-1, 1])
        y_pos_or_negative = random.choice([-1, 1])
        for fish in self.fish:
            fish.x_coord += x_move_percent * x_pos_or_negative
            fish.y_coord += (1 - x_move_percent) * y_pos_or_negative
            if fish.x_coord > self.ocean_side_length:
                fish.x_coord = self.ocean_side_length
            elif fish.x_coord < 0:
                fish.x_coord = 0
            if fish.y_coord > self.ocean_side_length
                fish.y_coord = self.ocean_side_length
            elif fish.y_coord < 0:
                fish.y_coord = 0


