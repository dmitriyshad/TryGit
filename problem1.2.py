import math

def read_power():
    power = raw_input()
    power = float(power)
    return power

def read_coordinates():
    coordinatesStr = raw_input()
    coordinatesStr = coordinatesStr.strip(' ')
    coordinatesStr = coordinatesStr + ' 0'
    return coordinatesStr.split(' ')

def calculate_norm(coordinates, power):
    sum = 0
    for coord in coordinates:
        sum += math.fabs(float(coord)) ** power
    return sum ** (1.0/power)

power = read_power()
coordinates = read_coordinates()
print calculate_norm(coordinates, power)
