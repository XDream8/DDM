from PyQt5.QtWidgets import QPushButton, QFileDialog, QLabel, QLineEdit, QMessageBox

from PyQt5.QtCore import QSettings

import requests
from requests.exceptions import RequestException

import os

#from configuration import sel_lang
from PyQt5.QtCore import QSettings

def detect_fname(self):

    self.settings = QSettings("DDM", "DreamDownloadManager")
    sel_lang = self.settings.value('selected_lang')

    url = str(self.urlbox.text())
    filename = str(self.enterfilename.text())
    if filename:
        if self.dirselectdialog == "":
            pass
        else:
            self.filename = filename
    else:
        try:
            with requests.get(url) as r:
                if "Content-Disposition" in r.headers.keys():
                    self.filename = r.headers.get(
                        "Content-Disposition").split("filename=")[1]
                else:
                    self.filename = url.split("/")[-1]
                print(filename)
                self.enterfilename.setText(self.filename)
        except RequestException as reqerr:
            print(reqerr)
            if sel_lang == "tr":
                hata = QMessageBox.warning(self.add_download_dialog, "İndirme Başarısız", str(
                    reqerr), QMessageBox.Ok, QMessageBox.Ok)
            elif sel_lang == "en":
                hata = QMessageBox.warning(self.add_download_dialog, "Download Failed", str(
                    reqerr), QMessageBox.Ok, QMessageBox.Ok)
                hata.close()


def detect_fsize(self):
    self.filesize = ""
    self.settings = QSettings("DDM", "DreamDownloadManager")
    sel_lang = self.settings.value('selected_lang')

    url = str(self.urlbox.text())
    with requests.get(url) as r:
        if "Content-Length" in r.headers.keys():
            filesize_kb = float(r.headers["Content-Length"])
            self.filesize = round((filesize_kb / 1024 / 1024), 2)
        else:
            if sel_lang == "tr":
                self.filesize = "Bilinmeyen Boyut"
            elif sel_lang == "en":
                self.filesize = "Unknown Size"
    print(self.filesize)

    # return self.filesize


def check_connection(self):
    url = str(self.urlbox.text())
    try:
        r = requests.head(url, timeout=3)
        return True
    except requests.ConnectionError as ex:
        print(ex)
        return False


def download(self):
    url = str(self.urlbox.text())
    fdowndir = self.downdirectory.text()

    def download_file(url):
        try:
            fdownname = fdowndir + "/" + self.filename
            with requests.get(url, allow_redirects=True, stream=True) as req:
                with open(fdownname, 'wb') as f:
                    for chunk in req.iter_content(chunk_size=1024 * 16):
                        if chunk:
                            f.write(chunk)
                            f.flush()
                            os.fsync(f.fileno())

                basarili = QMessageBox.information(
                    self.add_download_dialog, "İndirme Başarılı", "İndirme başarılı bir şekilde tamamlandı!", QMessageBox.Close, QMessageBox.Close)
                self.add_download_dialog.close()
        except Exception as e:
            print(e)
            return None

    # Start Download Thread
    try:
        self.check_connection()
        if self.check_connection == False:
            connection_err = QMessageBox.warning(
                self.add_download_dialog, "İndirme Başarısız", "Bağlantınızı Kontrol Ediniz!", QMessageBox.Ok, QMessageBox.Ok)
            connection_err.close()
        else:
            if self.enterfilename.text() == "":
                self.detect_fname()
            self.detect_fsize()
            if self.sel_lang == "tr":
                download_info = QMessageBox.question(self.add_download_dialog, "İndirmeyi Başlat",
                                                     f"Dosya İsmi={self.filename}\nBoyut={self.filesize} MB\n\nİndirilecek Konum={fdowndir}\n\nİndirmeyi başlatmak için evete bas")  # .format(self.filename, self.filesize, fdowndir))
            elif self.sel_lang == "en":
                download_info = QMessageBox.question(self.add_download_dialog, "Start Download",
                                                     f"Filename={self.filename}\nFilesize={self.filesize}\nDownload Dir={fdowndir}\n\nTo start download press Yes")  # .format(self.filename, self.filesize, fdowndir))
            if download_info == QMessageBox.Yes:
                download_file(url)
    except Exception as e:
        print(e)
        # excepterr = QMessageBox.warning(
        #    self, "Hata", str(e), QMessageBox.Ok, QMessageBox.Ok)
        # excepterr.close()
