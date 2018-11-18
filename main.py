from fishing_simulator.models.ocean import Ocean
from fishing_simulator.models.fish import Fish
from fishing_simulator.models.shoal import Shoal


if __name__ == "__main__":
    INITIAL_POPULATION = input("How many fish to start with?")
    OCEAN = Ocean(100)
    FISH = Shoal(100, Ocean)

