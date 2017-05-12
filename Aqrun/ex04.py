# -- coding: utf-8 --
"""
习题4：变量和命名
"""

cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven

print("There are %d cars available" % cars)
print("There are only %s drivers available" % drivers)
