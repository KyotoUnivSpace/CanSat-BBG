import sys
import RTIMU
import os.path
import time
import math

SETTINGS_FILE = "RTIMULib"

class IMUWrapper:
    def __init__(self):
        self.imu = RTIMU.RTIMU(RTIMU.Settings(SETTINGS_FILE))
        # this is a good time to set any fusion parameters
        self.imu.setSlerpPower(0.02)
        self.imu.setGyroEnable(True)
        self.imu.setAccelEnable(True)
        self.imu.setCompassEnable(True)
    def getGyro(self):
        if self.imu.IMURead():
            return self.imu.getGyro();
    def getFusionPose(self):
        if self.imu.IMURead():
            return self.imu.getFusionData()

if __name__ == '__main__':
    imu = IMUWrapper();
    poll_interval = imu.IMUGetPollInterval()
    while True:
        r, p, y = imu.getFusionPose();
        print("pose[r]: %f pose[p]: %f pose[y]: %f" % (math.degrees(r), math.degrees(p), math.degrees(y)))
        time.sleep(poll_interval*1.0/1000.0)
