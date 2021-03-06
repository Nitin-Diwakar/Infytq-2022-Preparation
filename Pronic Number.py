"""
Pronic number is a number which is the product of two consecutive integers, that is, a number n is a product of x and (x+1).

Take a string in which random numbers are present and we have to find the product and the numbers(one is lesser and one is greater) which are already present in the string.also the numbers x and x+1 are single digit numbers. Let’s see the example:

E.g. Given a string contains 1203456. The multiplication of 3 and 4(one is lesser and one is greater) product become 12 and it’s present in the string. Like 4 and 5 (one is lesser and one is greater) the product is 20 and it’s present in the string and so on.

In such a way, We have to find all the numbers and in the output, we have to display the pronic numbers on a single line. Display only distinct numbers and make sure they are in sorted order.

If we haven’t found any product then print -1.

Example Input
1203456789
 
Output
0 2 6 12 20 56
"""

string =input()
s = sorted(list(string))
result = []
# print(s)
for i in range(len(string)-1): # 1 5 7
    if int(s[i]) - int(s[i+1]) == -1:
        product = str(int(s[i])* int(s[i+1]))
    else:
        continue
    if product in string:
        result.append(product)
if len(result) != 0:
     print(" ".join(result))
else:
    print(-1)
    



