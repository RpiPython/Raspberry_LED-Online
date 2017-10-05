import RPi.GPIO as GPIO # Importar libreria de GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(21,GPIO.OUT)

for i in range (0,5):

	GPIO.output(21,GPIO.HIGH)
	time.sleep(1)
	GPIO.output(21,GPIO.LOW)
	time.sleep(1)

GPIO.cleanup()
