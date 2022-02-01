"""
In an airport, the Airport authority decides to charge some minimum amount to the passengers who are carrying luggage with them. They set a threshold weight value, say T, if the luggage exceeds the weight threshold you should pay double the base amount. If it is less than or equal to threshold then you have to pay $1.  

Input Format for Custom Testing:
•	The first line contains an integer, N, denoting the number of luggage. 
•	Each line i of the N subsequent lines (where 0 <= i <n) contains an integer describing weight of ith luggage. 
•	The next line contains an integer, T, denoting the threshold weight of the boundary wall

Sample Input 1
4
1
2
3
4
3

Sample Output 1
5

"""
lugguage = []
for _ in range(int(input())):
    lugguage.append(int(input()))
threshold = int(input())

amount = 0
for i in lugguage:
    if i <= threshold:
        amount+=1
    else:
        amount+=2
print(amount)