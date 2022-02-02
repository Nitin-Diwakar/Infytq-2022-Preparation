"""
Number of odd sub arrays. Find the number of distinct subarrays in an array of position integers such that the sum of the subarray is an odd integer, two subarrays are considered different if they either start or end at different index.

Input:
1
3
1 2 3
Output:4

Explanation: subarrays [[1], [1, 2], [1, 2, 3], [2], [2, 3], [3]]
"""

a = int(input())
b = int(input())
ar = [i for i in range(a,b+1)]
print(ar)
cnt=0
for i in range(len(ar)):
    for j in range(i,len(ar)):
        if sum(ar[i:j+1])%2!=0:
            cnt+=1
print(cnt)


