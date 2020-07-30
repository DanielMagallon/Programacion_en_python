import time
from pyfingerprint.pyfingerprint import PyFingerprint

try:
    f = PyFingerprint('/dev/ttyUSB0', 57600, 0xFFFFFFFF, 0x00000000)

    if ( f.verifyPassword() == False ):
        raise ValueError('The given fingerprint sensor password is wrong!')
    else:
        print("What would you want to do?")
        print("\t1) Store a new finger")
        print("\t2) Search a finger")
        print("Type any other key to exit")

        value = int(input())

        if value == 1:
            print("Storing a new finger...")


except Exception as e:
    print('The fingerprint sensor could not be initialized!')
    print('Exception message: ' + str(e))
    exit(1)

