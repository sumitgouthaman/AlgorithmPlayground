import unittest
from collections import deque

def paths_in_grid(grid_size):
    """Returns no of possible paths in a square grid starting from top right
    corner to the bottom left corner (while moing in only left and bottom
    direction)
    
    Args:
      grid_size (int): The size of grid
      
    Returns:
      int: The no of possible paths
    """
    
    n = grid_size # For convenience
    
    visited = [[False for x in range(n)] for x in range(n)]
    sums = [[0 for x in range(n)] for x in range(n)]
    
    sums[0][0] = 1
    
    queue = deque()
    
    current_point = (0, 0)
    while current_point != (n - 1, n - 1):
        x, y = current_point
        if visited[x][y] == True:
            current_point = queue.popleft()
            continue
        visited[x][y] = True
        neighbors = [(x + 1, y), (x, y + 1)]
        for neighbor in neighbors:
            i, j = neighbor
            if i < n and j < n:
                sums[i][j] += sums[x][y]
                queue.append(neighbor)
        current_point = queue.popleft()
    
    return sums[n - 1][n - 1]

# Unit tests
class PathsInGridTests(unittest.TestCase):

    def test1(self):
        self.failUnless(paths_in_grid(1) == 1)

    def test2(self):
        self.failUnless(paths_in_grid(2) == 2)
    
    def test3(self):
        self.failUnless(paths_in_grid(3) == 6)
        
    def test4(self):
        self.failUnless(paths_in_grid(4) == 20)

def main():
    unittest.main()

if __name__ == '__main__':
    main()
