from __future__ import division
import time
import math
import Adafruit_PCA9685
import Adafruit_GPIO.I2C as I2C

class Servo:
    # Operate seven servos. servo0~servo7
    def __init__(self):
        self.pwm = Adafruit_PCA9685.PCA9685(busnum = 2, i2c = I2C)
        self.pwm.set_pwm_freq(50) # Hz
        self.zeroduty = 98
        self.piduty = 485
        self.deg=[90 for _ in range(8)]
        for i in range(8):
            if i%2:
                self.deg[i]=90+45
            else:
                self.deg[i]=90-45
        for i in range(8):
            self.setDegree(i, self.deg[i])
        
        
    def setBasicDuty(self, zero, pi):
        # 1cycle--4096
        self.zeroduty = zero
        self.piduty = pi

    def setDegree(self, num, degree):
        if degree >=0 and degree <=180 and num>=0 and num<=7:
            count = float(self.zeroduty) + (self.piduty - self.zeroduty) * degree / 180.0
            count = int(math.floor(count + 0.5))
            self.pwm.set_pwm(num, 0, count)
            
    def rotate(self):
        flag=[True for _ in range(8)]
        diff=45
        while(1):
            # r = input()
            # self.setDegree(0, r)
            time.sleep(0.001)
            for i in range(8):
                if flag[i]:
                    r = self.deg[i]+1
                else:
                    r =self.deg[i]-1
                if (r > 90+diff):
                    r = 90+diff
                    flag[i] = not flag[i]
                if (r < 90-diff):
                    r = 90-diff
                    flag[i] = not flag[i]
                # r = input()
                self.deg[i]=r
                self.setDegree(i, r)
        
        

if __name__ == "__main__":
    servo = Servo()
    try:
        print("start")
        servo.rotate()
    except KeyboardInterrupt:
        pass