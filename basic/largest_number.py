list1 =[3,6,1,6,8,3,0,9,7]
largest = 0
for i in list1:
    if i>largest:
        largest =i
    
print(largest)

l=sorted(list1)
print(l[-1])

list1.sort()
print(list1[-1])