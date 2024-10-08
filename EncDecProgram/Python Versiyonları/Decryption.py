# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Decryption.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1086, 531)
        Form.setStyleSheet("#Form{\n"
"border-image: url(:/EncDec Background/encrypDecryptBackgroudn.jpg);\n"
"}")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(0, 0, 1081, 531))
        self.frame.setStyleSheet("#frame{\n"
"border-image: url(:/EncDec Background/encrypDecryptBackgroudn.jpg);\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.lineEdit_KeyN = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_KeyN.setGeometry(QtCore.QRect(720, 190, 241, 20))
        self.lineEdit_KeyN.setObjectName("lineEdit_KeyN")
        self.textEdit_DecryptedT = QtWidgets.QTextEdit(self.frame)
        self.textEdit_DecryptedT.setGeometry(QtCore.QRect(660, 220, 411, 271))
        self.textEdit_DecryptedT.setStyleSheet("background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:0, stop:0 rgba(70, 180, 255, 223), stop:1 rgba(255, 255, 255, 255));")
        self.textEdit_DecryptedT.setReadOnly(True)
        self.textEdit_DecryptedT.setObjectName("textEdit_DecryptedT")
        self.textEdit_EncryptedT = QtWidgets.QTextEdit(self.frame)
        self.textEdit_EncryptedT.setGeometry(QtCore.QRect(30, 220, 411, 271))
        self.textEdit_EncryptedT.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.011, y1:0, x2:1, y2:0, stop:0 rgba(70, 180, 255, 223), stop:1 rgba(255, 255, 255, 255));")
        self.textEdit_EncryptedT.setObjectName("textEdit_EncryptedT")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(660, 190, 61, 16))
        self.label_2.setStyleSheet("font: 87 11pt \"Segoe UI Black\";\n"
"color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.pushButton_Decrypt = QtWidgets.QPushButton(self.frame)
        self.pushButton_Decrypt.setGeometry(QtCore.QRect(970, 190, 101, 23))
        self.pushButton_Decrypt.setStyleSheet("background-color: qlineargradient(spread:reflect, x1:0, y1:0.0170455, x2:0.494, y2:0.0284091, stop:0.142045 rgba(147, 245, 227, 255), stop:0.818182 rgba(0, 59, 93, 255));\n"
"font: 87 9pt \"Segoe UI Black\";\n"
"color: rgb(68, 195, 209);")
        self.pushButton_Decrypt.setObjectName("pushButton_Decrypt")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(30, 190, 141, 20))
        self.label_3.setStyleSheet("font: 87 10pt \"Segoe UI Black\";\n"
"color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(480, 270, 171, 141))
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
        self.lineEdit_KeyN_2 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_KeyN_2.setGeometry(QtCore.QRect(720, 150, 241, 20))
        self.lineEdit_KeyN_2.setObjectName("lineEdit_KeyN_2")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(660, 150, 61, 16))
        self.label_4.setStyleSheet("font: 87 11pt \"Segoe UI Black\";\n"
"color: rgb(255, 255, 255);")
        self.label_4.setObjectName("label_4")
        self.lineEdit_KeyN_3 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_KeyN_3.setGeometry(QtCore.QRect(720, 110, 241, 20))
        self.lineEdit_KeyN_3.setObjectName("lineEdit_KeyN_3")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(660, 110, 61, 16))
        self.label_5.setStyleSheet("font: 87 11pt \"Segoe UI Black\";\n"
"color: rgb(255, 255, 255);")
        self.label_5.setObjectName("label_5")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_2.setText(_translate("Form", "Key1:"))
        self.pushButton_Decrypt.setText(_translate("Form", "Check"))
        self.label_3.setText(_translate("Form", "Text to be decrypted:"))
        self.label.setText(_translate("Form", "→"))
        self.label_4.setText(_translate("Form", "Nonce:"))
        self.label_5.setText(_translate("Form", "Tag:"))
import Resimler_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
