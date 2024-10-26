student_info = {

    'name':'Testing Funda',
    'age': 21,
    'grade': 'A',
    'subjects':['Python','Automation testing', 'Selenium']

}

print(type(student_info))

print(student_info['name'])

print(student_info.get('age'))

student_info['age'] = 25

print(student_info)

age = student_info.pop('age')
print(age)
print(student_info)

del student_info['grade']
print(student_info)

student_info.clear()
print(student_info)
