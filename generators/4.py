#squares to yield the square of all numbers from (a) to (b). Test it with a "for" loop and print each of the yielded values.
def squares(a, b):
    while a<=b:
        yield a*a
        a += 1
a = int(input())
b = int(input())
n = []
for i in squares(a, b):
    n.append(i)
print(n)