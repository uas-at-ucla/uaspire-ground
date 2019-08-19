#!/usr/bin/env python3

from servo import Servo

def main():
    s = Servo(180, 0.001)
    s.plotAngleAgainstTime()
    while True:
        print(s.getCurAngle())
        s.hold(1)

if __name__ == '__main__':
    main()
    