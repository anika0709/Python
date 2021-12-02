# def get_islands(grid):
#     recs = 0
#     #ans = []
#     rows = len(grid)
#     cols = len(grid[0])
#     def dfs(row,col):
        
#         if row in range(rows) and col in range(cols) and grid[row][col] == '1':
#             grid[row][col] = '0'
#             dfs(row-1,col)
#             dfs(row+1,col)
#             dfs(row,col-1)
#             dfs(row,col+1)
#         else:
#             return
            

#     for i in range(rows):
#         for j in range(cols):
#             if grid[i][j] == '1':
#                 dfs(i,j)
#                 recs += 1
#     return recs

import collections
# grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]
# grid = [
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]

def get_islands(grid):
    recs = 0
    #ans = []
    rows = len(grid)
    cols = len(grid[0])
    def bfs(i,j):
        grid[i][j] ='-1'
        coord = []
        q = collections.deque()
        q.append([i,j])
        coord.append([i,j])

        while q:
            r,c = q.popleft()
            directions = [(r-1,c),(r+1,c),(r,c-1),(r,c+1)]
            for dr,dc in directions:
                if (dr) in range(rows) and (dc) in range(cols) and grid[dr][dc] == '1' :
                    q.append([dr,dc])
                    coord.append([dr,dc])
                    grid[dr][dc] ='-1'
        return([coord[0],coord[-1]])
    ans = []
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == '1':
                coord = bfs(i,j)
                ans.append(coord)

                recs += 1
    print(ans)
    return recs

print(get_islands(grid))

grid = [[ '0', '0', '0', '0'],
[ '0', '1', '1', '0'],
[ '0', '1', '1', '0'],
[ '0', '0', '0', '0']]
print(get_islands(grid))
# Expected output: [['1',1], [2,2]]

grid = [[0, '0', '0', '0'],
['0', 0, 0, '0'],
['0', 0, 0, '0'],
['0', '0', '0', '0']]
# Expected output: [ [[0,0],[0,0]], [['1',1], [2,2]] ]
print(get_islands(grid))





