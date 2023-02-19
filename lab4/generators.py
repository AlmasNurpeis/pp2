import generators
# 1 Create a generator that generates the squares of numbers up to some number N.
n1 = int(input())
a = [i**2 for i in range(n1)]
#2 Write a program using generator to print the even numbers between 0 and n in comma separated form where n is input from console.
n2 = int(input())
b = [i for i in range(n2) if i % 2 == 0]
#3 Define a function with a generator which can iterate the numbers, which are divisible by 3 and 4, between a given range 0 and n
n3 = int(input())
c = [i for i in range(n3) if i % 3 == 0 or i % 4 == 0]
# 4 Implement a generator called squares to yield the square of all numbers from (a) to (b). Test it with a "for" loop and print each of the yielded values.
r1 = int(input())
r2 = int(input())
def squares(r1, r2):
    for i in range(r1, r2):
        print(i**2)
squares(r1, r2)
#5 Implement a generator that returns all numbers from (n) down to 0.
n4 = int(input())
def rev(n):
    while(n>=0):
        print(n)
        n-=1
rev(n4)