str1 = "adaslkndlnl"

print(str1[::-1])

str1 = "my name is adarsh"

print(str1[::-1])
new_str=str1.split(" ")

str2 =" ".join(new_str[::-1])
print(str2)

l=[]
for i in new_str:
    l.append(i[::-1])

str3 = " ".join(l)
print(str3)
