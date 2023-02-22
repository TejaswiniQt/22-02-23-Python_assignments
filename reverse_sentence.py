'''
write a python program to reverse a sentence
Input : "sky is blue"
output : "blue is sky"
'''



str1 = input("Enter the senteance: ")
str2 = str1.split()
str2 = str2[-1::-1]
str2 = " ".join(str2)
print(str2)
