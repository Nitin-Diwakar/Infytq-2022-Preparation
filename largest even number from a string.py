"""
Take as input a string. This string is a mixture of letters, integers and special char. From this string, find the largest even number that can pe possibly formed after removing the duplicates.

If an even is not formed then return -1.

Example Input

infosys@337

Output

-1
"""



s = input()
n = sorted(list(set(filter(lambda x:x.isdigit(),s))),reverse=True)
# print(n)
even =list(filter(lambda x: int(x)%2 == 0,n))
# print(even)
if len(even) == 0:
    print(-1)
else:
    if int(n[-1])%2 == 0:
        print("".join(n))
    else:
        n.remove(even[-1])
        n.append(even[-1])
        print("".join(n))