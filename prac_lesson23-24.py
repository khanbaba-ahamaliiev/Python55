import random


ls = [2, 9, 4, -4, 8, 5, -3, 7, 5, 5] # [random.randint(-10,10) for i in range(10)]
print(ls)

sum_neg = 0
for x in ls:
    if x < 0:
        sum_neg += x
print(sum_neg)

sum_even = 0
for x in ls:
    if x % 2 == 0:
        sum_even += x
print(sum_even)

sum_odd = 0
for x in ls:
    if x % 2 != 0:
        sum_odd += x
print(sum_odd)

prod_idx3 = 1
for i, x in enumerate(ls):
    if x % 3 == 0:
        prod_idx3 *= x
print(prod_idx3)

max_val = ls[0]
min_val = ls[0]
min_i = 0
max_i = 0
for i in range(1, len(ls)):
    if ls[i] > max_val:
        max_val = ls[i]
        max_i = i
    if ls[i] < min_val:
        min_val = ls[i]
        min_i = i
print(max_val, min_val)

prod_between = 1
for i in range(min_i+1, max_i):
    prod_between *= ls[i]

print(prod_between)
