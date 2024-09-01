from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMessageBox
from ImageDecrypt import Ui_Form
import sys
import base64
from Crypto.Cipher import ChaCha20
from io import BytesIO
from PIL import Image

class ImgDecScreen(QWidget):
    def __init__(self):
        super().__init__()
        self.ImageDecForm = Ui_Form()
        self.ImageDecForm.setupUi(self)
        self.ImageDecForm.pushButton_Decrypt.clicked.connect(self.decrypt_image_chacha20)
        
        # Decrypted image gösterim alanı
        self.decryptedImage = QLabel(self)
        self.decryptedImage.setGeometry(20, 220, 600, 400)
        self.decryptedImage.setScaledContents(True)
        self.decryptedImage.hide()  # Başlangıçta gizli tut

    def decrypt_image_chacha20(self):
        try:
            # Kullanıcıdan alınan verileri al
            encrypted_data_base64 = self.ImageDecForm.textEdit_EncryptedT.toPlainText().replace(" ", "")
            key_base64 = self.ImageDecForm.lineEdit_KeyN.text().replace(" ", "")
            nonce_base64 = self.ImageDecForm.lineEdit_KeyN_2.text()
            
            # Verileri base64 çöz
            encrypted_data = base64.b64decode(encrypted_data_base64)
            key = base64.b64decode(key_base64)
            nonce = base64.b64decode(nonce_base64)

            # Şifrelenmiş veriyi ve anahtarları yazdır
            print("Encrypted data (base64):", encrypted_data_base64)
            print("Key (base64):", key_base64)
            print("Nonce (base64):", nonce_base64)
            
            # ChaCha20 ile şifre çözme işlemi
            cipher = ChaCha20.new(key=key, nonce=nonce)
            decrypted_data = cipher.decrypt(encrypted_data)
            
            # Şifre çözülen veriyi kontrol et
            print("Decrypted data:", decrypted_data[:100])  # İlk 100 byte'ı yazdır
            if not decrypted_data:
                self.show_message("Hata", "Şifre çözme işlemi başarısız.")
                return
            
            # Şifre çözülen veriyi bellekte işlemeyi dene
            # try:
            #     image = Image.open(BytesIO(decrypted_data))
            #     image = image.convert("RGBA")  # Görüntüyü RGBA formatına dönüştürme
            #     byte_data = BytesIO()
            #     image.save(byte_data, format='PNG')
            #     byte_data.seek(0)
            #     qpixmap = QPixmap()
            #     qpixmap.loadFromData(byte_data.read())
                
            #     # QPixmap nesnesini QLabel'de gösterme
            #     self.decryptedImage.setPixmap(qpixmap)
            #     self.decryptedImage.show()  # Şifre çözülmüş görüntüyü göster
            # except Exception as e:
            #     self.show_message("Hata", f"Görsel işleme hatası: {e}")
            #     return

            # Dosya kaydetme
            save_path, _ = QFileDialog.getSaveFileName(self, 'Çözülen Dosyayı Kaydet', '', 'Images ( *.jpg)')
            if save_path:
                with open(save_path, 'wb') as f:
                    f.write(decrypted_data)
                self.show_message("Başarılı", "Şifre çözme işlemi tamamlandı ve dosya kaydedildi.")
            else:
                self.show_message("Hata", "Dosya kaydedilemedi.")
        except Exception as e:
            self.show_message("Hata", f"Şifre çözme işlemi sırasında bir hata oluştu: {e}")
    
    def show_message(self, title, message):
        msg = QMessageBox()
        msg.setWindowTitle(title)
        msg.setText(message)
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ImgDecScreen()
    ex.show()
    sys.exit(app.exec_())
