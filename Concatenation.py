"""
Input: a string of comma separated numbers. The numbers 5 and 8 are present in the list. Assume that 8 always comes after 5.

Case 1: num1 = add all numbers which do not lie between 5 and 8 in the input.
Case 2: num2= numbers formed by concatenating all numbers from 5 to 8.
Output: sum of num1 and num2

Example: 1) 3,2,6,5,1,4,8,9
Num1 : 3+2+6+9 =20
Num2: 5148
output: 5248+20 = 5168
"""

lst = list(map(int, input().split(",")))
num1 = sum(lst[:lst.index(5)]) + sum(lst[lst.index(8)+1:])
num2 = lst[lst.index(5):lst.index(8)+1]
num2 = [str(int) for int in num2]
num2 = ''.join(num2)
print(num1+int(num2))
