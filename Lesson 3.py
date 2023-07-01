# Lesson 3 Homeworks

#Task 1

import math
from datetime import date

r = int(input("Aylana Radiusini kiriting \n>>> "))
area=math.pi*r**2

print(area)

#Task 2

son = int(input("Son kiriting \n>>>"))
sqrt = math.sqrt(son)

print(sqrt)

#Task 3

yosh = int(input("Yoshingizni kiritin \n>>>"))
year = date.today().year
byear = year-yosh
print(byear)

#Task 4

gap = input("Write short sentence here \n>>>")
print(gap[::-1])