
abc = ['abc','def','xyz']
print(abc)

mix_list = [1,'Testing Funda', 3.67, 'Python']

print(mix_list[-1])

num = [1,2,3,4,5]

print(num)

num.append(6)
print(num)

num.insert(1,25)
print(num)

num.extend([7,8,9])
print(num)

num.remove(25)
print(num)

pop_item = num.pop(3)
print(pop_item)
print(num)

num.clear()
print(num)

num1 = [1,2,3,4,5,6,7,8,9]

print(len(num1))
num1.reverse()
print(num1)

subset = num1[2:5]
print(subset)

step_slice = num1[::2]
print(step_slice)

nested_list = [
[1,2,3,4,5,6,7,8,9],
[1,2,3,4,5],
[1,2,3]
]

