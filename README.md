# DummySCADA

## Introduction

Welcome to DummySCADA. This project is created for the beginners who are interested in Pentesting SCADA Networks. You can download HMI(Human Machine Interface) from repository to control your arduino using serial communication. Every Action that you perform is stored in the database created. 

## Versions
###v1.
HMI: In this version, you can find only HMI where you can connect to arduino and check the automation. You can build other networks for your use(RF). You can learn basic intraction using PySerial with arduino.

###v2. 
In Network: You have network architecture - TCP Server and Client. Arduino is connected to the server and HMI is at client side. You can understand the network communication between HMI and arduino and you can learn to pentest SCADA network.
*COMING SOON*

###v3.
ModBus: Using real SCADA devices you can understand the data transfer between different platforms. TCP Synchronus ModBus communication using Python and you can learn to pentest the DummySCADA with Dummy Netowk, Dummy HMI. 
*COMING SOON*


*This helps SCADA pentesters to demonstrate scenarios and perform various pentesting methods without disturbing real SCADA network.* 

## Things You Need
1. Arduino Mega                     x1
2. Ultrasonic Sensor (HC-SR04)      x1
3. L293D Driver IC(Motor)           x3
4. DC Motors                        x3
5. 9v DC Battery
5. Jumper Wires                     x as required
6. Kali Linux (Any linux)

## Installation

### Preparing system and Prerequisites

`$ sudo apt-get update`

`$ sudo apt-get upgrade`

`$ sudo apt-get install python` (Installing Python 2.7)

`$ sudo apt-get install python-qt4` (Installing PyQt4)

`$ sudo apt-get install arduino arduino-core` (Installing Arduino)

`$ sudo apt-get install gcc-avr avr-libc` (Installing compilers and libraries for arduino)

`$ pip install pyserial` or https://pypi.python.org/pypi/pyserial/2.7 (Installing PySerial)

`$ pip install python-handler-socket` (Installing Socket)

`$ pip install MySQL-python` (Installing MySQLdb)

*If you use Kali linux, you get arduino pre-installed. You have to install PyQt4 and other libraries.*

*If you are using other OS, Install Python, PyQt4, Arduino, PySerial, MySQLdb, os, time, hashlib, sys*


##Setting up system

###Connections
1. Check out connections.jpg and connect the devices according. 
2. Arduino
    port 25    L293D pin 1
    port 26    L293D pin 2
    port 27    L293D pin 7
    port 11    HC-SR04 Trig
    port 12    HC-SR04 Echo

    L293D 4, 5, 12, 13   9V Battery GND(-)
    L293D 3    DC Motor Yellow 
    L293D 6    DC Motor Green
    L293D 8    9V Battery Power(+)
    
    HC-SR04 VCC    Ard 5V
    HC-SR04 GND    Ard GND
    
    
