
a = input("Введите предложение:")
b = a.count(" ")

while b >= 5:
    print(a[(len(a)//2+1):],a[0:(len(a)//2+1)])
    break
else:
   print(a)


