"""
You are given an integer K. Find the smallest number N such that N has exactly K digits and none of the digits in N is 0. Also, the product of digits in number N is greater than or equal to the sum of digits in number N.

Input Format

The first line contains an integer T denoting the number of test cases.
For each test case, the first line contains an integer K.
For Example:
Input
2
1
3
Output
1
123

Explaination For the first test case, N = 1 is the smallest number that has a product of digits i.e., 1 greater than or equal to the sum of digits i.e., 1.

For the second test case, N = 123 is the smallest number that has a product of digits i.e., 6 greater than or equal to the sum of digits i.e., 6.

Constraints

1 ≤ T ≤ 1 ⋅ 10
1 ≤ K ≤ 5 ⋅ 10 ^ 4

Output Format

For each test case in a new line, print the smallest number N that satisfies the given condition.

Sample Input 0

1
Sample Output 0

1
"""

k=int(input())
sum=0
pro=1
s=int("1"*k)
for i in range(s,(10**k)-1):
    if("0" in str(i)):
        pass
    else:
        for j in str(i):
            sum=sum+int(j)
            pro=pro*int(j)
        if(sum==pro):
            print(i)
            break
        else:
            sum=0
            pro=1