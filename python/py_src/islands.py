def get_neighbours(start_point, grid):
    deltas = [(+1, 0), (-1, 0), (0, +1), (0, -1)]
    y,x = start_point
    neighbours = []
    for y_delta, x_delta in deltas:
            ny, nx = y + y_delta , x + x_delta
            if ny < len(grid) and nx < len(grid[0]) and ny >= 0 and nx >= 0:
                neighbours.append((ny, nx))
    return neighbours

def updateContiguousIsland(start_point, grid):
    next_points = [start_point]
    
    while next_points:
        next_point = next_points.pop()
        if grid[next_point[0]][next_point[1]] == "0":
            continue
        grid[next_point[0]][next_point[1]] = "0"
        neighbours = [n for n in get_neighbours(next_point, grid) if grid[n[0]][n[1]] == "1"]
        print(neighbours)
        for n in neighbours:
            next_points.insert(0, n)

    return



def numIslands(grid):
    # Find the first point of land (breadth first)
        # Find the entirety of the island and mark it depth first
        # If you encounter a point on a previously marked island, then update all the points associated with that island to the original island number
    island_ct = 0
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == "1":
                # Start finding the entirety of the island                    
                updateContiguousIsland((y,x), grid)
                island_ct += 1
                print(island_ct)
    return island_ct

                    

if __name__ == '__main__':
    grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
  #  assert numIslands(grid) == 1

    grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
  #  assert numIslands(grid) == 3
                    
    grid2 = [["1","1","1","1","1","0","1","1","1","1","1","1","1","1","1","0","1","0","1","1"],["0","1","1","1","1","1","1","1","1","1","1","1","1","0","1","1","1","1","1","0"],["1","0","1","1","1","0","0","1","1","0","1","1","1","1","1","1","1","1","1","1"],["1","1","1","1","0","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],["1","0","0","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],["1","0","1","1","1","1","1","1","0","1","1","1","0","1","1","1","0","1","1","1"],["0","1","1","1","1","1","1","1","1","1","1","1","0","1","1","0","1","1","1","1"],["1","1","1","1","1","1","1","1","1","1","1","1","0","1","1","1","1","0","1","1"],["1","1","1","1","1","1","1","1","1","1","0","1","1","1","1","1","1","1","1","1"],["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],["0","1","1","1","1","1","1","1","0","1","1","1","1","1","1","1","1","1","1","1"],["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],["1","1","1","1","1","0","1","1","1","1","1","1","1","0","1","1","1","1","1","1"],["1","0","1","1","1","1","1","0","1","1","1","0","1","1","1","1","0","1","1","1"],["1","1","1","1","1","1","1","1","1","1","1","1","0","1","1","1","1","1","1","0"],["1","1","1","1","1","1","1","1","1","1","1","1","1","0","1","1","1","1","0","0"],["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"]]
    print(numIslands(grid2))