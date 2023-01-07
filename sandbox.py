import random

import sympy as sy
lower_bound = 0.05
upper_bound = 0.1
interval_increase = 0.1
exponent = -3/2
integral_array = []

discard_rate = 0.65  # 0.5 -0.75
back_rate = 0.95
post_rate = 0.22


def f(x):
    return x**exponent


x = sy.Symbol("x")
print(sy.integrate(f(x), (x, 0.05, 0.1)))


while upper_bound <= 20:  #20

    interval_integral = sy.integrate(f(x), (x, lower_bound, upper_bound))

    integral_array.append([lower_bound, upper_bound, interval_integral])

    lower_bound = upper_bound
    upper_bound += interval_increase


print(integral_array)

values = []
probabilities = []
for i in range(len(integral_array)):
    values.append(integral_array[i][1])
    probabilities.append(integral_array[i][2])


print(random.choices(values, weights=probabilities))




