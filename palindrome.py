"""
Write a python function nearest_palindrome ()
Which can accepts a number and return the nearest greater palindrome number.
Input: 12300 -> output: 12321
Input: 12331 -> output: 12421
"""

def nearest_palindrome(n):
    while True:
        rev = int(str(n)[::-1])
        if rev == n:
            return int(n)
        n+=1

n = int(input())
print(nearest_palindrome(n))