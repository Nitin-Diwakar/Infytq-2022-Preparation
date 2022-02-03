"""
You are given an array of N integers, A1, A2 ,…, AN and an integer K. Return the of count of distinct numbers in all windows of size K.

Formally, return an array of size N-K+1 where i’th element in this array contains number of distinct elements in sequence Ai, Ai+1 ,…, Ai+k-1.

Note: If K > N, return empty array.

Input :

A = [1, 2, 1, 3, 4, 3]
K = 3

Output :

[2, 3, 3, 2]

Explanation

All windows of size K are
[1, 2, 1]
[2, 1, 3]
[1, 3, 4]
[3, 4, 3]
"""
A = list(map(int,input().split()))

k = int(input())
ans = []

for start in range(0,len(A)-k+1):
    curr_subarray = A[start:start+k]
    curr_unqiue = len(set(curr_subarray))
    ans.append(curr_unqiue)
print(ans)