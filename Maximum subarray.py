"""
An array is given suppose a =[3,5,8,2,19,12,7,11] One have to find the largest subarray that the element satisfy the following condition
x[i]=x[i-1]+x[i-2] If more than one substring if found then largets one has to print the array which starts with the minimum elements and if they are also same then the array with minimum second element and so on.
Here the subarrays |2,3,5,8],[3,8,11],[5,7,12,19] Expected is [2,3,5,8]
"""
# [0,1,2,3,4,5,6,7,8 ]
# [2,3,5,7,8,11,12,19]
array = list(map(int,input().split(",")))
array = sorted(array)
j = []

j.append(array[0])
j.append(array[1])

for i in range(2,len(array)):
    if j[i-1]+j[i-2] in array:
        j.append(j[i-1]+j[i-2])
    else:
        break
 
print(j)