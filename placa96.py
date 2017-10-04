
#!python 

# array placa 96 posiciones D6mm P 11mm
import serial 
from ctypes import *
import time
import os

arduino = serial.Serial('/dev/ttyACM0', 115200)
print "conectando"
grbl_out = arduino.readline() # Wait for grbl response with carriage return
print ' : ' + grbl_out.strip()
time.sleep(.5)
arduino.write('$X' + '\n')
grbl_out = arduino.readline()
print ' : ' + grbl_out.strip()
time.sleep(1)
arduino.write('$H' + '\n')
time.sleep(5)
grbl_out = arduino.readline()
print ' : ' + grbl_out.strip()
print "home hecho"
arduino.write('??' + '\n')
grbl_out = arduino.readline()
print ' : ' + grbl_out.strip()
print "status"
time.sleep(1)

print "aduino conectado"
MapX = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"]
MapY = ["A", "B", "C", "D", "E", "F", "G", "H"]
CoordX = ["X-91", "X-82", "X-73", "X-64", "X-55", "X-46", "X-37", "X-29", "X-20", "X-11", "X-11"]
CoordY = ["Y-18.5", "Y-27.5", "Y-36.5", "Y-45.5", "Y-54.5", "Y-63.5", "Y-72.5", "Y-81.5"]

Y = raw_input("ejemplo(lettre) Y:       ")
print Y
X = raw_input("ejemplo(numero) X:       ")
print X
allerY = CoordY[MapY.index(str(Y))]
allerX = CoordX[MapX.index(str(X))]
#		print "Pas un input valable: Mettez premierement un lettre qui signify le column (A, B, C, D, E, F, G, H)"
#		print "Puis, mettez un numero qui signify le row desirer (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)"
comando = (allerX + allerY)
arduino.write(comando + '\n') 
print comando 
# time.sleep(0.5)
#      grblout = arduino.readline()
#print'     :     ' + grbl_out.strip()

#arduino.close()
