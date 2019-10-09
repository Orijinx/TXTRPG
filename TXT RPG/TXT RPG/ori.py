# -*- coding: utf-8 -*-

import cv2
from PyQt5 import QtCore, QtGui, QtWidgets
import pyqrcode
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import (QLabel,QFileDialog,QAction,QApplication,QMainWindow)
from PyQt5.QtGui import QIcon
import numpy as np
import argparse
import qrtools
from PIL import Image
from pyzbar.pyzbar import decode
import telebot

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Ori")
        MainWindow.resize(640, 480)
        #MainWindow.geometry(self)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.hLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.hLayout.setObjectName('horizLayout')
        self.UrlEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.UrlEdit.setObjectName("UrlEdit")
        self.verticalLayout.addWidget(self.UrlEdit)
        self.Button = QtWidgets.QPushButton(self.centralwidget)
        self.Button.setObjectName("Button")
        self.Button.clicked.connect(self.ButtClicek)
        self.verticalLayout.addWidget(self.Button)
        self.verticalLayout.addLayout(self.hLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        #QRcodePixma
        pixmap = QPixmap("code.png")
        self.lbl = QLabel(self)
        self.lbl.setPixmap(pixmap)
        #self.lbl.mouseDoubleClickEvent(self.DBCLK,pixmap)
        self.hLayout.addWidget(self.lbl)
        #Декодирование QR
        self.dButton = QtWidgets.QPushButton(self.centralwidget)
        self.dButton.setObjectName('dButton')
        self.verticalLayout.addWidget(self.dButton)
        self.dButton.clicked.connect(self.Decoding)
        self.Output = QtWidgets.QLineEdit(self.centralwidget)
        self.Output.setObjectName('OUT')
        self.verticalLayout.addWidget(self.Output)
        #Камера Capture
        self.capButton = QtWidgets.QPushButton(self.centralwidget)
        self.capButton.setObjectName('capButton')
        self.verticalLayout.addWidget(self.capButton)
        self.capButton.clicked.connect(self.CameraCap)
        CamPix = QPixmap("cam.png")
        self.CamL = QLabel(self)
        self.CamL.setPixmap(CamPix)
        self.hLayout.addWidget(self.CamL)

        
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("Ori", "Ori"))
        self.Button.setText(_translate("Ori", "Generate QR"))
        self.dButton.setText(_translate("Ori","Decode QR"))
        self.capButton.setText(_translate("Ori","Capture from CAM"))

    def ButtClicek(self):
        try:
            URL = self.UrlEdit.text()
        except:
            self.Output.setText('Input Error')

        big_code = pyqrcode.create(URL, error='L', version=10,mode='binary')
        big_code.png('code.png', scale=6, module_color=[0, 0, 0, 128], background=[0xff, 0xff, 0xcc])
        pixma = QPixmap("code.png")
        self.lbl.setPixmap(pixma)
#Экшин декодинга
    def Decoding(self):
        try:
            fname = QFileDialog.getOpenFileName(self, 'Open file', '/home')[0]
            qr = decode(Image.open(fname))
            sqr = str(qr[0][0])
            sqr = sqr[2:(len(sqr)-1)]
            print(sqr)
        except:
             self.Output.setText('Error')
        try:
            self.Output.setText(sqr)
        except:
            self.Output.setText('Output Error')
#Акшин захвата камеры
    def CameraCap(self):
        capture = cv2.VideoCapture(0)

        for i in range(30):
           capture.read()
        ret, frame = capture.read()
        cv2.imwrite('cam.png', frame)
        capture.release()

        CamPix = QPixmap("cam.png")
        self.CamL.setPixmap(CamPix)
    
        
    def DBCLK(self,F):
        try:
            qr = decode(Image.open(F))
            sqr = qr[0][0]
            sqr = sqr[2,(len(sqr)-1)]
            self.Output.setText(sqr)
        except:
            self.Output.setText('Decode Error,Check the file')

###############Bot Declaration
def BotDecod(FN): 
    QRAPI = decode(Image.open(FN))
    T = QRAPI[0][0]
    return T

    

