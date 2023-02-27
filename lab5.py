import re

#1Write a Python program that matches a string that has an 'a' followed by zero or more 'b''s.
s1 = str(input())
result1 = re.match(r'a[b]*',s1)
print(result1.group(0))

#2Write a Python program that matches a string that has an 'a' followed by two to three 'b'
s2 = str(input())
result2 = re.match(r'a[b]{2,3}',s2)
print(result2.group(0))

#3Write a Python program to find sequences of lowercase letters joined with a underscore.
s3 = str(input())
result3 = re.split('_',s3).findall(r'[a-z]\w+',s3)
print(result3)

#4Write a Python program to find the sequences of one upper case letter followed by lower case letters
s4 = str(input())
results4 = re.findall(r'[A-Z]{1}[a-z]\w*',s4)
print(results4)

#5
s5 = str(input())
result5 = re.match(r'a\w*b',s5)
print(result5.group(0))

#6Write a Python program to replace all occurrences of space, comma, or dot with a colon.
s6 = str(input())
results6 = re.sub(r'[\s,.]',':',s6)
print(results6)

#7Write a python program to convert snake case string to camel case string.
snake7 = str(input())
temp1 = snake7.split('_')
camel7 = temp1[0] + ''.join(i.title() for i in temp1[1:])
print(camel7) 
#8Write a Python program to split a string at uppercase letters.
s8 = str(input())
results8 = re.split(r'[A-Z]',s8)

print(results8)

#9Write a Python program to insert spaces between words starting with capital letters.
s9 = str(input())
results9 = re.findall(r'[A-Z]{1}[a-z]\w*',s4)
for i in results9:
    print(i, '')

#10Write a python program to convert given camel case string to snake case string.
snake7 = str(input())
temp1 = snake7.split(' ')
camel7 ='_'.join(i.title() for i in temp1)
print(camel7) 
