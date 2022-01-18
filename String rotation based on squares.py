"""
You are given a list of strings each having 2 components to it - word and integer. These 2 components are separated by :.

If the square of digits in the number component is even, then you must rotate the word to the right by 1
If the square of digits in the number component is odd, then you must rotate the word to the left by 2
Finally, print the rotated word.

Example Input

rhdt:246,ghftd:1246
Output

trhd
ftdgh

"""

string = input().split(",")
for i in string:
    word,num = i.split(":")
    Sum = 0
    for j in num:
        Sum+=int(j)**2
    if Sum%2 == 0:
        print(word[-1]+word[:-1])
    else:
        print(word[2:]+word[:2])