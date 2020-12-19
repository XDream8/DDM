from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QFileDialog, QLabel, QLineEdit, QMessageBox, QProgressDialog, QMenuBar, QAction, QDialog, QHBoxLayout, QVBoxLayout, QComboBox
from PyQt5.QtCore import QSettings

#import requests
#from requests.exceptions import RequestException

import sys
from pathlib import Path


class DDMWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ConfigSettings()
        self.init_themes_main()

        self.MainMenuItems()

        self.MenuCreate()

        self.WindowSettings()
        self.show()

    def MainMenuItems(self):

        self.isim = QLabel("    DDM\nby XDream8", self)
        self.isim.setFont(QFont("Hack Nerd Font", 12))
        self.isim.setGeometry(170, 20, 125, 34)

        self.info = QLabel(
            " Burası geliştirilecektir.Şuanki durumda\nişlemleri Dosya Menüsünden Yapabilirsiniz.", self)
        self.info.setGeometry(40, 120, 410, 34)
        if self.sel_lang == "en":
            self.info.setText(
                "Here Will Be Updated.In this state\n you can do things from File Menu.")
            self.info.setGeometry(80, 120, 330, 34)
        self.info.setFont(QFont("Hack Nerd Font", 12))

    def Add_Download(self):
        self.add_download_dialog = QDialog()

        self.add_download_dialog.setWindowTitle("Add_Download")
        # self.setWindowIcon(QIcon("logo.png"))
        self.init_themes_add_dialog()
        self.add_download_dialog.setFixedSize(325, 240)
        self.add_download_dialog.setMinimumSize(325, 240)

        isim = QLabel("İndir", self.add_download_dialog)
        isim.setFont(QFont("Hack Nerd Font", 15))
        isim.setGeometry(124, 13, 125, 34)
        if self.sel_lang == "en":
            isim.setText("Download")
            isim.setGeometry(110, 13, 125, 34)

        # URL KUTUSU
        self.urlbox = QLineEdit("", self.add_download_dialog)
        # self.urlbox.setFixedSize(100,4)
        self.urlbox.setGeometry(35, 60, 250, 34)
        if self.sel_lang == "tr":
            self.urlbox.setPlaceholderText("URL Gir")
        elif self.sel_lang == "en":
            self.urlbox.setPlaceholderText("Enter the URL")
        self.urlbox.setFont(QFont("Hack Nerd Font", 11))

        # INDIRME KONUMU
        self.downdirectory = QLineEdit(
            str(Path.home()), self.add_download_dialog)
        self.downdirectory.setGeometry(35, 100, 210, 34)
        if self.sel_lang == "tr":
            self.downdirectory.setPlaceholderText("İndirilecek Konum")
        elif self.sel_lang == "en":
            self.downdirectory.setPlaceholderText("Enter Directory")
        self.downdirectory.setFont(QFont("Hack Nerd Font", 11))

        # Dosya İsmi
        self.enterfilename = QLineEdit("", self.add_download_dialog)
        # self.filename.setFixedSize(100,4)
        self.enterfilename.setGeometry(35, 140, 210, 34)
        if self.sel_lang == "tr":
            self.enterfilename.setPlaceholderText("Dosya İsmi(Opsiyonel)")
        elif self.sel_lang == "en":
            self.enterfilename.setPlaceholderText("File Name(Optional)")
        self.enterfilename.setFont(QFont("Hack Nerd Font", 11))

        self.connectfilename = QPushButton(".", self.add_download_dialog)
        self.connectfilename.setGeometry(249, 140, 36, 34)
        self.connectfilename.setFont(QFont("Hack Nerd Font", 11))
        self.connectfilename.clicked.connect(self.detect_fname)

        # KONUM SEÇ BUTONU
        def download_dir():
            if self.sel_lang == "tr":
                try:
                    self.dirselectdialog = QFileDialog.getExistingDirectory(
                        self.add_download_dialog, 'İndirilecek Konumu Seç')
                except Exception as e:
                    print(e)
            elif self.sel_lang == "en":
                try:
                    self.dirselectdialog = QFileDialog.getExistingDirectory(
                        self.add_download_dialog, 'Select Dir')
                except Exception as e:
                    print(e)
            if self.dirselectdialog == "":
                self.downdirectory.setText(str(Path.home()))
            else:
                self.downdirectory.setText(str(self.dirselectdialog))

        self.selectdirbutton = QPushButton("...", self.add_download_dialog)
        self.selectdirbutton.setGeometry(249, 100, 36, 34)
        self.selectdirbutton.setFont(QFont("Hack Nerd Font", 11))
        self.selectdirbutton.clicked.connect(download_dir)

        # INDIR BUTONU
        def start_downloading_process():
            url = str(self.urlbox.text())
            if url == "":
                if self.sel_lang == "tr":
                    self.urlboxempty = QMessageBox.warning(
                        self.add_download_dialog, "URL Kutusu Boş", "Lütfen bir url giriniz!", QMessageBox.Ok, QMessageBox.Ok)
                elif self.sel_lang == "en":
                    self.urlboxempty = QMessageBox.warning(
                        self.add_download_dialog, "URL Box Empty", "Please enter a URL!", QMessageBox.Ok, QMessageBox.Ok)
            else:
                # self.add_download_dialog.close()
                # self.downloading_file()
                # self.add_download_dialog.close()
                self.download()

        self.downloadbutton = QPushButton("İndir", self.add_download_dialog)
        self.downloadbutton.setGeometry(85, 190, 70, 40)
        self.downloadbutton.setFont(QFont("Hack Nerd Font", 11))
        self.downloadbutton.clicked.connect(start_downloading_process)
        # self.downloadbutton.setStyleSheet("background-color: #268bd2;")
        if self.sel_lang == "en":
            self.downloadbutton.setText("Download")
            self.downloadbutton.setGeometry(65, 190, 90, 40)

        # ÇIKIŞ BUTONU
        self.iptalbutton = QPushButton("İptal", self.add_download_dialog)
        if self.sel_lang == "en":
            self.iptalbutton.setText("Cancel")
        self.iptalbutton.setGeometry(160, 190, 70, 40)
        self.iptalbutton.setFont(QFont("Hack Nerd Font", 11))
        self.iptalbutton.clicked.connect(self.add_download_dialog.close)
        # self.cikisbutton.setStyleSheet("background-color: #ed0b0b;")

        self.add_download_dialog.exec()

    # def downloading_file(self):
    #    self.downloading_dialog = QDialog()
    #    self.init_themes_add_dialog()
    #    self.downloading_dialog.setFixedSize(240, 240)
    #    #self.downloading_dialog.setMinimumSize(325, 240)

        # self.downloading_dialog.exec()

    from download_script import detect_fname
    from download_script import detect_fsize
    from download_script import check_connection
    from download_script import download

    # MenuBar things
    from MenuBar import exitAction
    from MenuBar import MenuCreate

    from MenuBar import about

    from MenuBar import SettingsMenu
    from MenuBar import SetSettings
    from MenuBar import restartforsettings

    # Theming Things
    from theming import init_themes_main
    from theming import init_themes_add_dialog
    from theming import init_themes_settings_dialog
    from theming import init_themes_about_dialog

    def WindowSettings(self):
        self.setWindowTitle("Dream Download Manager")
        # self.setWindowIcon(QIcon("logo.png"))

        self.setFixedSize(485, 375)
        #self.setMinimumSize(325, 240)

    def ConfigSettings(self):
        self.settings = QSettings("DDM", "DreamDownloadManager")
        print(self.settings.fileName())
        if self.settings.contains('theme_selection'):
            self.selected_theme = self.settings.value('theme_selection')
        else:
            self.settings.setValue('theme_selection', 'Dark')

        if self.settings.contains('selected_lang'):
            self.sel_lang = self.settings.value('selected_lang')
        else:
            self.settings.setValue('selected_lang', 'en')


def main():
    app = QApplication(sys.argv)
    window = DDMWindow()
    app.setStyle("Fusion")
    sys.exit(app.exec())


main()
