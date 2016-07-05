# DummySCADA

## Introduction

Welcome to DummySCADA. This project is created for the beginners who are interested in Pentesting SCADA Networks. You can download HMI(Human Machine Interface) from repository to control your arduino using serial communication. Every Action that you perform is stored in the database created. 

## Versions
###v1 -> 
HMI: In this version, you can find only HMI where you can connect to arduino and check the automation. You can build other networks for your use(RF). You can learn basic intraction using PySerial with arduino.

###v2 -> 
In Network: You have network architecture - TCP Server and Client. Arduino is connected to the server and HMI is at client side. You can understand the network communication between HMI and arduino and you can learn to pentest SCADA network.
`COMIN SOON`

###v3 -> 
ModBus: Using real SCADA devices you can understand the data transfer between different platforms. TCP Synchronus ModBus communication using Python and you can learn to pentest the DummySCADA with Dummy Netowk, Dummy HMI. 

*This helps SCADA pentesters to demonstrate scenarios and perform various pentesting methods without disturbing real SCADA network.* 

## Things You Need
1. Arduino Mega
2. Ultrasonic Sensor (HC-SR04)
3. L293D Driver IC(Motor)
4. DC Motors
5. Jumper Wires
6. Kali Linux (Any linux)

## Installation

### Preparing system and Prerequisites

`sudo apt-get update`

`sudo apt-get upgrade`

`sudo apt-get install python` (Installing Python 2.7)

`sudo apt-get install python-qt4` (Installing PyQt4)

`sudo apt-get install arduino arduino-core` (Installing Arduino)

`sudo apt-get install gcc-avr avr-libc` (Installing compilers and libraries for arduino)

`pip install pyserial` or https://pypi.python.org/pypi/pyserial/2.7 (Installing PySerial)

*If you use Kali linux, you get arduino default. You have to install PyQt4.*

*If you are using other OS, Install Python, PyQt4, Arduino, PySerial


