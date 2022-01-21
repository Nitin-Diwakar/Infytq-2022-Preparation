# Given an array, find the number of sub-arrays whose sum is odd.

# Input Format

# First line contains the size of the array.
# second line the list of elements, separated by space
# Output Format:

# print the number of sub arrays who sum is odd
# Example Input

# 5 4 4 5 1 3

# Output

# 12

n,array = int(input()),list(map(int,input().split()))
subArray = [array[i:j] for i in range(n) for j in range(i+1,n+1)]
print(subArray)
# print('Len:',len(subArray))

result = list(filter(lambda x:sum(x)%2 !=0,subArray))
print(len(result))
