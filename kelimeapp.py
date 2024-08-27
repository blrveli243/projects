import os
import sys
from PyQt5 import QtWidgets

class KelimeIslemci(QtWidgets.QMainWindow):  # Sınıf ismi Python standartlarına uygun hale getirildi
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        # Widget'lar oluşturuluyor
        self.yazi_alani = QtWidgets.QTextEdit()
        self.ac = QtWidgets.QPushButton("Aç")
        self.kaydet = QtWidgets.QPushButton("Kaydet")
        self.temizle = QtWidgets.QPushButton("Temizle")
        self.cikis = QtWidgets.QPushButton("Çıkış")

        # Düğmeler için yatay düzen (hbox) oluşturuluyor
        hbox = QtWidgets.QHBoxLayout()
        hbox.addWidget(self.ac)
        hbox.addWidget(self.kaydet)
        hbox.addWidget(self.temizle)
        hbox.addWidget(self.cikis)

        # Dikey düzen (vbox) oluşturuluyor ve yazı alanı ile hbox ekleniyor
        vbox = QtWidgets.QVBoxLayout()
        vbox.addWidget(self.yazi_alani)
        vbox.addLayout(hbox)

        # QMainWindow'a centralWidget olarak bir QWidget atanıyor
        central_widget = QtWidgets.QWidget()
        central_widget.setLayout(vbox)
        self.setCentralWidget(central_widget)

        self.setWindowTitle("Kelime İşlemci")

        self.ac.clicked.connect(self.dosya_ac)
        self.kaydet.clicked.connect(self.dosya_kaydet)
        self.temizle.clicked.connect((self.yazi_sil))
        self.cikis.clicked.connect(self.cikis_yap)

        self.show()

    def dosya_ac(self):
        dosya = QtWidgets.QFileDialog.getOpenFileName(self,"Dosya Aç",os.getenv("Desktop"))
        with open(dosya[0], "r") as file:
            self.yazi_alani.setText(file.read())

    def dosya_kaydet(self):
        dosya = QtWidgets.QFileDialog.getSaveFileName(self,"Dosya Kaydet",os.getenv("Desktop"))
        with open(dosya[0], "w") as file:
            file.write(str(self.yazi_alani.toPlainText()))

    def yazi_sil(self):
        self.yazi_alani.clear()

    def cikis_yap(self):
        quit()

# Uygulama başlatılıyor

uygulama = QtWidgets.QApplication(sys.argv)
kelime = KelimeIslemci()
sys.exit(uygulama.exec_())
