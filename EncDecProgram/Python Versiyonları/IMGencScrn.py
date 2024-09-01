from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap
from DogrulamaEkraniAna import DogruPage
from ImageEncrypt import Ui_Form
import sys
import rsa
import base64
from email.mime.text import MIMEText
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from Crypto.Cipher import ChaCha20
from Crypto.Random import get_random_bytes

class ImgEncScreen(QWidget):
    verif = False
    key = " "
    nonce = " "
    EncText = " "
    
    def __init__(self):
        super().__init__()
        self.ImageEncForm = Ui_Form()
        self.ImageEncForm.setupUi(self)
        self.ImageEncForm.comboBox_Encryptions.addItem(" ")
        self.ImageEncForm.comboBox_Encryptions.addItem("RSA")
        self.ImageEncForm.comboBox_Encryptions.addItem("ChaCha20")
        self.DogruAc = DogruPage()
        self.ImageEncForm.pushButton_Encrypt_2.clicked.connect(self.upload_image)
        self.ImageEncForm.pushButton_Encrypt.clicked.connect(self.CheckAndEnc)
        self.ImageEncForm.pushButton_SendC.clicked.connect(self.AcDogru)
    
    def AcDogru(self):
        aliciMail = self.ImageEncForm.lineEdit_EMail.text()
        self.DogruAc.sendEmail(aliciMail)
        if self.DogruAc.dogrulama:
            self.DogruAc.show()
    
    def CheckAndEnc(self):
        self.verif = self.DogruAc.verify
        algoritma = self.ImageEncForm.comboBox_Encryptions.currentText()
        if algoritma.strip() == "RSA":
            if self.image_path.strip() == "":
                self.show_message("Hata", "Lütfen resim seçiniz.")
            else:
                self.rsa_encrypt_file(self.image_path)
        elif algoritma.strip() == "ChaCha20":
            if self.image_path.strip() == "":
                self.show_message("Hata", "Lütfen resim seçiniz.")
            else:
                self.chacha20_encrypt_file(self.image_path)
    
    def rsa_encrypt_file(self, file_path):
        if not self.verif:
            self.show_message("Hata", "Önce mailinizi doğrulayınız!")
        else:
            public_key, private_key = rsa.newkeys(2048)
            with open(file_path, 'rb') as f:
                data = f.read()
                encrypted_data = rsa.encrypt(data, public_key)
                kullaniciMail = self.ImageEncForm.lineEdit_EMail.text()
                self.send_email_with_encrypted_data(kullaniciMail, self.ImageEncForm.lineEdit_Name.text(), encrypted_data, private_key, "rsa")
    
    def chacha20_encrypt_file(self, file_path):
        if not self.verif:
            self.show_message("Hata", "Önce mailinizi doğrulayınız!")
        else:
            key = get_random_bytes(32)
            with open(file_path, 'rb') as f:
                data = f.read()
                cipher = ChaCha20.new(key=key)
                ciphertext = cipher.encrypt(data)
                nonce = cipher.nonce
                encrypted_data = nonce + ciphertext
                kullaniciMail = self.ImageEncForm.lineEdit_EMail.text()

                print(f"Original data: {data[:100]}")  # İlk 100 byte'ı yazdır
                print(f"Encrypted data: {encrypted_data[:100]}")  # İlk 100 byte'ı yazdır
               
                self.send_email_with_encrypted_data(kullaniciMail, self.ImageEncForm.lineEdit_Name.text(), encrypted_data, key, "chacha20", nonce)
                self.ImageEncForm.textEdit_EText.setText("Gerekli bilgiler gönderilmiştir.")
    
    def upload_image(self):
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getOpenFileName(self, 'Resim Dosyası Seç', '', 'Images (*.png *.xpm *.jpg)', options=options)
        if fileName:
            self.image_path = fileName
            print(self.image_path)
    
    def show_message(self, title, message):
        msg = QMessageBox()
        msg.setWindowTitle(title)
        msg.setText(message)
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()
    
    def send_email_with_encrypted_data(self, recipient_email, subject, encrypted_data, key, algorithm, nonce=None):
        msg = MIMEMultipart()
        msg['From'] = 'forsmtp01@gmail.com'
        msg['To'] = recipient_email
        msg['Subject'] = subject

        msg.attach(MIMEText("Aşağıda şifrenizi ve şifrelenmiş veriyi ek olarak bulabilirsiniz.", 'plain'))

        if algorithm == "rsa":
            key_text = key.save_pkcs1().decode('utf-8')
            key_filename = "rsa_private_key.txt"
        elif algorithm == "chacha20":
            key_text = base64.b64encode(key).decode('utf-8')
            nonce_text = base64.b64encode(nonce).decode('utf-8')
            nonce_filename = "chacha20_nonce.txt"
            self.attach_file(msg, nonce_filename, nonce_text)

        encrypted_data_text = base64.b64encode(encrypted_data).decode('utf-8')
        
        key_filename = f"{algorithm}_key.txt"
        encrypted_data_filename = f"{algorithm}_encrypted_data.txt"

        self.attach_file(msg, key_filename, key_text)
        self.attach_file(msg, encrypted_data_filename, encrypted_data_text)

        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.login('forsmtp01@gmail.com', 'spwl djou aolg bqvx')
        text = msg.as_string()
        server.sendmail('forsmtp01@gmail.com', recipient_email, text)
        server.quit()

    def attach_file(self, msg, filename, content):
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(content) #.encode('utf-8')
        #encoders.encode_base64(part)
        part.add_header('Content-Disposition', f'attachment; filename= {filename}')
        msg.attach(part)
