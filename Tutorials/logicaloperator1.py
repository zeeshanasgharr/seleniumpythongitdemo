a = True
b = False
c = 5
d = 10


result = (a or b) and not (c > d) #   a or b = True  AND not( 5 > 10)

print(result)

result1 = (c < d) or (not a and b)
print(result1)