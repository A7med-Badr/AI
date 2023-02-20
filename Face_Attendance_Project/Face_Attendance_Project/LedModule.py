import RPi.GPIO as GPIO
from time import sleep 

GPIO.setmode(GPIO.BCM)

class ledRBG():
    def __init__(self,R,B,G):
        self.R = R
        self.B = B
        self.G = G
        GPIO.setup(self.R, GPIO.OUT)
        GPIO.setup(self.B, GPIO.OUT)
        GPIO.setup(self.G, GPIO.OUT)
    
    def color(self, myColor):
        if myColor == 'red':
            GPIO.output(self.R, GPIO.LOW)
            GPIO.output(self.B, GPIO.HIGH)
            GPIO.output(self.G, GPIO.HIGH)
        elif myColor == 'blue':
            GPIO.output(self.R, GPIO.HIGH)
            GPIO.output(self.B, GPIO.LOW)
            GPIO.output(self.G, GPIO.HIGH)
        elif myColor == 'green':
            GPIO.output(self.R, GPIO.HIGH)
            GPIO.output(self.B, GPIO.HIGH)
            GPIO.output(self.G, GPIO.LOW)
        elif myColor == 'off':
            GPIO.output(self.R, GPIO.HIGH)
            GPIO.output(self.B, GPIO.HIGH)
            GPIO.output(self.G, GPIO.HIGH)
        elif myColor == 'white':
            GPIO.output(self.R, GPIO.LOW)
            GPIO.output(self.B, GPIO.LOW)
            GPIO.output(self.G, GPIO.LOW)

def main():
    myLed = ledRBG(17,27,22)
    while True:
        myLed.color('red')
        sleep(1)
        myLed.color('blue')
        sleep(1)
        myLed.color('green')
        sleep(1)
        myLed.color('off')
        sleep(1)
        myLed.color('white')
        sleep(1)

if __name__ == "__main__":
    main()


