"""QUESTION 1"""

lis = []
for i in range(2000, 3200+1):
    if i % 7 == 0 and i % 5 != 0:
        lis.append(i)
print(lis)