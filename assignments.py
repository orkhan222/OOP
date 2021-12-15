a, b, c = 2,5,10

# 1-ci Kullanicidan aldiginiz 2 sayinin carpimi ile a,b,c toplaminin farki nedir?
x= int(input('x: '))
y= int(input('y: '))
sonuc = (x*y) - (a+b+c)

# 2-ci c-nin b-ye kalansiz bolumunu hesaplayiniz
sonuc = c // b 

# 3-cu (a,b,c) toplaminin mod 3-u nedir?
sonuc = (a+b+c) % 3

# 4-cu b-nin a kuvventini hesaplayiniz.
sonuc = b **a

# 5-ci a,*b,c = sayilar islemine gore c-nin kupu kactir?
sayilar = 1,5,7,10,3
a,*b,c = sayilar
print(c ** 3)

# 6-ci a, *b,c = sayilar islemine gore b-nin degerleri toplami kactir?
a,*b,c = sayilar
print(b[0]+b[1]+b[2])


print(sonuc)