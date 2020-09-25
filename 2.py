from math import sqrt

print('please, enter two numbers')
first_leg, second_leg = input(), input()
if first_leg.isdigit() and second_leg.isdigit():
    result = sqrt(int(first_leg) ** 2 + int(second_leg) ** 2)
else:
    print('please, try again, legs must be numbers!')
