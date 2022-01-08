"""
A non empty string instr containing only parenthesis (,),{.},[,] it return outstr based on following,
– instr is properly nested and return 0
– instr not properly nested, return position of element in instr
– position start from 1
Input: {([])} Output: 0
Input: (])()] Output: 3
Input: [[()]  Output: n+1 for last element i.e 5+1=6
"""
st = []
ope = ['[', '{', '(']
close = [']', "}", ")"]
# define function


def check(s):
    for i in range(len(s)):
        if s[i] in ope:
            st.append(s[i])
        elif s[i] in close:
            last = close.index(s[i])

            if (len(st) > 0) and (ope[last] == st[len(st) - 1]):
                st.pop()
            else:
                return i+1
    if len(st) == 0:
        return 0
    else:
        return len(s)+1
# give the input


s = input()
print(check(s))
