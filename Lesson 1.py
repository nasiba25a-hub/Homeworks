"""
Lesson 1 Homeworks
"""

#Variables

name = "Nasiba "
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

months = ('yanvar', 'mart', 'oktyabr', 'noyabr', 'dekabr', 'iyul')
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
    'name': 'Nasiba',
    'age': 15,
    'city': 'Tashkent'
}
print(dictionary['age'])
dictionary['faoliyati'] = 'talaba'
dictionary.pop('city')
print(dictionary)
