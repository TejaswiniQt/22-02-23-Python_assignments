'''
write a program to count the number of character count in s string
'''

mystr = "a,a,a,b,b,c,c,c,c"
str1 = mystr.split(',')
visited = []
final_list = []
for ch in str1:
    if ch not in visited:
        final_list.append(f"{ch}:{str1.count(ch)}")
        visited.append(ch)
print(",".join(final_list))
