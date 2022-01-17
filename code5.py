"""
Take input from the user in the given format
consist of name and code.
find the sum of square of digits from code. if the sum of squares of digit of the code are:
	Even: then add the last 2 char in the beg
	Odd: the add first character at the end

input:- abcde:1234, rewqt:2131

eg: abcde = deabc
	1^2 + 2^2 + 3^2 + 4^2 = 30(even)
	so-> deabc


"""

item = input().split(",")
for i in item:
    word,num = i.split(":")
    Sum = 0
    for j in num:
        Sum+=int(j)**2
    if Sum%2 == 0:
        word = word[-2:] + word[:-2]
    else:
        word = word[1:]+ word[0]
    print(word)