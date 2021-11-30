# num1 = int(input('reqem: '))
# new = []
# num2 = 0

# while num1>0:
#     num2=num1%10
#     new.append(num2)
#     num1//=10
    
# print(max(new))

# num1 = int(input('reqem: '))
# num2 = int(input('reqem: '))
# count = 0
# while num1 >= num2:
#     if num1%num2 == 0:
#         count+=1
#     num2+=1 
# print(count)

# a = int(input('reqem: '))
# b= []
# c = 0
# while a>0:
    
#     b.append(c)
    
# print(max(b))


# print(dir(float))

# urunA=5000
# urunB=6000
# kdv=0.18

# print(urunA + (urunA*kdv))
# print(urunB + (urunB*kdv))


# pi =3.14
# r = float(input('yari capi: '))

# alan = pi *(r**2)
# cevre = 2 * pi * r

# print(alan, cevre)

# ad = input('adiniz: ')
# soyad = input('soyadiniz: ')
# yas = str(input('yasiniz: '))

# msj= 'Menim adim ' + ad + ' ve soyadim ' + soyad + '.Yasim ise o' + yas + '.'

# print(msj)

# print(msj[0])
# print(msj[1])
# print(msj[-1])
# print(msj[15])


name = ['anar','aydan','aybeniz','aynur','oraxn','ozal']
index = 0
count= 0
while len(name) > index:
    if name[index][0] == 'a':
        count+=1
    index+=1
print(count)
    