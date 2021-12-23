num1 = int(input('Num1: '))
# new = []
num2 = 0

# while num1> 0:
#     num2 = num1%10
#     new.append(num2)
#     num1//=10
# print(max(new))

# while num1> 0:
#     num2 = num1%10
#     new.append(num2)
#     num1//=10
# print(new)


while num1>0:
    num2 = (num2*10) + (num1%10)
    num1//=10
print(num2)