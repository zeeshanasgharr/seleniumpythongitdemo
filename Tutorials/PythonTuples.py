tuple = (1,2,3)
tuple1 = ('ac','bd','tr')
tuple2 = ('ac',1,True)

tuple4 = (5,)
print(type(tuple4))

tuple5 = ()

print(tuple5)

tuple6 = (1,2,3,4,5,6,7)
print(tuple6[-1])
print(tuple6[1:3])

tuple7 = (1,2,3)
tuple8 = (4,5,6)

combine = tuple7 + tuple8
print(combine)
rep = tuple7 * 3
print(rep)

tuple9 = ('a','b','c')
print('a' in tuple9)
print('d' in tuple9)

print(len(tuple9))

list = list(tuple9)
print(list)