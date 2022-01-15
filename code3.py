"""
Reverse the string after removing duplicates?

Ex= programming

p/o= nimagorp

infosys = ysofni
"""
string = input()
unique = list(dict.fromkeys(string))
unique.reverse()
print("".join(unique))