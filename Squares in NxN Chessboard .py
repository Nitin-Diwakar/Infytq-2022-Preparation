"""
Find total number of Squares in a N*N cheesboard.

Example 1:

Input:
N = 1
Output:
1
Explanation:
A 1*1 chessboard has only 1 square.

Example 2:

Input:
N = 2
Output:
5
Explanation:
A 2*2 chessboard has 5 squares.
4 1*1 squares and a 2*2 square.
"""

class Solution:
    def squaresInChessBoard(self, N):
        
         # code here
        sum = 0
        for i in range(1,N+1):
            sum+=(i*i)
        return sum
if __name__ == '__main__':
    for _ in range(int(input())):
        N = int(input())
        ob = Solution()
        print(ob.squaresInChessBoard(N))