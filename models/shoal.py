import random
import matplotlib.pyplot as plt
from models.fish import Fish


class Shoal:
    def __init__(self, population, ocean):
        self.fish=[Fish(random.randint(0,100),
                        random.randint(0,10),
                        random.randint(ocean.min_x, ocean.max_x),
                        random.randint(ocean.min_y, ocean.max_y),
                        random.choice(["M", "F"]))
                        for fish in range(population)]
        self.ocean_side_length = ocean.side_length

    def move(self, distance=1):
        for fish in self.fish:
            x_move_percent = random.randint(0, 100) / 100
            x_pos_or_negative = random.choice([-1, 1])
            y_pos_or_negative = random.choice([-1, 1])
            fish.x_coord += x_move_percent * x_pos_or_negative * distance
            fish.y_coord += (1 - x_move_percent) * y_pos_or_negative * distance
            if fish.x_coord > self.ocean_side_length:
                fish.x_coord = self.ocean_side_length
            elif fish.x_coord < 0:
                fish.x_coord = 0
            if fish.y_coord > self.ocean_side_length:
                fish.y_coord = self.ocean_side_length
            elif fish.y_coord < 0:
                fish.y_coord = 0

    def plot(self):
        # unit area ellipse
        for i in range(10):
            self.move(5)
            x = [fish.x_coord for fish in self.fish]
            y = [fish.y_coord for fish in self.fish]
            plt.scatter(x,y)
            plt.pause(1)
        plt.show()



