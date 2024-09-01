from PyQt5.QtWidgets import QApplication
from mainScreen import MainPage
from PyQt5 import QtGui
import sys
import Resimler_rc

app= QApplication([])
pencere = MainPage()
pencere.show()
SystemExit(app.exec_())