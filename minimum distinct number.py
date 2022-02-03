"""
Given a list(combination of repeated and distinct elements whihc are space seperated) and number of elements deletion X. You have to delete any X element from the list so that list will have minimum distinct number

Input: 4
	1 1 1 2 2 3 3 4 5 6
Output: 3

Input: 3
	1 1 1 2 2 2 4 5 6
Output: 2
"""

x = int(input())
array = list(map(int,input().split(" ")))

unique = set(array) # for unique element  to count all occurence of each element

counter = [] # to store all occurence of each element
for i in unique:
    counter.append(array.count(i))
# print(counter)
counter.sort() #sort the counter, by this we can delete more distinct element to minimize it

length = len(counter) # to count distinct element left

for i in counter:
    if i <= x:
        x-=i
        length-=1
    else:
        break
print(length)