from gpiozero import Button, LED
from signal import pause


button = Button(2)
led = LED(17)
led.off()
