"""
Number of odd sub arrays. Find the number of distinct subarrays in an array of position integers such that the sum of the subarray is an odd integer, two subarrays are considered different if they either start or end at different index.

Input:
1
3
1 2 3
Output:4

Explanation: subarrays [[1], [1, 2], [1, 2, 3], [2], [2, 3], [3]]
"""

n1 = int(input())
n2 = int(input())

#generate array from n1 to n2 using list comprehension(it is handy to use)
array = [i for i in range(n1,n2+1)]
print(array)
#generating a subarray with first or last digit different
subArray = [array[i:j+1] for i in range(len(array)) for j in range(i,len(array))]

print(subArray)

#counter loop
count = 0
for i in subArray:
    if sum(i)%2 != 0:
        count+=1
print(count)


