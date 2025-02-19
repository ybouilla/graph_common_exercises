# count the islands
# https://www.giulianopertile.com/blog/the-definitive-guide-to-graph-problems/
grid = [
    ["W", "L", "W", "W", "L", "L"],
    ["W", "W", "W", "W", "W", "W"],
    ["W", "W", "W", "W", "L", "W"],
    ["W", "L", "L", "W", "L", "L"],
    ["W", "L", "L", "W", "L", "W"],
    ["W", "W", "W", "W", "W", "W"],
]

def count_island(map_sea):
    visited = []
    nb_islands = 0
    biggest_island_size = 0
    
    for r in range(len(map_sea)):
        for c, c_val in enumerate(map_sea[r]):
            if c_val == "L" and (r, c) not in visited:
                # land detected
                #visited.append((r, c))

                island_size = bfs(map_sea, r, c, visited)
                biggest_island_size = max(island_size, biggest_island_size)
                nb_islands += 1
    return nb_islands, biggest_island_size

def bfs(grid, r, c, visited):
    queue = [(r, c)]
    island_size =0
    while len(queue) > 0:
        
        new_r, new_c = queue.pop(0)
  
        if (new_r, new_c) not in visited:
            visited.append((new_r, new_c))

            if grid[new_r] [new_c] =='L':
                island_size += 1
                # get neighboours
                neighs = get_neighbors(grid, new_r, new_c)
                
                for neigh in neighs:
                    queue.append(neigh)
    return island_size

def get_neighbors(grid, row, col):
    # collect nodes around the underrstudied node
    neighbors = []
    # up
    if row > 0:
        neighbors.append((row-1, col))
    # down
    if row + 1 < len(grid):
        neighbors.append((row+1, col))
    # left
    if col > 0:
        neighbors.append((row, col - 1))
    # right
    if col +1 < len(grid[0]):
        neighbors.append((row , col+1))

    return neighbors


print("ex3: coiunt island")
print(count_island(grid))