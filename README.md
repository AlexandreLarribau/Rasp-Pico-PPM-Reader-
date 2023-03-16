# Rasp-Pico-PPM-Reader-
This code is a micropython code permitting to read a PPM signal coming on a raspberry pico pin. 

It first defines a RCChannels Class which takes as arguments the input pin and the number of channels expected. 

Then it detects the maximum value, which is the end of each period before the ppm start again. 

Then we are able to reorder the channel and remove the value that carries no informations. 
