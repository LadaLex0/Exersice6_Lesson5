import random
list1 = []

for i in range(4):
    list1.append(random.randint(1, 100))
print("1st list:", list1)

list2 = list1[:]
for i in list1:
    list2.append(i ** 2)
print("2nd:", list2)

