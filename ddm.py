#from PyQt5.QtCore import *
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QFileDialog, QLabel, QLineEdit, QMessageBox, QInputDialog

import requests
from requests.exceptions import RequestException
import re
import sys


class DDMWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.MainUI()
    
    def MainUI(self):
        
        self.MainMenuItems()
        
        self.WindowSettings()
        self.show()

    def MainMenuItems(self):
        self.isim = QLabel("    DDM\nby XDream8",self)
        self.isim.setFont(QFont("Hack Nerd Font",12))
        self.isim.setGeometry(105,6,125,34)


        ## URL KUTUSU
        self.urlbox = QLineEdit("", self)
        #self.urlbox.setFixedSize(100,4)
        self.urlbox.setGeometry(35,60,250,34)
        self.urlbox.setPlaceholderText("İndirmenin Yapılacağı URL")
        self.urlbox.setFont(QFont("Hack Nerd Font",12))

        ## INDIR BUTONU
        self.downloadbutton = QPushButton("İndir", self)
        self.downloadbutton.setGeometry(115,110,70,40)
        self.downloadbutton.setFont(QFont("Hack Nerd Font",12))
        self.downloadbutton.clicked.connect(self.download)
       
    def download(self):
        url = str(self.urlbox.text())


        def download_file(url):
            try:
                fnameinput = QInputDialog.getText(self, "İndirilecek Dosyanın Adını Gir", "İndirilecek dosyaya kendiniz isim vermek istiyorsanız isim giriniz.(Dosya Uzantısı Dahil)")
                filename = str(fnameinput[0])
                
                filedialog = QFileDialog.getExistingDirectory(self, 'İndirilecek Konumu Seç')
                if filename:
                    if filedialog == "":
                        pass
                    else:
                        filename = filedialog + "/" + filename
                else:
                    try:
                        with requests.get(url) as r:
                            if filedialog == "":
                                if "Content-Disposition" in r.headers.keys():
                                    filename = re.findall("filename=(.+)", r.headers["Content-Disposition"])[0]
                                else:
                                    filename = url.split("/")[-1]
                                print(filename)
                            else:
                                if "Content-Disposition" in r.headers.keys():
                                    filename = filedialog + "/" + re.findall("filename=(.+)", r.headers["Content-Disposition"])[0]
                                else:
                                    filename = filedialog + "/" + url.split("/")[-1]
                                print(filename)
                    except RequestException as reqe:
                        print(reqe)
                        hata = QMessageBox.warning(self, "İndirme Başarısız", str(reqe))
                        hata.close()

                with requests.get(url) as req:
                    with open(filename, 'wb') as f:
                        for chunk in req.iter_content(chunk_size=8192):
                            if chunk:
                                f.write(chunk)
                                
                    basari = QMessageBox.information(self, "İndirme Başarılı", "İndirme başarılı bir şekilde tamamlandı!")
                    basari.close()
                    return filename
            except Exception as e:
                print(e)
                return None

        
        download_file(url)
        
    def WindowSettings(self):
        self.setWindowTitle("Dream Download Manager")
        #self.setWindowIcon(QIcon("logo.png"))
        self.setFixedSize(325,220)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = DDMWindow()
    sys.exit(app.exec())
    