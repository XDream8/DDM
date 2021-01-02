from PySide2.QtWidgets import (QMainWindow, QApplication, QPushButton, QFileDialog, QLabel, QLineEdit,
                               QMessageBox, QProgressDialog, QMenuBar, QAction, QDialog, QHBoxLayout,
                               QVBoxLayout, QComboBox, QListWidget, QListWidgetItem, QWidget, QFrame,
                               QFormLayout, QMenu, QProgressBar)

from PySide2.QtGui import QFont, QIcon, QCursor
from PySide2.QtCore import QSettings, QSize, Qt, QCoreApplication, QMetaObject, QPropertyAnimation
from PySide2 import QtCore

from database import getData, delData

import sys
from pathlib import Path

import asyncio
import aiohttp

import icons


class DDMWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ConfigSettings()
        self.init_themes_main()

        self.MainMenuItems()

        self.MenuCreate()

        self.WindowSettings()
        self.show()

    def download_Cache(self):
        self.list_widget.clear()
        for i in getData():
            items = QListWidgetItem(i[0], self.list_widget)

    def download_CacheDelete(self):
        try:
            name = self.list_widget.currentItem().text()
            #print(f"Removing {name}")
            for i in getData():
                if name in i:
                    fname = i
                    break
            delData(name, fname[1], fname[2])
            myfile = Path(f"{fname[1]}/{fname[2]}")
            print(myfile)
            if myfile.exists():
                if self.sel_lang == "tr":
                    dosya_silme = QMessageBox.warning(
                        self, "Dosyayı Sil", "Dosyayı diskten silmeli miyiz?\n\nDiskten silmek için evete basın!", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
                elif self.sel_lang == "en":
                    dosya_silme = QMessageBox.warning(
                        self, "Delete File", "Should we delete file from disk?\n\nTo delete file from disk press yes!", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
                if dosya_silme == QMessageBox.Yes:
                    try:
                        myfile.unlink()
                        if self.sel_lang == "tr":
                            dosya_silme = QMessageBox.information(
                                self, "Dosya Silindi", "Dosya Başarıyla Silindi!", QMessageBox.Ok, QMessageBox.Ok)
                        elif self.sel_lang == "en":
                            dosya_silme = QMessageBox.information(
                                self, "File Deleted", "File Succesfuly Deleted!", QMessageBox.Ok, QMessageBox.Ok)
                    except Exception as e:
                        print(e)
                elif dosya_silme == QMessageBox.No:
                    pass
            self.download_Cache()
        except Exception as e:
            print(e)

    def slideLeftMenu(self):
        width = self.left_side_menu.width()

        if width == 50:
            newWidth = 150
        else:
            newWidth = 50

        self.animation = QPropertyAnimation(
            self.left_side_menu, b"minimumWidth")
        self.animation.setDuration(250)
        self.animation.setStartValue(width)
        self.animation.setEndValue(newWidth)
        self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.animation.start()

    def Add_Download(self):
        self.add_download_dialog = QDialog()

        self.add_download_dialog.setWindowTitle("Add_Download")
        # self.setWindowIcon(QIcon("logo.png"))
        self.init_themes_add_dialog()
        self.add_download_dialog.setFixedSize(325, 275)
        self.add_download_dialog.setMinimumSize(325, 240)

        self.isim = QLabel("İndir", self.add_download_dialog)
        self.isim.setFont(QFont("Hack Nerd Font", 15))
        self.isim.setGeometry(124, 13, 125, 34)

        # İlerleme/Progress
        # self.progressBar =

        # URL KUTUSU
        self.urlbox = QLineEdit("", self.add_download_dialog)
        # self.urlbox.setFixedSize(100,4)
        self.urlbox.setGeometry(35, 60, 250, 34)
        self.urlbox.setPlaceholderText("URL Gir")
        self.urlbox.setFont(QFont("Hack Nerd Font", 11))

        # INDIRME KONUMU
        self.downdirectory = QLineEdit(
            str(Path.home()), self.add_download_dialog)
        self.downdirectory.setGeometry(35, 100, 210, 34)
        self.downdirectory.setPlaceholderText("İndirilecek Konum")
        self.downdirectory.setFont(QFont("Hack Nerd Font", 11))

        # Dosya İsmi
        self.enterfilename = QLineEdit("", self.add_download_dialog)
        # self.filename.setFixedSize(100,4)
        self.enterfilename.setGeometry(35, 140, 210, 34)
        self.enterfilename.setPlaceholderText("Dosya İsmi(Opsiyonel)")
        self.enterfilename.setFont(QFont("Hack Nerd Font", 11))

        def connectfilename():
            fnameloop = asyncio.get_event_loop()
            fnameloop.run_until_complete(self.detect_fname())
        self.connectfilename = QPushButton(".", self.add_download_dialog)
        self.connectfilename.setGeometry(249, 140, 36, 34)
        self.connectfilename.setFont(QFont("Hack Nerd Font", 11))
        self.connectfilename.clicked.connect(connectfilename)

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

        # ProgressBar/İlerleme
        self.progressbar = QProgressBar(self.add_download_dialog)
        self.progressbar.setGeometry(35, 180, 250, 34)
        self.progressbar.setValue(0)
        # self.progressbar.hide()

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
        self.downloadbutton.setGeometry(85, 220, 70, 40)
        self.downloadbutton.setFont(QFont("Hack Nerd Font", 11))
        self.downloadbutton.clicked.connect(start_downloading_process)
        # self.downloadbutton.setStyleSheet("background-color: #268bd2;")

        # ÇIKIŞ BUTONU
        self.iptalbutton = QPushButton("İptal", self.add_download_dialog)
        self.iptalbutton.setGeometry(160, 220, 70, 40)
        self.iptalbutton.setFont(QFont("Hack Nerd Font", 11))
        self.iptalbutton.clicked.connect(self.add_download_dialog.close)
        # self.iptalbutton.setStyleSheet("background-color: #ed0b0b;")
        self.reTranslateAddDownload()
        self.add_download_dialog.show()

    # def downloading_file(self):
    #    self.downloading_dialog = QDialog()
    #    self.init_themes_add_dialog()
    #    self.downloading_dialog.setFixedSize(240, 240)
    #    #self.downloading_dialog.setMinimumSize(325, 240)

        # self.downloading_dialog.exec()
    def reTranslateAddDownload(self):
        if self.sel_lang == "en":
            self.isim.setText("Download")
            self.isim.setGeometry(110, 13, 125, 34)

            self.downloadbutton.setText("Download")
            self.downloadbutton.setGeometry(65, 220, 90, 40)

            self.iptalbutton.setText("Cancel")

            self.enterfilename.setPlaceholderText("File Name(Optional)")
            self.downdirectory.setPlaceholderText("Enter Directory")
            self.urlbox.setPlaceholderText("Enter the URL")

    def eventFilter(self, source, event):
        try:
            if (event.type() == QtCore.QEvent.ContextMenu and
                    source is self.list_widget):
                try:
                    self.menu = QMenu()
                    self.menu.addAction('In Future')
                    if self.menu.exec_(event.globalPos()):
                        item = source.itemAt(event.pos())
                        print(item.text())
                    return True
                except Exception as e:
                    print(e)
            return super().eventFilter(source, event)
        except Exception as e:
            print(e)

    from mainUI import MainMenuItems
    from mainUI import reTranslateMain

    from download_script import detect_fname
    from download_script import detect_fsize
    from download_script import check_connection
    from download_script import download

    # MenuBar things
    from MenuBar import exitAction
    from MenuBar import MenuCreate

    from MenuBar import about
    from MenuBar import reTranslateAbout

    from MenuBar import SettingsMenu
    from MenuBar import SetSettings
    from MenuBar import restartforsettings
    from MenuBar import reTranslateSettings

    # Theming Things
    from theming import init_themes_main
    from theming import init_themes_add_dialog
    from theming import init_themes_settings_dialog
    from theming import init_themes_about_dialog

    def WindowSettings(self):
        self.setWindowTitle("Dream Download Manager")
        # self.setWindowIcon(QIcon("logo.png"))

        #self.setFixedSize(485, 375)
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
    # sys.exit(app.exec())
    app.exec_()


main()
