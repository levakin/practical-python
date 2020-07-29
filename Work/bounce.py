# bounce.py
#
# Exercise 1.5
height = 100
jump_num = 1
for i in range(10):
    height = height * 0.6
    print(jump_num, round(height, 4))
    jump_num += 1
