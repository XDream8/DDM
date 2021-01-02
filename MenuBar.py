from PySide2.QtGui import QFont, QIcon, QColor
from PySide2.QtWidgets import QPushButton, QLabel, QLineEdit, QMessageBox, QMenuBar, QAction, QDialog, QComboBox

# from configuration import *
from PySide2.QtCore import QSettings, Qt

from theming import init_themes_settings_dialog
from theming import init_themes_about_dialog

import sys
import os

import icons

def SetSettings(self):

    self.settings = QSettings("DDM", "DreamDownloadManager")
    self.selected_theme = self.settings.value('theme_selection')

    # self.settings.setValue('theme_selection', 'Dark')
    if self.combobox.currentText() == "Light":
        self.settings.setValue('theme_selection', 'Light')
    elif self.combobox.currentText() == "Dark":
        self.settings.setValue('theme_selection', 'Dark')
    elif self.combobox.currentText() == "Breeze Light":
        self.settings.setValue('theme_selection', 'Breeze Light')
    elif self.combobox.currentText() == "Breeze Dark":
        self.settings.setValue('theme_selection', 'Breeze Dark')

    if self.lang_combobox.currentText() == "tr":
        self.settings.setValue('selected_lang', 'tr')
    elif self.lang_combobox.currentText() == "en":
        self.settings.setValue('selected_lang', 'en')


def restartforsettings(self):
    if self.sel_lang == "tr":
        restart = QMessageBox.warning(self.settingsdialog, "Yeniden Başlatma Gerekli",
                                      "Dili yüklemek için yeniden başlatmak gerekli.Uygulamayı yeniden başlatacağız.", QMessageBox.Ok, QMessageBox.Ok)
    elif self.sel_lang == "en":
        restart = QMessageBox.warning(self.settingsdialog, "Restart Required",
                                      "To load the language we will restart the app.", QMessageBox.Ok, QMessageBox.Ok)
    os.execl(sys.executable, sys.executable, *sys.argv)


def SettingsMenu(self):

    self.settingsdialog = QDialog()
    self.settingsdialog.setWindowTitle("Ayarlar")
    self.settingsdialog.setFixedSize(240, 220)

    self.init_themes_settings_dialog()

    self.combobox = QComboBox(self.settingsdialog)
    self.combobox.setGeometry(65, 60, 100, 34)
    # Items
    if self.selected_theme == "Light":
        self.combobox.addItems(
            ["Light", "Dark", "Breeze Dark", "Breeze Light"])
    elif self.selected_theme == "Dark":
        self.combobox.addItems(
            ["Dark", "Light", "Breeze Dark", "Breeze Light"])
    elif self.selected_theme == "Breeze Light":
        self.combobox.addItems(
            ["Breeze Light", "Breeze Dark", "Dark", "Light"])
    elif self.selected_theme == "Breeze Dark":
        self.combobox.addItems(
            ["Breeze Dark", "Breeze Light", "Dark", "Light"])

    self.lang_combobox = QComboBox(self.settingsdialog)
    self.lang_combobox.setGeometry(65, 100, 100, 34)

    if self.sel_lang == "en":
        self.lang_combobox.addItems(["en", "tr"])
    elif self.sel_lang == "tr":
        self.lang_combobox.addItems(["tr", "en"])

    def finished():
        self.settingsdialog.close()
        # self.ThemeSelector()
        # self.LanguageSelector()
        if self.selected_theme == self.combobox.currentText() and self.sel_lang == self.lang_combobox.currentText():
            pass
        else:
            # self.LanguageSelector()
            # time.sleep(1)
            self.SetSettings()
            self.restartforsettings()
            # self.restartforsettingslangs()
        # if sel_lang == self.lang_combobox.currentText():
        #    pass
        # else:
        #    self.LanguageSelector()
        #    self.restartforsettingslangs()

    self.okbutton = QPushButton("Tamam", self.settingsdialog)

    self.okbutton.setGeometry(85, 170, 70, 40)
    self.okbutton.setFont(QFont("Hack Nerd Font", 11))
    self.okbutton.clicked.connect(finished)

    self.reTranslateSettings()

    self.settingsdialog.exec()


def about(self):

    self.about_dialog = QDialog()
    self.about_dialog.setFixedSize(225, 225)
    self.about_dialog.setWindowTitle("Hakkımızda")

    self.init_themes_about_dialog()

    programname = QLabel("Dream Download Manager", self.about_dialog)
    programname.setFont(QFont("JetBrains Mono Bold", 14))
    programname.setGeometry(2, 10, 220, 20)
    self.owner = QLabel(
        "    Yapımcı: XDream8\nDDM Sürümü: v0.740Beta", self.about_dialog)
    self.owner.setGeometry(10, 80, 220, 40)
    self.owner.setFont(QFont("JetBrains Mono Font", 12))

    self.reTranslateAbout()

    self.about_dialog.exec()


def exitAction(self):
    if self.sel_lang == "tr":
        cikisonay = QMessageBox.question(
            self, "Çıkış Onay", "Çıkış Yapmak İstiyor musun?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
    elif self.sel_lang == "en":
        cikisonay = QMessageBox.question(
            self, "Exit", "Do you really wanna exit?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
    if cikisonay == QMessageBox.Yes:
        self.close()
    else:
        pass


def MenuCreate(self):
    mainMenu = self.menuBar()
    if self.sel_lang == "tr":
        fileMenu = mainMenu.addMenu("Dosya")
        helpMenu = mainMenu.addMenu("Yardım")
    elif self.sel_lang == "en":
        fileMenu = mainMenu.addMenu("File")
        helpMenu = mainMenu.addMenu("Help")

    add_download = QAction(QIcon(":/icons/add.png"), "Ekle", self)
    add_download.triggered.connect(self.Add_Download)
    fileMenu.addAction(add_download)

    settings = QAction(QIcon(":/icons/settings.png"), "Ayarlar", self)
    settings.triggered.connect(self.SettingsMenu)
    fileMenu.addAction(settings)

    exit = QAction(QIcon(":/icons/exit.png"), "Çıkış", self)
    exit.triggered.connect(self.exitAction)
    fileMenu.addAction(exit)

    about = QAction(QIcon(":/icons/about.png"), "Hakkımızda", self)
    about.triggered.connect(self.about)
    helpMenu.addAction(about)

    if self.sel_lang == "en":
        add_download.setText("Add")
        settings.setText("Settings")
        exit.setText("Exit")

        about.setText("About")


def reTranslateAbout(self):
    if self.sel_lang == "en":
        self.owner.setText("    Owner: XDream8\nDDM Version v0.740Beta")

        self.about_dialog.setWindowTitle("About")


def reTranslateSettings(self):
    if self.sel_lang == "en":
        self.okbutton.setText("Ok")
        self.settingsdialog.setWindowTitle("Settings")
