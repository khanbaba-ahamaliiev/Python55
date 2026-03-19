round(12.2, 3)#- округливает

#условия

# if elif else

# match

# and or not

# 1 not
# 2 and
# 3 or



# if <condition>:
#     <code...>
# elif <condition>:
#       <code...>
# else :
#   <code...>

age=15

if age >= 18:
    print("You are old enough.")
    # pass # - пропустить
elif 12 < age < 18:
    print("You are teenager.")
else:
    print("You are not old enough.")

print("the end")

n = 2
if n % 5 == 0:
    if n == 25:
        print("25")
    else:
        print("not 25")
else:
    print("n % 5 !=0")