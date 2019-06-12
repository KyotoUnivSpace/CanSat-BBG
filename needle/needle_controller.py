import math
import time

from servo import Servo


class NeedleController:
    def __init__(self, servo_distance, initial_degrees = [0.0] * 8):
        """
        Args
        ----------
        servo_distance : float
            Distance between an axis of servo motor and a center of needle
            The unit is same as that of "length" in "set_length" function.
        initial_degrees : list of float
            Initial degrees of servo motors
        """
        self.servo_distance = servo_distance
        self.initial_degrees = initial_degrees
        self.servo = Servo()

    def set_length(self, num, length):
        """
        Args
        ----------
        num : int
            The index of servo motor
        length : float
            The length of needle connected with the servo[num]
        """
        radian = math.atan(length / self.servo_distance) + self.initial_degrees[num]
        self.servo.setDegree(num, math.degrees(radian))


if __name__ == "__main__":
    needle = NeedleController(servo_distance = 10)
    try:
        while(True):
            for i in range(10):
                needle.set_length(num = 0, length = i)
                time.sleep(0.2)
    except KeyboardInterrupt:
        pass
