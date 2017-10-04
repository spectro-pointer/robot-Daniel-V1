import serial
import os

arduino = serial.Serial('/dev/ttyACM0', 115200)

print("Starting!")

continuar = True
while continuar:
        comando = raw_input('Introduce un comando: ') #Input
        arduino.write(comando + '\n')  #Mandar un comando hacia Arduino
        print comando 
        if comando == 'exit':
                continuar = False

        grblout=arduino.readline()
        print '     :     ' + grblout.strip()


arduino.close() #Finalizamos la comunicacion
