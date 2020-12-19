from PyQt5.QtCore import QFile, QTextStream, QSettings
import breeze_resources

from PyQt5.QtGui import QColor, QPalette


def init_themes_main(self):
    if self.selected_theme == "Light":
        pass
    elif self.selected_theme == "Breeze Light":
        # set stylesheet
        file = QFile(":/light.qss")
        file.open(QFile.ReadOnly | QFile.Text)
        stream = QTextStream(file)
        self.setStyleSheet(stream.readAll())
        # self.add_download_dialog.setStyleSheet(stream.readAll())
    elif self.selected_theme == "Breeze Dark":
        # set stylesheet
        file = QFile(":/dark.qss")
        file.open(QFile.ReadOnly | QFile.Text)
        stream = QTextStream(file)
        self.setStyleSheet(stream.readAll())
        # self.add_download_dialog.setStyleSheet(stream.readAll())

    elif self.selected_theme == "Dark":
        #
        # # Now use a palette to switch to dark colors:
        dark_palette = QPalette()
        dark_palette.setColor(QPalette.Window, QColor(53, 53, 53))
        dark_palette.setColor(QPalette.WindowText, QColor(255, 255, 255))
        dark_palette.setColor(QPalette.Base, QColor(35, 35, 35))
        dark_palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
        dark_palette.setColor(QPalette.ToolTipBase, QColor(25, 25, 25))
        dark_palette.setColor(QPalette.ToolTipText, QColor(255, 255, 255))
        dark_palette.setColor(QPalette.Text, QColor(255, 255, 255))
        dark_palette.setColor(QPalette.Button, QColor(53, 53, 53))
        dark_palette.setColor(QPalette.ButtonText, QColor(255, 255, 255))
        dark_palette.setColor(QPalette.BrightText, QColor(255, 0, 0))
        dark_palette.setColor(QPalette.Link, QColor(42, 130, 218))
        dark_palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
        dark_palette.setColor(QPalette.HighlightedText, QColor(35, 35, 35))
        dark_palette.setColor(
            QPalette.Active, QPalette.Button, QColor(53, 53, 53))
        dark_palette.setColor(
            QPalette.Disabled, QPalette.ButtonText, QColor(47, 79, 79))
        dark_palette.setColor(
            QPalette.Disabled, QPalette.WindowText, QColor(47, 79, 79))
        dark_palette.setColor(
            QPalette.Disabled, QPalette.Text, QColor(47, 79, 79))
        dark_palette.setColor(
            QPalette.Disabled, QPalette.Light, QColor(53, 53, 53))
        self.setPalette(dark_palette)
        # self.add_download_dialog.setPalette(dark_palette)


def init_themes_add_dialog(self):
    if self.selected_theme == "Light":
        pass
    elif self.selected_theme == "Breeze Light":
        # set stylesheet
        file = QFile(":/light.qss")
        file.open(QFile.ReadOnly | QFile.Text)
        stream = QTextStream(file)
        # self.setStyleSheet(stream.readAll())
        self.add_download_dialog.setStyleSheet(stream.readAll())
    elif self.selected_theme == "Breeze Dark":
        # set stylesheet
        file = QFile(":/dark.qss")
        file.open(QFile.ReadOnly | QFile.Text)
        stream = QTextStream(file)
        # self.setStyleSheet(stream.readAll())
        self.add_download_dialog.setStyleSheet(stream.readAll())

    elif self.selected_theme == "Dark":
        #
        # # Now use a palette to switch to dark colors:
        dark_palette = QPalette()
        dark_palette.setColor(QPalette.Window, QColor(53, 53, 53))
        dark_palette.setColor(QPalette.WindowText, QColor(255, 255, 255))
        dark_palette.setColor(QPalette.Base, QColor(35, 35, 35))
        dark_palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
        dark_palette.setColor(QPalette.ToolTipBase, QColor(25, 25, 25))
        dark_palette.setColor(QPalette.ToolTipText, QColor(255, 255, 255))
        dark_palette.setColor(QPalette.Text, QColor(255, 255, 255))
        dark_palette.setColor(QPalette.Button, QColor(53, 53, 53))
        dark_palette.setColor(QPalette.ButtonText, QColor(255, 255, 255))
        dark_palette.setColor(QPalette.BrightText, QColor(255, 0, 0))
        dark_palette.setColor(QPalette.Link, QColor(42, 130, 218))
        dark_palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
        dark_palette.setColor(QPalette.HighlightedText, QColor(35, 35, 35))
        dark_palette.setColor(
            QPalette.Active, QPalette.Button, QColor(53, 53, 53))
        dark_palette.setColor(
            QPalette.Disabled, QPalette.ButtonText, QColor(47, 79, 79))
        dark_palette.setColor(
            QPalette.Disabled, QPalette.WindowText, QColor(47, 79, 79))
        dark_palette.setColor(
            QPalette.Disabled, QPalette.Text, QColor(47, 79, 79))
        dark_palette.setColor(
            QPalette.Disabled, QPalette.Light, QColor(53, 53, 53))
        # self.setPalette(dark_palette)
        self.add_download_dialog.setPalette(dark_palette)


