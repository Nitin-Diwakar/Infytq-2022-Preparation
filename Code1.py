# set of number and sum is given
# -1,1,0,0,-2,2

# sum = 0
# print no. of combination possible of lenght 4
# which sum = 0

from itertools import combinations
num = list(map(int,input().split(',')))
s = int(input())
com = list(combinations(num,4))

count = 0
for i in com:
    i = sum(i)
    if(i == s):
        count+=1
print(count)
