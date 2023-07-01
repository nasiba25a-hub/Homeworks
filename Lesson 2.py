"""
Lesson 2 Homeworks

None{null}
Numeric - { Int, Float, Complex, Bool -> {True(1)/False(0)} }
List
Tuple
Set
String
Range
Dictionary

"""
"""
a = 10
print(id(a))
print(type(a))

b = 10.2
print(id(b))
print(type(b))

c = 10.0
print(id(c))
print(type(c))

comp = 5+6j
print(type(comp))


a=range(100, 9, -10)
new= list(a)
print(new)


Operators in Python

1
Arithmetic
operators

+, -, *, /, **

2
Assignment
operators

x = 5
y = 8
x < x + 3
x = y - 3

x = x + 5 <= > x += 5

3
Realational
operators

a > b, a < b, a <= b, a >= b, a != b, a == b

4
Logical
operators

and (*), or (+), not ((-1) *)

5
Unary
operators

"""


# 1-task

Hafta_kuni = "Juma"
Son = 3
print(f"Salom. {Hafta_kuni} dagi {Son}-darsning vazifalarini bajarmoqdasiz")

# 2-task

h = 3
w = 6
P = 2 * (h + w)
print(P)

# 3-task

Sel = 46
Fah = Sel * (9 / 5) + 32
print(Fah)

# 4-task

a = 10
b = 7
print(f"{a + b}, {a - b}, {a * b}, {a / b}, {a ** b}")

# 5-task

X = 7
print(X + 5)
print(X - 2)
print(X * 3)
print(X / 2)
print(X % 4)

# 6-task

son1 = input("a sonni kiriting \n >>> ")
son2 = input("b sonni kiriting \n >>> ")

if son1 > son2:
    print(f"{son1} {son2} dan katta")
elif son1 < son2:
    print(f"{son1} {son2} dan kichik")
else:
    print(f"{son1} bilan {son2} teng")

# 7-task

yosh = int(input("Yoshingizni kiriting \n >>> "))

if yosh >= 16:
    print("Dastur foydalanuvchisi haydash huquqiga ega")
else:
    print("ALERT! \nDastur foydalanuvchisi haydash huquqiga ega emas!")