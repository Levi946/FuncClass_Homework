def is_polindrom(number):
    a=str(number)
    b=int(a[::-1])
    if number==b:
        return True
    else:
        return False
max_polindron=[]
for i in range(100,1000):
    for j in range(100,1000):
        if is_polindrom(i*j)==True:
            max_polindron.append(i * j)
print(max(max_polindron))
