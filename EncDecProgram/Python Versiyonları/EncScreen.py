from PyQt5.QtWidgets import *
from Encryption import Ui_Form
from DogrulamaEkraniAna import DogruPage
import Resimler_rc
import random
import sys
sys.path.append(r"C:\Users\msı\AppData\Local\Programs\Python\Python312\Lib\site-packages")
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from cryptography.fernet import Fernet
from email.mime.text import MIMEText
import smtplib
import base64
import string

class EncPage(QWidget):
    verif=False
    key=" "
    nonce=" "
    tag=" "
    def __init__(self):
        super().__init__()
        self.EncForm= Ui_Form()
        self.EncForm.setupUi(self)
        self.DogruAc = DogruPage()
        self.EncForm.pushButton_SendC.clicked.connect(self.AcDogru)
        self.EncForm.pushButton_Encrypt.clicked.connect(self.EncClicked)
      
    def EncClicked(self):
        KullaniciGirdi=self.EncForm.textEdit_NText.toPlainText()
        secilenSifreleme = self.EncForm.comboBox_Encryptions.currentText()
        textBaslik = self.EncForm.lineEdit_Name.text() 
        self.verif=self.DogruAc.verify
        print(self.verif)
        if not (self.verif and KullaniciGirdi.replace(" ", "") == ""):
            aliciMail = self.EncForm.lineEdit_EMail.text()
            if not(secilenSifreleme.replace(" ", "") == ""):
                if not(textBaslik.replace(" ", "")== ""):
                    if(secilenSifreleme.strip() == "AES"):
                        key1="J7LyJ9OPqX"
                        sifrelenmis_metin , self.tag = self.AESEnc(KullaniciGirdi)
                        self.EncForm.textEdit_EText.setText(str(sifrelenmis_metin))
                    elif(secilenSifreleme.strip() == "Fernet"):
                        key1="SEQyJ1FeYz"
                        sifrelenmis_metin = base64.urlsafe_b64encode(self.FernetEnc(KullaniciGirdi)).decode()
                        self.EncForm.textEdit_EText.setText(str(sifrelenmis_metin))
                    elif(secilenSifreleme.strip() == "Sezar"):
                        key1 = "qZTs8JH1QB"
                        oteleme = random.randint(1, 10)
                        karakterler = string.ascii_letters + string.digits

                        # Rastgele karakter dizisini oluştur
                        uzunluk = 10  # İfade uzunluğu
                        rastgele_ifade = ''.join(random.choice(karakterler) for _ in range(uzunluk))

                        print("Rastgele ifade:", rastgele_ifade)
                        self.key=rastgele_ifade+"-"+str(oteleme)
                        sifrelenmis_metin= self.SezarEnc(KullaniciGirdi,oteleme)
                    
                    self.keyGonder(aliciMail, self.key, key1, self.nonce, self.tag, textBaslik, sifrelenmis_metin)
                    
    
    def AcDogru(self):
        aliciMail= self.EncForm.lineEdit_EMail.text()
        self.DogruAc.sendEmail(aliciMail)
        if self.DogruAc.dogrulama == True:
            self.DogruAc.show()
   
    def keyGonder(self, aliciMail, key, key1, nonce, tag, textName, EncryptedText):
        print(aliciMail)
        try:
            sender_email = 'forsmtp01@gmail.com'
            sender_password = 'spwl djou aolg bqvx'
           
            msg = MIMEText(f'Bu sizin oluşturduğunuz {textName} adlı metin için geçerli olan 1.anahtardır:{key1}  Bunu key1 yazan yere yazmanız gerekmektedir. Ana anahtarınız:{key} (Bu anahtarı key1 check edildikten sonra key yazan yere yazmanız gerekmektedir) \n\n(Tag={tag}\n\nNonce={nonce}\n\nBu değerler boşsa dikkate almayınız eğer doluysa istendiğinde yazılması gerekmektedir.) \n\n Burasıda şifrelenmiş metininizdir:\n\n {EncryptedText} ')
            msg['Subject'] = 'Oluşturulan Anahtarınız'
            msg['From'] = sender_email
            msg['To'] = aliciMail
           
            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
                server.login(sender_email, sender_password)
                server.sendmail(sender_email, aliciMail, msg.as_string())
        except Exception as e:
            self.DogruAc.show_message("Hata", "Bir hata ile karşılaştık lütfen internet bağlantınızı ve emailinizi kontrol ediniz.")
    
    
    def AESEnc(self, text):
        text = text.encode("utf8")
        self.key = get_random_bytes(16)
        print(self.key)
        
        cipher = AES.new(self.key, AES.MODE_EAX)
        self.key = base64.b64encode(self.key).decode('utf-8')
        self.nonce = cipher.nonce
        self.nonce = base64.b64encode(self.nonce).decode('utf-8')
        ciphertext, tag = cipher.encrypt_and_digest(text)
        return base64.b64encode(ciphertext).decode('utf-8'), base64.b64encode(tag).decode('utf-8')
        
    def FernetEnc(self, text):
        text = text.encode("utf8")
        self.key = Fernet.generate_key()
        cipher_suite = Fernet(self.key)
        cipher_text = cipher_suite.encrypt(text)
        self.key = base64.urlsafe_b64encode(self.key).decode() 
        return cipher_text
    
    def SezarEnc(self, text, otelemeS):
        sifre=""
        for i in text:
            sifre = sifre + chr(ord(i)+otelemeS) 
        return sifre