# DummySCADA

## Introduction

Welcome to DummySCADA. This project is created for the beginners who are interested in Pentesting SCADA Networks. You can download HMI(Human Machine Interface) from repository to control your arduino using serial communication. Every Action that you perform is stored in the database created. 

![Real "DummySCADA"](https://cloud.githubusercontent.com/assets/15664727/20664120/e6ebccb6-b57f-11e6-82cf-5d19552aefd5.jpg)


## Versions
###v1.
HMI: In this version, you can find only HMI where you can connect to arduino and check the automation. You can build other networks according to your requirements(RF). You can learn basic intraction using PySerial with arduino.

###v2. 
In Network: You have network architecture - TCP Server and Client. Arduino is connected to the server and HMI is at client side. You can understand the network communication between HMI and arduino and you can learn to pentest SCADA network.<br>
*COMING SOON*

###v3.
ModBus: Using real SCADA devices you can understand the data transfer between different platforms. TCP Synchronus ModBus communication using Python and you can learn to pentest the DummySCADA with Dummy Netowk, Dummy HMI. <br>
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
2. Arduino<br>
    port 25    L293D pin 1<br>
    port 26    L293D pin 2<br>
    port 27    L293D pin 7<br>
    port 11    HC-SR04 Trig<br>
    port 12    HC-SR04 Echo<br><br>

    L293D 4, 5, 12, 13   9V Battery GND(-)<br>
    L293D 3    DC Motor Yellow <br>
    L293D 6    DC Motor Green<br>
    L293D 8    9V Battery Power(+)<br><br>
    
    HC-SR04 VCC    Ard 5V<br>
    HC-SR04 GND    Ard GND<br>
    
*You can add 2 more motors like this continuing from pin 28 with same L293D PIN structure.*

###Database
`$ service mysql start`

`$ mysql`

`mysql> CREATE USER 'Admin' IDENTIFIED BY 'Admin@143';`<br>

*Once you restart your system, you need to login as database user in order to avoid errors*<br>

`$ mysql -u admin -p`<br>

*Enter Admin@143 as password*

`mysql> CREATE DATABASE scada_client;`<br>

`mysql> USE scada_client;`<br>

`mysql> CREATE TABLE DAM (da DATE, user VARCHAR(20), status VARCHAR(10), ti TIME);`<br>

`mysql> CREATE TABLE Gate1 (da DATE, user VARCHAR(20), status VARCHAR(10), ti TIME);`<br>

`mysql> CREATE TABLE Gate2 (da DATE, user VARCHAR(20), status VARCHAR(10), ti TIME);`<br>

`mysql> CREATE TABLE Gate3 (da DATE, user VARCHAR(20), status VARCHAR(10), ti TIME);`<br>

`mysql> CREATE TABLE level (da DATE, user VARCHAR(20), status VARCHAR(10), ti TIME, volume varchar(50), depth varchar(50));`<br>

`mysql> SHOW TABLES;`<br>





###Interface
1. Cloning GIT<br>
`$ git clone https://github.com/Pradyumna007/dummyscada.git`

2. Unzip `dummyscada-master.zip`

3. Upload `test.ino` into Arduino board.<br> 
*This helps you test interface between Arduino and Python HMI.*<br>

4. Run dummyscada.py <br>
`python dummyscada.py`<br><br>

    `Click Gate 1 to run the Motor`<br>
    `Click Gate 1 Stop to Turn Off the Motor`<br>
    `Click Gate 1 Close to run the Motor in anti-clockwise direction` <br><br>

5. Upload `dummyscada.ino` into Arduino board.<br>
*If test.ino is successful upload dummyscada.ino into board.*<br><br>

6. Run dummyscada.py <br>
`python dummyscada.py`<br><br>

7. Check all the buttons that are available.<br>
`Click on Buttons to get the appropriate Output`<br><br>

*Each Motor represents Each Gate. Gate1 for the first motor, Gate2 for second Motor, Gate3 for Third motor and DAM for all 3 gates at a time. If you have only 1 motor and try to execute it by clicking on Gate2, IT MIGHT THROW SOME ERRORS.* <br><br>

##Authors 
* [Pradyumna Cheerala](https://github.com/Pradyumna007) has completely designed and maintained the Project.
   1. [Facebook](https://www.facebook.com/Pradyumna.Cheerala.hackie)
   2. [Linked In](https://www.linkedin.com/in/pradyumna-ch-21a74762)

##License
This project is licensed under the GNU License - see the [LICENSE](https://github.com/Pradyumna007/dummyscada/blob/master/LICENSE) file for details.

##Acknowledgment
* I am greatful to [Justin Searle](https://www.linkedin.com/in/meeas) who provided insight and expertise that greatly assisted the research.

