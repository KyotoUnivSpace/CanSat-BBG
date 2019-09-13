import sys
import RTIMU
import os.path
import time
import math
sys.path.append('.')

SETTINGS_FILE = "RTIMULib"

class IMUWrapper:
    def __init__(self):
        print("Using settings file " + SETTINGS_FILE + ".ini")
        if not os.path.exists(SETTINGS_FILE + ".ini"):
            print("Settings file does not exist, will be created")
        self.s = RTIMU.Settings(SETTINGS_FILE)
        self.imu = RTIMU.RTIMU(self.s)
        print("IMU Name: " + self.imu.IMUName())
        # print(self.imu.IMUInit())
        if not self.imu.IMUInit():
            print("IMU Init Failed")
            sys.exit(1)
        else:
            print("IMU Init Succeeded")
        # this is a good time to set any fusion parameters
        self.imu.setSlerpPower(0.02)
        self.imu.setGyroEnable(True)
        self.imu.setAccelEnable(True)
        self.imu.setCompassEnable(True)
    def getGyro(self):
        return self.imu.getGyro();
    def getFusionPose(self):
        return self.imu.getFusionData()
    def read(self):
        return self.imu.IMURead()
    def getPollInterval(self):
        return self.imu.IMUGetPollInterval()

if __name__ == '__main__':
    imuWrapper = IMUWrapper();
    poll_interval = imuWrapper.getPollInterval()
    while True:
        if imuWrapper.read():
            (r, p, y) = imuWrapper.getFusionPose();
            (_r, _p, _y) = imuWrapper.getGyro();
            print("pose[r]:%f pose[p]:%f pose[y]:%f   gyro[r]:%f gyro[p]:%f gyro[y]:%f" % (math.degrees(r), math.degrees(p), math.degrees(y), math.degrees(_r), math.degrees(_p), math.degrees(_y)))
            time.sleep(poll_interval*1.0/1000.0)
