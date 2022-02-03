"""
Input a Matrix, check if do we get the same number consecutively at least 4 times in any fashion(Vertically, horizontally, diagonally). Record those sets.

If we get multiple values, then print minimum of them. And if no such consecutive number then print -1.

Input: 6 6

1 3 3 3 3 9
1 6 9 2 3 9
1 2 2 5 4 9
2 2 4 5 7 9
2 4 5 6 7 2
1 2 3 4 5 6

Output: 2
"""

row,col = map(int,input().split())
Matrix = []
for i in range(row):
    row_no = list(map(int,input().split(" ")))
    Matrix.append(row_no)

result = []
for i in range(row):
    for j in range(col):
        if j < col-3: # for consecutive number in all rows
            if Matrix[i][j] == Matrix[i][j+1] == Matrix[i][j+2] == Matrix[i][j+3]:
                result.append(Matrix[i][j])
        
        if i < row-3: #for consecutive number in all cols
            if Matrix[i][j] == Matrix[i+1][j] == Matrix[i+2][j] == Matrix[i+3][j]:
                result.append(Matrix[i][j])
        
        if i >=3 and j >=3: # consecutive number in all left to right diagonal
            if Matrix[i][j] == Matrix[i-1][j-1] == Matrix[i-2][j-2] == Matrix[i-3][j-3]:
                result.append(Matrix[i][j]) 
                
        if i >=3 and j < col-3: # consecutive number in all right to left diagonal
            if Matrix[i][j] == Matrix[i-1][j+1] == Matrix[i-2][j+2] == Matrix[i-3][j+3]:
                result.append(Matrix[i][j]) 
if len(result) == 0:
    print(-1)
else:
    print(min(result))
