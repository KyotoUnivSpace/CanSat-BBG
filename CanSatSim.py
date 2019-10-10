import numpy as np
import matplotlib.pyplot as plt
from math import *
%matplotlib inline


servo_distance = 40e-3

minLength = 74e-3
length = []
vLength = []
servo_angles = []
angles = []
theta = 0 # rad
time = []

vCansat = 20.0e-3 # m/s

length.append(minLength)

index = 0

while True:
    time.append(index / 100)
    vLength.append(100.0*(sqrt((minLength * tan(theta) + vCansat/100)**2 + minLength**2) - minLength / cos(theta)))
    if index > 0: length.append(length[index - 1] + vLength[index - 1] / 100.0)
    servo_angle = atan((length[index] - 70e-3) / servo_distance)
    servo_angles.append(degrees(servo_angle))
    angles.append(degrees(theta))
    if length[index] * sin(theta) > minLength: break
    theta = acos(minLength / length[index]) if vLength[index] > 0 else -acos(minLength / length[index])
    index += 1

# plt.plot(time, length)
# plt.show()
# plt.plot(time, vLength)
# plt.show()
# plt.plot(angles, length)
# plt.show()
plt.plot(angles, vLength)
plt.show()
plt.plot(angles, servo_angles)
plt.show()

print((servo_angles[-1] - servo_angles[-2]) *100)
