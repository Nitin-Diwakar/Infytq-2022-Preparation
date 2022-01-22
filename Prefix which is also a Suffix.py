"""
Given a string, find the longest length of a prefix which is also a suffix.

Example Input

aaa

Output

1

Example Input

abcdab

Output

2
"""
string = input()
n = len(string)
flag = 0
for index in range(n//2,0,-1):
    prefix = string[:index]
    suffix = string[n-index:]
    if prefix == suffix:
        flag = 1
        break
if flag:
    print(len(prefix))
else:
    print(-1)




