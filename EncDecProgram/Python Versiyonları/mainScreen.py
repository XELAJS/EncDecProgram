from PyQt5.QtWidgets import *
from MainSC import Ui_MainScreen
from PyQt5 import QtGui
import Resimler_rc
from DecScreen import DecPage
from EncScreen import EncPage
from IMGencScrn import ImgEncScreen
from IMDecScrn import ImgDecScreen
class MainPage(QWidget):
    def __init__(self):
        super().__init__()
        self.MainForm= Ui_MainScreen()
        self.MainForm.setupUi(self)
        self.DecAc = DecPage()
        self.MainForm.pushButton_EncryptionS.clicked.connect(self.AcEnc)
        self.MainForm.pushButton_2_DecryptionS.clicked.connect(self.AcDec)
        self.MainForm.pushButton_ImageENC.clicked.connect(self.AcIMGenc)
        self.MainForm.pushButton_2_ImageDEC.clicked.connect(self.AcIMGdec)
    def AcEnc(self):
        self.close()
        self.enc_page = EncPage()
        self.enc_page.show()
    def AcDec(self):
        self.close()
        self.DecAc.show()
    def AcIMGenc(self):
        self.close()
        self.IMG_encPage=ImgEncScreen()
        self.IMG_encPage.show()
    def AcIMGdec(self):
        self.close()
        self.IMG_DecPage = ImgDecScreen()
        self.IMG_DecPage.show()