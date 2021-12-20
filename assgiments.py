# s = {2,3}
# print(s*3)-----------eror

# c= 4//5*5
# for i in range(3):
#     for j in range(i):
#         if i == j:
#             c = c+1
        
# print(c)---------------------0

# l = [1,2,3,4]
# l.remove(1)
# print(l) ----------------[2,3,4]

# fruits = ['a','b','c']
# fruits.clear(1)
# print(fruits) --------------eror

# aList = [5,10,15,25]
# print(aList[::-2]) ---------------[25, 10]

# L = [2,3,4,5]
# L = list(filter(lambda x:x%2, L))
# print(L)----------[3, 5]

n1, n2 =15, 20
if (n1> n2):
    max = n1
else:
    max = n2
while(True):
    if(max % n1 == 0 and max % n2 ==  0):
        break;
    max = max + 1
print(max)