from PySide2.QtWidgets import (QMainWindow, QApplication, QPushButton, QFileDialog, QLabel, QLineEdit,
                             QMessageBox, QProgressDialog, QMenuBar, QAction, QDialog, QHBoxLayout,
                             QVBoxLayout, QComboBox, QListWidget, QListWidgetItem, QWidget, QFrame,
                             QFormLayout)

from PySide2.QtGui import QFont, QIcon, QCursor
from PySide2.QtCore import QSettings, QSize, Qt, QCoreApplication, QMetaObject, QPropertyAnimation

import concurrent.futures

import icons

def MainMenuItems(self):
    self.centralwidget = QWidget(self)
    self.centralwidget.setStyleSheet("background-color: rgb(255, 255, 255);")
    self.verticalLayout = QVBoxLayout(self.centralwidget)
    self.verticalLayout.setSpacing(0)
    self.verticalLayout.setContentsMargins(0, 0, 0, 0)
    self.main_header = QFrame(self.centralwidget)
    self.main_header.setMaximumSize(QSize(16777215, 50))
    self.main_header.setStyleSheet("QFrame{\n"
                                   "   border-bottom: 1px solid #000;\n"
                                   "   \n"
                                   "   background-color: rgb(0, 0, 0);\n"
                                   "}")
    self.main_header.setFrameShape(QFrame.WinPanel)
    self.main_header.setFrameShadow(QFrame.Raised)
    self.horizontalLayout_2 = QHBoxLayout(self.main_header)
    self.horizontalLayout_2.setSpacing(0)
    self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
    self.tittle_bar_container = QFrame(self.main_header)
    self.tittle_bar_container.setFrameShape(QFrame.StyledPanel)
    self.tittle_bar_container.setFrameShadow(QFrame.Raised)
    self.horizontalLayout_5 = QHBoxLayout(self.tittle_bar_container)
    self.horizontalLayout_5.setSpacing(0)
    self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
    self.left_menu_toggle = QFrame(self.tittle_bar_container)
    self.left_menu_toggle.setMinimumSize(QSize(50, 0))
    self.left_menu_toggle.setMaximumSize(QSize(50, 16777215))
    self.left_menu_toggle.setStyleSheet("QFrame{\n"
                                        "   background-color: #000;\n"
                                        "}\n"
                                        "QPushButton{\n"
                                        "   padding: 5px 10px;\n"
                                        "   border: none;\n"
                                        "   border-radius: 5px;\n"
                                        "   background-color: #000;\n"
                                        "   color: #fff;\n"
                                        "}\n"
                                        "QPushButton:hover{\n"
                                        "   background-color: rgb(0, 92, 157);\n"
                                        "}")
    self.left_menu_toggle.setFrameShape(QFrame.StyledPanel)
    self.left_menu_toggle.setFrameShadow(QFrame.Raised)
    self.horizontalLayout_4 = QHBoxLayout(self.left_menu_toggle)
    self.horizontalLayout_4.setSpacing(0)
    self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
    self.left_menu_toggle_btn = QPushButton(self.left_menu_toggle)
    self.left_menu_toggle_btn.setMinimumSize(QSize(0, 50))
    self.left_menu_toggle_btn.setMaximumSize(QSize(50, 16777215))
    self.left_menu_toggle_btn.setCursor(QCursor(Qt.PointingHandCursor))
    icon = QIcon()
    icon.addFile(":/icons/cil-menu.png",
                 QSize(), QIcon.Normal, QIcon.Off)
    self.left_menu_toggle_btn.setIcon(icon)
    self.left_menu_toggle_btn.setIconSize(QSize(24, 24))
    self.left_menu_toggle_btn.clicked.connect(lambda: self.slideLeftMenu())

    self.horizontalLayout_4.addWidget(self.left_menu_toggle_btn)

    self.horizontalLayout_5.addWidget(self.left_menu_toggle)

    self.tittle_bar = QFrame(self.tittle_bar_container)
    self.tittle_bar.setFrameShape(QFrame.StyledPanel)
    self.tittle_bar.setFrameShadow(QFrame.Raised)

    self.horizontalLayout_5.addWidget(self.tittle_bar)

    self.horizontalLayout_2.addWidget(self.tittle_bar_container)

    self.top_right_btns = QFrame(self.main_header)
    self.top_right_btns.setMaximumSize(QSize(100, 16777215))
    self.top_right_btns.setStyleSheet("QPushButton{\n"
                                      "   border-radius: 5px;\n"
                                      "}\n"
                                      "QPushButton:hover{\n"
                                      "   background-color: rgb(0, 92, 157);\n"
                                      "}")
    self.top_right_btns.setFrameShape(QFrame.StyledPanel)
    self.top_right_btns.setFrameShadow(QFrame.Raised)
    self.horizontalLayout_3 = QHBoxLayout(self.top_right_btns)
    self.horizontalLayout_3.setSpacing(0)
    self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)

    self.horizontalLayout_2.addWidget(self.top_right_btns)

    self.verticalLayout.addWidget(self.main_header)

    self.main_body = QFrame(self.centralwidget)
    self.main_body.setFrameShape(QFrame.StyledPanel)
    self.main_body.setFrameShadow(QFrame.Raised)
    self.horizontalLayout = QHBoxLayout(self.main_body)
    self.horizontalLayout.setSpacing(0)
    self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
    self.left_side_menu = QFrame(self.main_body)
    self.left_side_menu.setMaximumSize(QSize(50, 16777215))
    self.left_side_menu.setStyleSheet("QFrame{\n"
                                      "   background-color: #000;\n"
                                      "}\n"
                                      "QPushButton{\n"
                                      "   padding: 20px 10px;\n"
                                      "   border: none;\n"
                                      "   border-radius: 10px;\n"
                                      "   background-color: #000;\n"
                                      "   color: #fff;\n"
                                      "}\n"
                                      "QPushButton:hover{\n"
                                      "   background-color: rgb(0, 92, 157);\n"
                                      "}")
    self.left_side_menu.setFrameShape(QFrame.NoFrame)
    self.left_side_menu.setFrameShadow(QFrame.Raised)
    self.verticalLayout_3 = QVBoxLayout(self.left_side_menu)
    self.verticalLayout_3.setSpacing(0)
    self.verticalLayout_3.setContentsMargins(7, 0, 0, 0)
    self.left_menu_top_buttons = QFrame(self.left_side_menu)
    self.left_menu_top_buttons.setFrameShape(QFrame.StyledPanel)
    self.left_menu_top_buttons.setFrameShadow(QFrame.Raised)
    self.formLayout = QFormLayout(self.left_menu_top_buttons)
    self.formLayout.setHorizontalSpacing(0)
    self.formLayout.setVerticalSpacing(0)
    self.formLayout.setContentsMargins(0, 0, 0, 0)
    self.userButton = QPushButton("Hakkımızda", self.left_menu_top_buttons)
    self.userButton.setMinimumSize(QSize(100, 0))
    self.userButton.setStyleSheet("background-image: url(:/icons/cil-user.png);\n"
                                    "background-repeat: none;\n"
                                    "padding-left: 50px;\n"
                                    "background-position: center left;")
    self.userButton.clicked.connect(self.about)

    self.formLayout.setWidget(
        1, QFormLayout.SpanningRole, self.userButton)

    self.homeButton = QPushButton("ANA", self.left_menu_top_buttons)
    self.homeButton.setMinimumSize(QSize(100, 0))
    self.homeButton.setStyleSheet("background-image: url(:/icons/cil-home.png);\n"
                                    "background-repeat: none;\n"
                                    "padding-left: 50px;\n"
                                    "background-position: center left;")

    self.formLayout.setWidget(
        0, QFormLayout.SpanningRole, self.homeButton)

    self.verticalLayout_3.addWidget(self.left_menu_top_buttons)

    self.settingsButton = QPushButton("Ayarlar", self.left_side_menu)
    self.settingsButton.setMinimumSize(QSize(100, 0))
    self.settingsButton.setStyleSheet("background-image: url(:/icons/cil-settings.png);\n"
                                    "background-repeat: none;\n"
                                    "padding-left: 50px;\n"
                                    "background-position: center left;")
    self.settingsButton.clicked.connect(self.SettingsMenu)

    self.verticalLayout_3.addWidget(self.settingsButton)

    self.horizontalLayout.addWidget(self.left_side_menu)

    self.center_main_items = QFrame(self.main_body)
    self.center_main_items.setStyleSheet("")
    self.center_main_items.setFrameShape(QFrame.StyledPanel)
    self.center_main_items.setFrameShadow(QFrame.Raised)
    self.verticalLayout_2 = QVBoxLayout(self.center_main_items)
    self.list_widget = QListWidget(self.center_main_items)
    self.list_widget.setMinimumSize(QSize(0, 50))
    self.list_widget.setMaximumSize(QSize(16777215, 16777215))
    self.list_widget.setFont(
        QFont("Hack Nerd Font", 12, QFont.Weight(78), QFont.Bold))

    self.list_widget.installEventFilter(self)

    self.download_Cache()

    self.verticalLayout_2.addWidget(self.list_widget)

    self.horizontalLayout.addWidget(self.center_main_items)

    self.right_side_menu = QFrame(self.main_body)
    self.right_side_menu.setMaximumSize(QSize(100, 16777215))
    self.right_side_menu.setStyleSheet("")
    self.right_side_menu.setFrameShape(QFrame.NoFrame)
    self.right_side_menu.setFrameShadow(QFrame.Raised)
    self.right_side_menu.setStyleSheet("QFrame{\n"
                                       "   background-color: rgb(0, 0, 0);\n"
                                       "   border-top-color: solid 1px  rgb(0, 0, 0);\n"
                                       "}")
    self.right_side_Layout = QVBoxLayout(self.right_side_menu)

    self.horizontalLayout.addWidget(self.right_side_menu)

    self.verticalLayout.addWidget(self.main_body)

    self.main_footer = QFrame(self.centralwidget)
    self.main_footer.setMaximumSize(QSize(16777215, 30))
    self.main_footer.setStyleSheet("QFrame{\n"
                                   "   background-color: #000;\n"
                                   "   border-top-color: solid 1px  rgb(0, 0, 0);\n"
                                   "}")
    self.main_footer.setFrameShape(QFrame.WinPanel)
    self.main_footer.setFrameShadow(QFrame.Raised)

    self.verticalLayout.addWidget(self.main_footer)

    self.bottom_menu = QFrame(self.main_footer)
    self.bottom_menu.setMaximumSize(QSize(100, 16777215))
    self.bottom_menu.setFrameShape(QFrame.NoFrame)
    self.bottom_menu.setFrameShadow(QFrame.Raised)
    self.bottom_menu.setStyleSheet("QFrame{\n"
                                      "   background-color: #000;\n"
                                      "}\n"
                                      "QPushButton{\n"
                                      "   padding: 8px 8px;\n"
                                      "   border: none;\n"
                                      "   border-radius: 10px;\n"
                                      "   background-color: #000;\n"
                                      "   color: #fff;\n"
                                      "}\n"
                                      "QPushButton:hover{\n"
                                      "   background-color: rgb(0, 92, 157);\n"
                                      "}")
    self.verticalLayout.addWidget(self.bottom_menu)

    self.footer_horizontalLayout = QHBoxLayout(self.bottom_menu)
    def ThreadDownloadDialog():
      with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
        executor.map(self.Add_Download(), range(1))

    self.add = QPushButton(self.main_footer)
    self.add.setIcon(QIcon(":/icons/cil-add.png"))
    self.add.setGeometry(38, 328, 50, 34)
    self.add.clicked.connect(ThreadDownloadDialog)
    self.add.setStyleSheet("background-repeat: none;\n"
                        "padding-left: 3px;\n"
                        "background-position: center center;")
    self.footer_horizontalLayout.addWidget(self.add)

    self.delete = QPushButton(self.main_footer)
    self.delete.setIcon(QIcon(":/icons/cil-delete.png"))
    self.delete.setGeometry(98, 328, 50, 34)
    self.delete.clicked.connect(self.download_CacheDelete)
    self.delete.setStyleSheet("background-repeat: none;\n"
                        "padding-left: 3px;\n"
                        "background-position: center center;")
    self.footer_horizontalLayout.addWidget(self.delete)

    self.setCentralWidget(self.centralwidget)

    self.reTranslateMain()

    QMetaObject.connectSlotsByName(self)





def reTranslateMain(self):
  if self.sel_lang == "en":
    self.userButton.setText("About US")
    self.settingsButton.setText("Settings")
    self.homeButton.setText("HOME")

