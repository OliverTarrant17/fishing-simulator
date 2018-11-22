class Ocean:
    def __init__(self, side_length):
        self.side_length = side_length
        self.min_x = 0
        self.max_x = side_length
        self.min_y = 0
        self.max_y = side_length

    def interior(self):
        list_of_coords = [[[x, y] for x in range(self.side_length)] for y in range(self.side_length)]
        flattened_list = []
        for sub_list in list_of_coords:
            for sub_sub_list in sub_list:
                flattened_list.append(sub_sub_list)
        return flattened_list

    def  fish_per_unit_square(self, shoal):
        list_of_densities = []
        ocean_interior = self.interior()
        list_of_fish_coords = [[int(fish.x_coord), int(fish.y_coord)] for fish in shoal.fish]
        for coords in ocean_interior:
            count = list_of_fish_coords.count(coords)
            list_of_densities.append([coords, count])
        return list_of_densities

