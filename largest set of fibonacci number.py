"""
Given an array with positive number(comma seperated) the task is that we find largest subset from array that constain elements which are Fibonacci Numbers.

If more than two elements exist then print its length else print -1

Input: 3,2,5,8,9,10,11
Output: 4  i.e.([2,3,5,8])

Input: 2,6,3,5,8,9
output: 4   i.e.([2,3,5,8])
"""

from operator import le


array = list(map(int,input().split(",")))
x = max(array)

a,b = 0,1
fibo = [0,1]
count = 0
while count <= x:
    c = a+b
    a = b
    b = c
    count+=1
    fibo.append(b)

len = 0
for i in array:
    if i in fibo:
        # print(i)
        len+=1
if len <= 2:
    print(-1)
else:
    print(len)
    