def init_themes_settings_dialog(self):
    if self.selected_theme == "Light":
        pass
    elif self.selected_theme == "Breeze Light":
        # set stylesheet
        file = QFile(":/light.qss")
        file.open(QFile.ReadOnly | QFile.Text)
        stream = QTextStream(file)
        # self.setStyleSheet(stream.readAll())
        self.settingsdialog.setStyleSheet(stream.readAll())
    elif self.selected_theme == "Breeze Dark":
        # set stylesheet
        file = QFile(":/dark.qss")
        file.open(QFile.ReadOnly | QFile.Text)
        stream = QTextStream(file)
        # self.setStyleSheet(stream.readAll())
        self.settingsdialog.setStyleSheet(stream.readAll())

    elif self.selected_theme == "Dark":
        #
        # # Now use a palette to switch to dark colors:
        dark_palette = QPalette()
        dark_palette.setColor(QPalette.Window, QColor(53, 53, 53))
        dark_palette.setColor(QPalette.WindowText, QColor(255, 255, 255))
        dark_palette.setColor(QPalette.Base, QColor(35, 35, 35))
        dark_palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
        dark_palette.setColor(QPalette.ToolTipBase, QColor(25, 25, 25))
        dark_palette.setColor(QPalette.ToolTipText, QColor(255, 255, 255))
        dark_palette.setColor(QPalette.Text, QColor(255, 255, 255))
        dark_palette.setColor(QPalette.Button, QColor(53, 53, 53))
        dark_palette.setColor(QPalette.ButtonText, QColor(255, 255, 255))
        dark_palette.setColor(QPalette.BrightText, QColor(255, 0, 0))
        dark_palette.setColor(QPalette.Link, QColor(42, 130, 218))
        dark_palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
        dark_palette.setColor(QPalette.HighlightedText, QColor(35, 35, 35))
        dark_palette.setColor(
            QPalette.Active, QPalette.Button, QColor(53, 53, 53))
        dark_palette.setColor(
            QPalette.Disabled, QPalette.ButtonText, QColor(47, 79, 79))
        dark_palette.setColor(
            QPalette.Disabled, QPalette.WindowText, QColor(47, 79, 79))
        dark_palette.setColor(
            QPalette.Disabled, QPalette.Text, QColor(47, 79, 79))
        dark_palette.setColor(
            QPalette.Disabled, QPalette.Light, QColor(53, 53, 53))
        # self.setPalette(dark_palette)
        self.settingsdialog.setPalette(dark_palette)


def init_themes_about_dialog(self):
    if self.selected_theme == "Light":
        pass
    elif self.selected_theme == "Breeze Light":
        # set stylesheet
        file = QFile(":/light.qss")
        file.open(QFile.ReadOnly | QFile.Text)
        stream = QTextStream(file)
        # self.setStyleSheet(stream.readAll())
        self.about_dialog.setStyleSheet(stream.readAll())
    elif self.selected_theme == "Breeze Dark":
        # set stylesheet
        file = QFile(":/dark.qss")
        file.open(QFile.ReadOnly | QFile.Text)
        stream = QTextStream(file)
        # self.setStyleSheet(stream.readAll())
        self.about_dialog.setStyleSheet(stream.readAll())

    elif self.selected_theme == "Dark":
        #
        # # Now use a palette to switch to dark colors:
        dark_palette = QPalette()
        dark_palette.setColor(QPalette.Window, QColor(53, 53, 53))
        dark_palette.setColor(QPalette.WindowText, QColor(255, 255, 255))
        dark_palette.setColor(QPalette.Base, QColor(35, 35, 35))
        dark_palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
        dark_palette.setColor(QPalette.ToolTipBase, QColor(25, 25, 25))
        dark_palette.setColor(QPalette.ToolTipText, QColor(255, 255, 255))
        dark_palette.setColor(QPalette.Text, QColor(255, 255, 255))
        dark_palette.setColor(QPalette.Button, QColor(53, 53, 53))
        dark_palette.setColor(QPalette.ButtonText, QColor(255, 255, 255))
        dark_palette.setColor(QPalette.BrightText, QColor(255, 0, 0))
        dark_palette.setColor(QPalette.Link, QColor(42, 130, 218))
        dark_palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
        dark_palette.setColor(QPalette.HighlightedText, QColor(35, 35, 35))
        dark_palette.setColor(
            QPalette.Active, QPalette.Button, QColor(53, 53, 53))
        dark_palette.setColor(
            QPalette.Disabled, QPalette.ButtonText, QColor(47, 79, 79))
        dark_palette.setColor(
            QPalette.Disabled, QPalette.WindowText, QColor(47, 79, 79))
        dark_palette.setColor(
            QPalette.Disabled, QPalette.Text, QColor(47, 79, 79))
        dark_palette.setColor(
            QPalette.Disabled, QPalette.Light, QColor(53, 53, 53))
        # self.setPalette(dark_palette)
        self.about_dialog.setPalette(dark_palette)
