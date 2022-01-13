"""
For a given list of numbers find the its factors and add the factors then if the sum of all factor is present in original list, sort it and print it
Ex:
Input: 0,1,6
Factors: 0 = 0, sum =0
1 = 1, sum =1
6 =1,2,3 = sum =6
Output: 1,6
If the sum is not present in the list then return -1.
"""

def factor(n):
    Sum = 0
    if n == 1:
        return 1
    for i in range(1,n):
        if n%i == 0:
            Sum+=i
    return Sum

arr = list(map(int, input().split(",")))
flag = 0
for i in arr:
    if factor(i) in arr:
        flag = 1
        print(i)
    if flag == 0:
        print(-1)



