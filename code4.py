"""
take input consist of name and code.

find the max digit from code which is less than or equal to the length of name
and put the place char in the final string if there is no any digit found which
satisfies the given condition then simply put 'X'.

input = coder:2431, ram:124,aman:4239
o/p = ean
"""
word_num = list(map(str,input().split(",")))
result = ""
for i in word_num:
    word,num = i.split(":")
    # print(word,'\t',num)
    size = len(word)
    
    maxx = 0
    # print(word,':',size)
    for j in num:
        # print(j)
        if int(j) <= size and int(j)>=int(maxx):
            maxx = j
            # print('Max',maxx)
    if maxx == 0:
        result+="X"
    else:
        result+=word[int(maxx)-1]
print(result)