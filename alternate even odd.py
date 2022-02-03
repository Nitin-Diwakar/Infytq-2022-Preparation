"""
Given a string containing at least one special character, one even-digit and one-odd-digit, return an output string outstr based on the number of special characters as below:

- If the number of special characters is odd,append all the odd digits and even digits alternatively to the outstr, starting with the first odd digit.

- If the number of special character is even, append all the even digits and odd digits alternatively the outstr,starting wiht the first even digit.

- After arranging the digits based on the above two points,if there are any additional digits remaining, append them at the end of outstr.

Input: A5c67r21i@p#8t
Output: 652781

Input: h93@5213#w4rld&
Output: 9234513
"""

string = input()

num = []
count = 0
for i in string:
    if i.isalpha():
        continue
    elif i.isdigit():
        num.append(int(i))
    else:
        count+=1
# print(num)   
even = list(filter(lambda x:x%2 == 0,num))
odd = list(filter(lambda x:x%2 != 0,num))
# print(even)
# print(odd)

# approach1 for printing even odd
if count&1 == 1: # for odd
    for i in range(max(len(even),len(odd))):
        if i < len(odd):
            print(odd[i],end="")
        if i < len(even):
            print(even[i],end="")
            
else: #for even
    for i in range(max(len(even),len(odd))):
        if i < len(even):
            print(even[i],end="")
        if i < len(odd):
            print(odd[i],end="")
            

"""
approach 2 for printing even odd

if count&1 == 1:
    odd,even = even,odd
   
for i in range(max(len(even),len(odd))):
    if i < len(even):
        print(even[i],end="")
    if i < len(odd):
        print(odd[i],end="") 
"""
