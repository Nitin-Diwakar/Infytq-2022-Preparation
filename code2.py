"""
input is 5624381275 seperate odd place integer = 6,4,8,2,5
return 4 digit otp by square the digit.

square is 6,4,8,2,5 = 36,16,64,4,25.
so the otp is 3616.
"""


interger = list(input())
string = ""
i=1
while i<len(interger):
    string+=str(int(interger[i])**2)
    i+=2
print(string[:4])