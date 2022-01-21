""" 
Given a string, we have to find the longest substring which is unique (that has no repetition) and whose size is at least 3.

If more than one substring is found with max length then we have to print the one which appeared first in the string

If no substring is present that matches the condition then we have to print -1

Example input: A@bcd1abx

Output: A@bcd1a
"""



string = input()
unqiue = ""
for i in range(len(string)):
    subString = string[i]
    for j in range(i+1,len(string)):
        subString+=string[j]
        sublen = len(subString)
        if sublen >=3 and len(set(subString)) == sublen:
            if len(unqiue) < sublen:
                unqiue = subString
            
if len(unqiue) == 0:
    print(-1)
else:
    print(unqiue)