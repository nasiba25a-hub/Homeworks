"""
Lesson 1 Homeworks
"""

#Variables

name = "Jahongir "
age = str(16)
total = name + age
print(total)

#Lists

fruits = ['apple', 'grape', 'banana']
print(fruits)
fruits.append("apricot")
fruits.remove('apple')
print(fruits)

#Tuples

months = ('yanvar', 'mart', 'oktyabr', 'noyabr', 'dekabr', 'iyun')
print(months [3])
#months[5] = 'iyul' { Tuple is unchangeablemethod type :) }

#Sets

color = {'blue', 'green', 'white', 'black', 'green'}
print(len(color))
#color.update('yellow') { Unchangeable method type }
#color.remove('green') { It removes 2nd item automatically }
print(color)

#Dictionary

dictionary = {
    'name': 'Jahongir',
    'age': 16,
    'city': 'Karshi'
}
print(dictionary['age'])
dictionary['faoliyati'] = 'talaba'
dictionary.pop('city')
print(dictionary)