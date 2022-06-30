#1 задание

a=[x for x in range(1000) if x%3==0 or x%5==0]
print(sum(a))

#2 задание
a = 333
b = 555
a, b = b, a
print("в переменной а:", a)
print("в переменной b:", b)

#3 задание

a="4729461084"

b=0
for i in a:
    b+=int(i)
print(b)
