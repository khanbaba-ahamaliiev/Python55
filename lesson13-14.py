
# while

# while <cond>:
# .... code....
# .... code....

i = 1
while i <= 5:
    print(f"iter #{i}")
    i += 1


# break, continue, else


# data = ""
# while True:
#     x = input("enter data")
#     if x == "exit":
#         break
#     data += x
#     data += "\n"
# print(data)
# print("the end")

# data = ""
# x = None
# while x != "exit":
#     x = input("enter data")
#     data += x
#     data += "\n"
# print(data)
# print("the end")



# i = 1
# while i <= 5:
#     if i == 2 or i == 3:
#         i += 1
#         continue
#     print(f"iter #{i}")
#     i += 1
# print("the end")

# i = 1
# while i <= 5:
#     if i not in (2, 3):
#         print(f"iter #{i}")
#     i += 1
# print("the end")


# i = 1
# while i <= 3:
#     print(f"iter #{i}")
#     i += 1
# else: #исполняется при нормальный условиях (без break)
#     print("the end without break\n")

#
# i = 1 # - делает табличку умножения
# while i <= 10:
#     j = 1
#     while j <= 10:
#         print(i*j, end="\t")
#         j += 1
#     print()
#     i += 1


# h = 10
# w = 10
# i = 1 # - делает куб
# while i <= h:
#     j = 1
#     while j <= w:
#         if j == 1 or i == 1 or j == w or i == h:
#             print('*', end="\t")
#         else:
#             print(' ', end="\t")
#         j += 1
#     print()
#     i += 1



# h = 10
# w = 10
# i = 1 # - делает треугольник
# while i <= h:
#     j = 1
#     while j <= w:
#         if i >= j:
#             print('*', end="\t")
#         else:
#             print(' ', end="\t")
#         j += 1
#     print()
#     i += 1



