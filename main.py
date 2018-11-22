from models.ocean import Ocean
from models.shoal import Shoal
import matplotlib.pyplot as plt
from actions.actions import animated_plot


if __name__ == "__main__":
    INITIAL_POPULATION = int(input("How many fish to start with?"))
    OCEAN = Ocean(3)
    for i in range(10):
        FISH = Shoal(INITIAL_POPULATION, OCEAN)
        print(OCEAN.fish_per_unit_square(FISH))
        FISH.move(1)



