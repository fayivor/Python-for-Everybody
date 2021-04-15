NUM_ROWS = 25
NUM_COLS = 25

# construct a matrix
my_matrix = []
for row in range(NUM_ROWS):
    new_row = []
    for col in range(NUM_COLS):
        new_row.append(row * col)
    my_matrix.append(new_row)
#print(my_matrix)
# print the matrix
for row in my_matrix:
    pass
    #print(row)

#print(range(len(my_matrix[0])))
# contruct a trace matrix
def trace(matrix):
    trac = []
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):

            if row == col:
                #print(matrix[row][col])
                trac.append(matrix[row][col])
    return sum(trac)

print("trace = ",trace(my_matrix) )
