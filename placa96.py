
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
CoordX = ["X-99", "X-90", "X-81", "X-72", "X-63", "X-54", "X-45", "X-36", "X-28", "X-19", "X-10", "X-1"]
CoordY = ["Y-19.5", "Y-28.5", "Y-37.5", "Y-46.5", "Y-55.5", "Y-64.5", "Y-73.5", "Y-82.5"]
while True:
	Y = raw_input("ejemplo(lettre) Y:       ")
	print Y
	X = raw_input("ejemplo(numero) X:       ")
	print X
	allerY = CoordY[MapY.index(Y)]
	allerX = CoordX[MapX.index(X)]
	#		print "Pas un input valable: Mettez premierement un lettre qui signify le column (A, B, C, D, E, F, G, H)"
	#		print "Puis, mettez un numero qui signify le row desirer (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)"
	comando = (allerX + allerY)
	arduino.write(comando + '\n') 
	print comando 
# time.sleep(0.5)
#      grblout = arduino.readline()
#print'     :     ' + grbl_out.strip()

#arduino.close()
