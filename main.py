import sys
sys.path.append("./needle")
sys.path.append("./imu")
from needle_controller import NeedleController
from imu_sensor import IMUWrapper
from math import *
import time

needle = NeedleController(servo_distance = 40e-3)
imuWrapper = IMUWrapper()



minLength = 74e-3 #
vCansat = 20.0e-3 # m/s

poll_interval = imuWrapper.getPollInterval()

while(True):
    if imuWrapper.read():
        (r, p, y) = imuWrapper.getFusionPose();
        (_r, _p, _y) = imuWrapper.getGyro();
        p = degrees(p) + 180
        back = int(p/45) + 1
        front = 0 if back == 7  else back + 1
        front_length = minLength / cos(radians(front*45 - p))
        needle.set_length(front , front_length)
        back_length = minLength / cos(radians(p - back*45))
        # print("back : back_length = " + str(back) + " : " + str(back_length))
        # print(-p + front*45)
        # print("p : front : back = " + str(int(p)) + " : " + str(front) + " : " + str(back))
        needle.set_length(back, back_length)
        time.sleep(poll_interval*1.0/1000.0)
