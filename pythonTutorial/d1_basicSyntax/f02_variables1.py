"""
table
object reference count
"""

a="nyc"
b="nyc"
print("nyc")
print("a is: " + a)

print(a==b)
print(a is b)

a="sfo"
print(a is b)

c=a
print("c is: " + c)

a="sjc"
print("a is: " + a)

print("c is still: " + c)

d=a+c
print("d is: " + d)

d="a" + "c"
print("d is: " + d)

e=" "
d = a + e + c
print("d is: " + d)