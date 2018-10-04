grid = [['.', '.', '.', '.', '.', '.'],
['.', 'O', 'O', '.', '.', '.'],
['O', 'O', 'O', 'O', '.', '.'],
['O', 'O', 'O', 'O', 'O', '.'],
['.', 'O', 'O', 'O', 'O', 'O'],
['O', 'O', 'O', 'O', 'O', '.'],
['O', 'O', 'O', 'O', '.', '.'],
['.', 'O', 'O', '.', '.', '.'],
['.', '.', '.', '.', '.', '.']]

#for i in grid:   # to print rows of matrix
#    print i
trans = [[grid[j][i] for j in range(len(grid))] for i in range(len(grid[0]))]          # to traverse matrix
print("\n") 
#for i in trans:     # to print trans of matrix
#    print(i) 

for i in range(len(trans)):
    print "\n"
    for j in range(len(trans[i])):
        print trans[i][j],                 # to print elemetns of trans matrix without list element 
