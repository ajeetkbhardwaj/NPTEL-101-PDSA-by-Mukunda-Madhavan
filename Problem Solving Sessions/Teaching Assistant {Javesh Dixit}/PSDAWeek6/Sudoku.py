
#### http://pi.math.cornell.edu/~mec/Summer2009/Mahmood/Home.html   Read more about sudoku here.

### Checking if filled entry is correct or not for the given row and column
def IsFilled(prob, row, col, n):

    ## Checking if element is present anywhere else in the given row
    for i in range(box_len):
	    if prob[row][i] == n:
	        return False
    ## Checking if element is present anywhere else in the given row
    for i in range(box_len):
        if prob[i][col] == n:
            return False

    ## Checking if element is present anywhere else in the sub-square (that contains 9 boxes)
    startRow = row - row % 3
    startCol = col - col % 3
    for i in range(3):
        for j in range(3):
            if prob[i + startRow][j + startCol] == n:
                return False
    return True

##### Solving for all the rows and columns for unfilled boxes
def SolveSudoku(prob, row, col):

	if row == box_len-1 and col == box_len:
		return True

	if col == box_len:
		row = row + 1
		col = 0
    ## Checking if a box is already filled
	if prob[row][col] > 0:
		return SolveSudoku(prob, row, col + 1)
    ### for unfilled box checking entries from '1' to '9' for validity
	for n in range (1, box_len+1, 1):

		if IsFilled(prob, row, col, n):

			prob[row][col] = n


			if SolveSudoku(prob, row, col+1):
				return True

		prob[row][col] = 0

	return False

def print_soln(prob):
    print ('----------------------')
    for i in range(box_len):
        for j in range(box_len):
            if (j+1)%3 == 0:
                print(prob[i][j], end = " | ")
            else:
                print(prob[i][j], end = "|")
        if (i+1)%3 == 0:   
            print('\n----------------------')
        else:
            print()

box_len = 9

# prob = [[0, 0, 0,   0, 0, 3,    0, 0, 2],
#         [0, 5, 0,   0, 0, 0,    0, 0, 0],
#         [7, 0, 4,   6, 0, 0,    1, 0, 0],
        
#         [0, 8, 0,   9, 0, 0,    0, 0, 0],
#         [0, 6, 0,   0, 0, 0,    5, 0, 0],
#         [9, 0, 5,   0, 2, 0,    0, 0, 1],
        
#         [8, 0, 0,   0, 0, 0,    0, 0, 0],
#         [0, 0, 0,   0, 6, 0,    0, 7, 0],
#         [1, 0, 9,   7, 0, 0,    4, 0, 0]]


with open("Sudoku_prob.txt", "r") as f:
    prob = [[int(x) for x in line.split()] for line in f]
print('Sudoku Problem')
print_soln(prob)

print('Sudoku Solution') 
if (SolveSudoku(prob, 0, 0)):
    print_soln(prob)
else:
    print("no solution  exists ")





