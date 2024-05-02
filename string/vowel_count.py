# Write a Python Program to Find Vowels From a String.

str="jwebvbch ksbdkcjbkjkbcasiuocdsbkj kjs"
count =0
for each in str:
    if each.lower() in ['a','e','i','o','u']:
        count = count+1
print(count)