"""
Your task here is to take input a string and reverse it. However, you should reverse only the normal alphabets. The special characters should be in their original positions.

Example Input
sd&hg#j
 
Output
jg&hd#s
"""

# brute force-----------
n = list(input())
i = 0
j = len(n)-1
while i<j:
    if n[i].isalpha() and n[j].isalpha():
        n[i],n[j] = n[j],n[i]
        i+=1
        j-=1
    elif n[i].isalpha() and n[j].isalpha() == False:
        j-=1
    elif n[i].isalpha() == False and n[j].isalpha():
        i+=1
print("".join(n))

#optimised approach
n = input()
string = ""
for i in range(len(n)-1,-1,-1):
    if n[i].isalpha():
        string+=n[i]
string = list(string)
for i in range(len(n)):
    if n[i].isalpha() ==  False:
        string.insert(i,n[i])
print("".join(string))
