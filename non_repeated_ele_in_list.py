'''
write a program to print non-repeated elements in a python
'''

mylist = [1,2,2,3,3,3,3,4,4,5,6,6,6,6,8,8]
new_list = []
for num in mylist:
    if mylist.count(num) == 1:
        new_list.append(num)
print("Expected output: ",new_list)
