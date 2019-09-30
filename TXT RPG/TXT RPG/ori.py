import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import (QWidget, QToolTip,
    QPushButton, QApplication,QDialog)
import pyqrcode


class Ui_Ori(QWidget):
    def __init__(self):
        super(Ui_Ori, self).__init__()

    def setupUi(self, Ori):
        Ori.setObjectName("Ori")
        Ori.resize(434, 300)
        self.verticalLayout = QtWidgets.QVBoxLayout(Ori)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lab = QtWidgets.QLabel(Ori)
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.lab.setFont(font)
        self.lab.setTextFormat(QtCore.Qt.AutoText)
        self.lab.setObjectName("lab")
        self.horizontalLayout.addWidget(self.lab)
        self.URLEdit = QtWidgets.QLineEdit(Ori)
        self.URLEdit.setObjectName("URLEdit")
        self.horizontalLayout.addWidget(self.URLEdit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.CreateButton = QtWidgets.QPushButton(Ori)
        self.CreateButton.setAutoFillBackground(True)
        self.CreateButton.setObjectName("CreateButton")
        self.CreateButton.clicked.connect(self.ButtClicek)
        self.gridLayout.addWidget(self.CreateButton, 0, 0, 1, 1)
        self.QRcode = QtWidgets.QGraphicsView(Ori)
        self.QRcode.setObjectName("QRcode")
        self.gridLayout.addWidget(self.QRcode, 1, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.show()

        self.retranslateUi(Ori)
        QtCore.QMetaObject.connectSlotsByName(Ori)

    def retranslateUi(self, Ori):
        _translate = QtCore.QCoreApplication.translate
        Ori.setWindowTitle(_translate("Ori", "Orio"))
        self.lab.setText(_translate("Ori", "URL"))
        self.CreateButton.setText(_translate("Ori", "Generate QR"))

    def ButtClicek(self):
        big_code = pyqrcode.create(self.URLEdit.text, error='L', version=27, mode='binary')
        big_code.png('code.png', scale=6, module_color=[0, 0, 0, 128], background=[0xff, 0xff, 0xcc])
        big_code.show()

if __name__ == '__main__':

    app = QApplication(sys.argv)
    main = Ui_Ori()
    sys.exit(app.exec_())