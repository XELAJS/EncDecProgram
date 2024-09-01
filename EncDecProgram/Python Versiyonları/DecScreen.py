from PyQt5.QtWidgets import *
from Decryption import Ui_Form
import sys
sys.path.append(r"C:\Users\msı\AppData\Local\Programs\Python\Python312\Lib\site-packages")
from Crypto.Cipher import AES
import Resimler_rc
import ast
import base64
from cryptography.fernet import Fernet

class DecPage(QWidget):   
    AESMi=False
    FernetMi=False
    sezarMi=False
    ciphertext=" "
    def __init__(self):
        super().__init__()
        self.DecForm= Ui_Form()
        self.DecForm.setupUi(self)
        self.DecForm.label_4.setVisible(False)
        self.DecForm.label_5.setVisible(False)
        self.DecForm.lineEdit_KeyN_2.setVisible(False)
        self.DecForm.lineEdit_KeyN_3.setVisible(False)
        self.DecForm.pushButton_Decrypt.clicked.connect(self.ChckandDecrypt)
    
    def show_message(self, title, message):
        msg = QMessageBox()
        msg.setWindowTitle(title)
        msg.setText(message)
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()
    
    def DecAES(self, tag, nonce, key):
        
        
        self.ciphertext = base64.b64decode(self.DecForm.textEdit_EncryptedT.toPlainText())
        tag = base64.b64decode(tag)
        key = base64.b64decode(key)
        nonce = base64.b64decode(nonce)
        
       
        cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
        decrypted_text = cipher.decrypt(self.ciphertext)
        
        print(decrypted_text)
        
        try:
            cipher.verify(tag)
            decrypted_text_str = decrypted_text.decode("utf8")
            self.DecForm.textEdit_DecryptedT.setText(decrypted_text_str)
        except ValueError:
            self.show_message("Hata", "Girdiğiniz değerler eksik veya hatalıdır.")
        
    def DecFernet(self,key):
        encrypted_message = self.DecForm.textEdit_EncryptedT.toPlainText()
        print(key)
        key_bytes = base64.urlsafe_b64decode(key)
        print()
        print(key_bytes)
        encrypted_message_bytes = base64.urlsafe_b64decode(encrypted_message)
            
        print(encrypted_message)
        print()
        print()
        
        cipher_suite = Fernet(key_bytes)
        decrypted_text = cipher_suite.decrypt(encrypted_message_bytes).decode()
        print(decrypted_text)
        self.DecForm.textEdit_DecryptedT.setText(decrypted_text)
            

    def SezarDec(self, text, otelemeS):
        cozulmus_metin = ""
        for i in text:
            cozulmus_metin += chr(ord(i) - int(otelemeS))
        return cozulmus_metin
        
    
    def ChckandDecrypt(self):
        
        if self.DecForm.pushButton_Decrypt.text() == "Check" and self.DecForm.lineEdit_KeyN.text().strip() == "J7LyJ9OPqX":
            self.DecForm.label_4.setVisible(True)
            self.DecForm.label_5.setVisible(True)
            self.DecForm.lineEdit_KeyN_2.setVisible(True)
            self.DecForm.lineEdit_KeyN_3.setVisible(True)
            self.DecForm.pushButton_Decrypt.setText("Decrypt")
            self.DecForm.lineEdit_KeyN_2.setText("")
            self.DecForm.lineEdit_KeyN_3.setText("")
            self.DecForm.lineEdit_KeyN.setText("")
            self.DecForm.label_2.setText("Key")
            self.AESMi = True
            
        elif self.DecForm.pushButton_Decrypt.text() == "Check" and self.DecForm.lineEdit_KeyN.text().strip() == "SEQyJ1FeYz" or self.DecForm.lineEdit_KeyN.text().strip() == "qZTs8JH1QB": 
            self.DecForm.pushButton_Decrypt.setText("Decrypt")
            if self.DecForm.lineEdit_KeyN.text()=="SEQyJ1FeYz":
                self.FernetMi=True
            elif self.DecForm.lineEdit_KeyN.text()== "qZTs8JH1QB":
                self.sezarMi=True
            self.DecForm.lineEdit_KeyN_2.setText("")
            self.DecForm.lineEdit_KeyN_3.setText("")
            self.DecForm.lineEdit_KeyN.setText("")
            self.DecForm.label_2.setText("Key")
            self.DecForm.label_4.setVisible(False)
            self.DecForm.label_5.setVisible(False)
            self.DecForm.lineEdit_KeyN_2.setVisible(False)
            self.DecForm.lineEdit_KeyN_3.setVisible(False)
            self.AESMi = False
           
        else:
            self.DecForm.pushButton_Decrypt.setText("Check")
            self.DecForm.label_2.setText("Key1")
            self.DecForm.label_4.setVisible(False)
            self.DecForm.label_5.setVisible(False)
            self.DecForm.lineEdit_KeyN_2.setVisible(False)
            self.DecForm.lineEdit_KeyN_3.setVisible(False)
            if self.AESMi:
                tag = self.DecForm.lineEdit_KeyN_3.text().strip()
                nonce = self.DecForm.lineEdit_KeyN_2.text().strip()
                key = self.DecForm.lineEdit_KeyN.text().strip()
                self.DecAES(tag, nonce, key)
            elif self.FernetMi==True:
                 self.key= self.DecForm.lineEdit_KeyN.text().strip()
                 self.DecFernet(self.key)
            elif self.sezarMi==True:
                self.key=self.DecForm.lineEdit_KeyN.text().strip()
                bolKey_ilk, separator, otelemeS = self.key.partition('-')
                
                normalMetin = self.SezarDec(self.DecForm.textEdit_EncryptedT.toPlainText(), int(otelemeS))
                self.DecForm.textEdit_DecryptedT.setText(normalMetin)
                
