# taken from: https://github.com/simonbrahan/aoc2021/tree/master/09

def is_low_point(x, y, elevation):
    height = elevation[y][x]

    for neighbour_x, neighbour_y in get_neighbours(x, y, elevation):
        try:
            neighbour_height = elevation[neighbour_y][neighbour_x]
        except:
            print(neighbour_x, neighbour_y)

        if neighbour_height <= height:
            return False

    return True


def get_basin_size(x, y, elevation):
    def get_basin_extent(x, y, elevation, basin_points):
        if (x, y) in basin_points:
            return basin_points

        if elevation[y][x] == 9:
            return basin_points

        basin_points.add((x, y))

        for neighbour_x, neighbour_y in get_neighbours(x, y, elevation):
            basin_points = get_basin_extent(neighbour_x, neighbour_y, elevation, basin_points)

        return basin_points

    basin_extent = get_basin_extent(x, y, elevation, set())

    return len(basin_extent)


def elevation_from_file(filepath):
    with open(filepath) as f:
        elevation = [[int(char) for char in line.strip()] for line in f]

    return elevation


def get_neighbours(x, y, elevation):
    directions = [(-1, 0), (0, -1), (0, 1), (1, 0)]

    out = []
    for add_x, add_y in directions:
        neighbour_x = x + add_x
        neighbour_y = y + add_y

        if 0 <= neighbour_y < len(elevation) and 0 <= neighbour_x < len(elevation[neighbour_y]):
            out.append((neighbour_x, neighbour_y))

    return out

from math import prod

elevation = elevation_from_file('2021/Day9/Day9_input.txt')
# elevation = elevation_from_file('2021/Day9/Day9_test_input.txt')

basin_sizes = []

for y, row in enumerate(elevation):
    for x, height in enumerate(row):
        if is_low_point(x, y, elevation):
            basin_sizes.append(get_basin_size(x, y, elevation))

print(prod(sorted(basin_sizes)[-3:]))