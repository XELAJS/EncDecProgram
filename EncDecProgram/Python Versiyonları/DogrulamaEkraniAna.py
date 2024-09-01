from PyQt5.QtWidgets import *
from DogrulamaEkrani import Ui_Form
import smtplib
from email.mime.text import MIMEText
import random

class DogruPage(QWidget):
    verify = False
    verificationCode = 0
    dogrulama = False
    mailAlici=" "
    def __init__(self):
        super().__init__()
        self.DogruForm = Ui_Form()
        self.DogruForm.setupUi(self)
        self.DogruForm.pushButton_Verify.clicked.connect(self.deneme)
        self.DogruForm.pushButton_SendAgain.clicked.connect(self.sendAgain)
        
        
    def deneme(self):
        self.userInput = self.DogruForm.lineEdit_VCode.text()
        print(self.userInput)
        if self.userInput == str(self.verificationCode):
            self.verify = True
            self.show_message("Başarılı", "Doğrulama başarılı.")
            self.close()
        else:
            self.verify = False
            self.show_message("Başarısız", "Doğrulama başarısız.")
        
    def sendAgain(self):
        if self.mailAlici.strip():  # mailAlici'nın boş olup olmadığını kontrol et
            self.sendEmail(self.mailAlici)
        else:
            print("E mail boş")

    def sendEmail(self, aliciMail):
        self.mailAlici = aliciMail
        self.verificationCode= random.randint(100000, 999999) 
        print(self.verificationCode)
        try:
            sender_email = 'forsmtp01@gmail.com'
            sender_password = 'spwl djou aolg bqvx'
           
            msg = MIMEText(f'Your verification code is {self.verificationCode}')
            msg['Subject'] = 'Verification Code'
            msg['From'] = sender_email
            msg['To'] = aliciMail
           
            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
                server.login(sender_email, sender_password)
                server.sendmail(sender_email, aliciMail, msg.as_string())
            self.dogrulama = True
        except Exception as e:
            self.show_message("Hata", "Bir hata ile karşılaştık lütfen internet bağlantınızı ve emailinizi kontrol ediniz.")
    
    def show_message(self, title, message):
        msg = QMessageBox()
        msg.setWindowTitle(title)
        msg.setText(message)
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()

