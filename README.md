# Rasp-Pico-PPM-Reader-
This code is a micropython code permitting to read a PPM signal coming on a raspberry pico pin. 

The point is to separate the channels of a ppm signal of a RC receiver (in my case the FLYSKY FSI6) containing a fix number of PWM values.

It first defines a RCChannels Class which takes as arguments the input pin and the number of channels expected. 

In my case, I had a period of 20ms between each packets but one can easily modify the line 11 to get the value of his choice. 

Then it detects the maximum value, which is the end of each period before the ppm start again. 

Then we are able to reorder the channel and remove the value that carries no informations. 
