import machine
import time

class RCChannels:
    def __init__(self, pin, nb):
        self.pin = machine.Pin(pin, machine.Pin.IN)
        self.channels = [0] * nb
        
    def read(self):
        for i in range(len(self.channels)):
            self.channels[i] = int(machine.time_pulse_us(self.pin, 20000))
        return self.channels

rc_channels = RCChannels(11, 9)

while True:
    channels = rc_channels.read()
    max_value = max(channels)
    index = channels.index(max_value)
    
    # Reorder the channels list so that the first value is the first PPM channel
    channels = channels[index+1:] + channels[:index]
    
    # Remove the last value which is the end of the PPM cycle
    channels.pop()
    
    print(channels)
    time.sleep(0.1)
