#!/usr/bin/python

from PyQt4 import QtCore, QtGui, uic
import socket
import sys
import MySQLdb
import hashlib
import os
import serial
import time


ser = serial.Serial("/dev/ttyACM0", 9600)
x = ser.write
a = time.strftime("%Y-%m-%d")
ti = time.strftime("%H:%M:%S")

serial_class = uic.loadUiType("mainmenuc.ui")[0]

class serialwindow(QtGui.QMainWindow, serial_class):
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        self.setupUi(self)

        self.dam.clicked.connect(self.dam_application)
        self.gate1.clicked.connect(self.gate1_application)
        self.gate2.clicked.connect(self.gate2_application)
        self.gate3.clicked.connect(self.gate3_application)
        self.std.clicked.connect(self.std_application)
        self.st1.clicked.connect(self.st1_application)
        self.st2.clicked.connect(self.st2_application)
        self.st3.clicked.connect(self.st3_application)
        self.damc.clicked.connect(self.damc_application)
        self.g1c.clicked.connect(self.g1c_application)
        self.g2c.clicked.connect(self.g2c_application)
        self.g3c.clicked.connect(self.g3c_application)
        self.vol.clicked.connect(self.vol_application)
        self.lev.clicked.connect(self.lev_application)
        self.db.clicked.connect(self.db_application)
        self.ser.clicked.connect(self.ser_application)
        self.close3.clicked.connect(self.close3_application)


    @QtCore.pyqtSlot()

    def dam_application(self):
        x('i') # 3 LEDs 3 Buzzers 3 Motors
        i = ser.readline(13)
        print i

        if i:
            conn = MySQLdb.connect(user = "admin", passwd = "Admin@143", db = "scada_client")

            with conn:
                cur = conn.cursor()
                sql = '''INSERT INTO DAM(da, user, status, ti) \
                                VALUES (%s, %s, %s, %s)'''
                cur.execute(sql, (a, 'Client', 'ON', ti))
            


    def gate1_application(self):
        x('g')#GATE 1 LED Buzzer Motor
        g = ser.readline(13)
        print g

        if g:
            conn = MySQLdb.connect(user = "admin", passwd = "Admin@143", db = "scada_client")

            with conn:
                cur = conn.cursor()
                sql = '''INSERT INTO Gate1(da, user, status, ti) \
                                VALUES (%s, %s, %s, %s)'''
                cur.execute(sql, (a, 'Client', 'ON', ti))
      
    
    def gate2_application(self):
        x('z')#GATE 2 LED Buzzer Motor
        z = ser.readline(13)
        print z

        if a:
            conn = MySQLdb.connect(user = "admin", passwd = "Admin@143", db = "scada_client")

            with conn:
                cur = conn.cursor()
                sql = '''INSERT INTO Gate2(da, user, status, ti) \
                                VALUES (%s, %s, %s, %s)'''
                cur.execute(sql, (a, 'Client', 'ON', ti))


        
    def gate3_application(self):
        x('b')#GATE 3 LED Buzzer Motor
        b = ser.readline(13)
        print b

        if b:
            conn = MySQLdb.connect(user = "admin", passwd = "Admin@143", db = "scada_client")

            with conn:
                cur = conn.cursor()
                sql = '''INSERT INTO Gate3(da, user, status, ti) \
                                VALUES (%s, %s, %s, %s)'''
                cur.execute(sql, (a, 'Client', 'ON', ti))



    def std_application(self):
        x('m')
        l = ser.read(13)
        print l

    def st1_application(self):
        x('l')
        l = ser.readline(13)
        print l

    def st2_application(self):
        x('n')
        l = ser.read(13)
        print l

    def st3_application(self):
        x('o')
        l = ser.read(13)
        print l


        
    def damc_application(self):
        x('c')# 3 LEDs 3 Buzzers 3 Motors OFF
        c = ser.readline(13)
        print c

        if c:
            conn = MySQLdb.connect(user = "admin", passwd = "Admin@143", db = "scada_client")

            with conn:
                cur = conn.cursor()
                sql = '''INSERT INTO DAM(da, user, status, ti) \
                                VALUES (%s, %s, %s, %s)'''
                cur.execute(sql, (a, 'Client', 'OFF', ti))
        
    def g1c_application(self):
        x('e')#GATE 1 LED Buzzer Motor OFF
        e = ser.read(13)
        print e

        if e:
            conn = MySQLdb.connect(user = "admin", passwd = "Admin@143", db = "scada_client")

            with conn:
                cur = conn.cursor()
                sql = '''INSERT INTO Gate1(da, user, status, ti) \
                                VALUES (%s, %s, %s, %s)'''
                cur.execute(sql, (a, 'Client', 'OFF', ti))

        
    def g2c_application(self):
        x('f')#GATE 1 LED Buzzer Motor OFF
        f = ser.readline(13)
        print f

        if f:
            conn = MySQLdb.connect(user = "admin", passwd = "Admin@143", db = "scada_client")

            with conn:
                cur = conn.cursor()
                sql = '''INSERT INTO Gate2(da, user, status, ti) \
                                VALUES (%s, %s, %s, %s)'''
                cur.execute(sql, (a, 'Client', 'OFF', ti))

        
    def g3c_application(self):
        x('j')#GATE 1 LED Buzzer Motor OFF
        j = ser.readline(13)
        print j

        if j:
            conn = MySQLdb.connect(user = "admin", passwd = "Admin@143", db = "scada_client")

            with conn:
                cur = conn.cursor()
                sql = '''INSERT INTO Gate3(da, user, status, ti) \
                                VALUES (%s, %s, %s, %s)'''
                cur.execute(sql, (a, 'Client', 'OFF', ti))

    
    def vol_application(self):
        x('v')
        v = ser.readline()
        print 'Volume :', v

        if v:
            conn = MySQLdb.connect(user = "admin", passwd = "Admin@143", db = "scada_client")

            with conn:
                cur = conn.cursor()
                sql = '''INSERT INTO level(da, user, status, ti, volume) \
                                VALUES (%s, %s, %s, %s, %s)'''
                cur.execute(sql, (a, 'Client', 'OFF', ti, v))


    def lev_application(self):
        x('k')
        k = ser.readline()
        print 'Depth :', k

        if k:
            conn = MySQLdb.connect(user = "admin", passwd = "Admin@143", db = "scada_client")

            with conn:
                cur = conn.cursor()
                sql = '''INSERT INTO level(da, user, status, ti, depth) \
                                VALUES (%s, %s, %s, %s, %s)'''
                cur.execute(sql, (a, 'Client', 'OFF', ti, k))


    def db_application(self):
        print "Connecting to the Database.... \n"

        conn = MySQLdb.connect(user = "admin", passwd = "Admin@143", db = "scada_client")

        with conn:
            cur = conn.cursor()
            if cur:
                print "Database scada_client connected\n"


    def ser_application(self):
        if ser:
            print "In serial communication with /dev/ttyACM0"


 

    def close3_application(self):
        choice = QtGui.QMessageBox.question(self, 'Extract', "You want to exit SCADA Client ?", QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)

        if choice == QtGui.QMessageBox.Yes:
            print 'Exiting'
            sys.exit()
        else:
            pass

     

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    mySerial = serialwindow(None)
    mySerial.show()
    sys.exit(app.exec_())
        
