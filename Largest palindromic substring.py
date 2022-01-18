"""
Take as input a string. Find the longest possible substring from this string which is also a palindrome.

Example
Input: dcodocir

Output" codoc
"""
n = input()
sub = [n[i:j+1] for i in range(len(n)) for j in range(i,len(n))]
print(sub)
mx = 0
for i in sub:
    if i == i[::-1] and len(i) > mx:
        result = i
        mx = len(i)
print(result)
        
        
