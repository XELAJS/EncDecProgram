# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ImageEncrypt.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1085, 522)
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(0, 0, 1081, 521))
        self.frame.setStyleSheet("#frame{\n"
"border-image: url(:/EncDec Background/encrypDecryptBackgroudn.jpg);\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(650, 140, 61, 16))
        self.label_4.setStyleSheet("font: 87 10pt \"Segoe UI Black\";\n"
"color: rgb(255, 255, 255);")
        self.label_4.setObjectName("label_4")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(480, 230, 141, 161))
        font = QtGui.QFont()
        font.setFamily("Rockwell Extra Bold")
        font.setPointSize(100)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.label.setFont(font)
        self.label.setStyleSheet("font: 81 100pt \"Rockwell Extra Bold\";\n"
"color: qlineargradient(spread:reflect, x1:0, y1:0.0170455, x2:0.494, y2:0.0284091, stop:0.130682 rgba(0, 59, 93, 255), stop:0.846591 rgba(209, 245, 236, 255));")
        self.label.setObjectName("label")
        self.lineEdit_EMail = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_EMail.setGeometry(QtCore.QRect(730, 140, 221, 20))
        self.lineEdit_EMail.setText("")
        self.lineEdit_EMail.setObjectName("lineEdit_EMail")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(20, 170, 121, 20))
        self.label_3.setStyleSheet("font: 87 10pt \"Segoe UI Black\";\n"
"color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.lineEdit_Name = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_Name.setGeometry(QtCore.QRect(730, 170, 221, 20))
        self.lineEdit_Name.setObjectName("lineEdit_Name")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(650, 170, 81, 16))
        self.label_2.setStyleSheet("font: 87 10pt \"Segoe UI Black\";\n"
"color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.pushButton_SendC = QtWidgets.QPushButton(self.frame)
        self.pushButton_SendC.setGeometry(QtCore.QRect(960, 140, 101, 23))
        self.pushButton_SendC.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0.0113636, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(191, 191, 191, 255));\n"
"\n"
"font: 87 8pt \"Segoe UI Black\";\n"
"color: rgb(170, 255, 255);")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/mesajİcon/icons8-send-48.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_SendC.setIcon(icon)
        self.pushButton_SendC.setObjectName("pushButton_SendC")
        self.textEdit_EText = QtWidgets.QTextEdit(self.frame)
        self.textEdit_EText.setGeometry(QtCore.QRect(650, 200, 411, 271))
        self.textEdit_EText.setStyleSheet("background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:0, stop:0 rgba(70, 180, 255, 223), stop:1 rgba(255, 255, 255, 255));")
        self.textEdit_EText.setReadOnly(True)
        self.textEdit_EText.setObjectName("textEdit_EText")
        self.pushButton_Encrypt = QtWidgets.QPushButton(self.frame)
        self.pushButton_Encrypt.setGeometry(QtCore.QRect(960, 170, 101, 23))
        self.pushButton_Encrypt.setStyleSheet("background-color: qlineargradient(spread:reflect, x1:0, y1:0.0170455, x2:0.494, y2:0.0284091, stop:0.130682 rgba(0, 59, 93, 255), stop:0.880682 rgba(147, 245, 227, 255));\n"
"font: 87 9pt \"Segoe UI Black\";\n"
"color: rgb(0, 0, 255);")
        self.pushButton_Encrypt.setObjectName("pushButton_Encrypt")
        self.comboBox_Encryptions = QtWidgets.QComboBox(self.frame)
        self.comboBox_Encryptions.setGeometry(QtCore.QRect(140, 170, 291, 22))
        self.comboBox_Encryptions.setObjectName("comboBox_Encryptions")
        self.pushButton_Encrypt_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_Encrypt_2.setGeometry(QtCore.QRect(220, 310, 101, 23))
        self.pushButton_Encrypt_2.setStyleSheet("background-color: qlineargradient(spread:reflect, x1:0, y1:0.0170455, x2:0.494, y2:0.0284091, stop:0.130682 rgba(0, 59, 93, 255), stop:0.880682 rgba(147, 245, 227, 255));\n"
"font: 87 9pt \"Segoe UI Black\";\n"
"color: rgb(0, 0, 0);")
        self.pushButton_Encrypt_2.setObjectName("pushButton_Encrypt_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_4.setText(_translate("Form", "E-Mail:"))
        self.label.setText(_translate("Form", "→"))
        self.label_3.setText(_translate("Form", "Encryption Name:"))
        self.label_2.setText(_translate("Form", "Image name:"))
        self.pushButton_SendC.setText(_translate("Form", "Send Code"))
        self.pushButton_Encrypt.setText(_translate("Form", "Encrypt"))
        self.pushButton_Encrypt_2.setText(_translate("Form", "Fotoğraf Yükle"))
import Resimler_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
