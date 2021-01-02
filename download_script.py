from PySide2.QtWidgets import QPushButton, QFileDialog, QLabel, QLineEdit, QMessageBox

from PySide2.QtCore import QSettings, Qt

import asyncio
import aiohttp
import time
import async_timeout

from pathlib import Path

from database import getData, addData

import icons


async def detect_fname(self):
    async with aiohttp.ClientSession() as session:
        self.filename = ""
        self.settings = QSettings("DDM", "DreamDownloadManager")
        sel_lang = self.settings.value('selected_lang')

        url = str(self.urlbox.text())
        filename = str(self.enterfilename.text())
        if filename:
            self.filename = filename
        else:
            try:
                async with async_timeout.timeout(120):
                    async with session.get(url) as response:
                        if "Content-Disposition" in response.headers.keys():
                            self.filename = response.headers.get(
                                "Content-Disposition").split("filename=")[1]
                        else:
                            self.filename = url.split("/")[-1]
                        print(filename)
                        self.enterfilename.setText(self.filename)
            except Exception as e:
                print(reqerr)
                if sel_lang == "tr":
                    hata = QMessageBox.warning(self.add_download_dialog, "İndirme Başarısız", str(
                        e), QMessageBox.Ok, QMessageBox.Ok)
                elif sel_lang == "en":
                    hata = QMessageBox.warning(self.add_download_dialog, "Download Failed", str(
                        e), QMessageBox.Ok, QMessageBox.Ok)
                    hata.close()


async def detect_fsize(self):
    async with aiohttp.ClientSession() as session:
        self.filesize = ""
        self.settings = QSettings("DDM", "DreamDownloadManager")
        sel_lang = self.settings.value('selected_lang')

        url = str(self.urlbox.text())
        async with async_timeout.timeout(120):
            async with session.get(url) as response:
                if "Content-Length" in response.headers.keys():
                    filesize_kb = float(response.headers["Content-Length"])
                    self.filesize = round((filesize_kb / 1024 / 1024), 2)
                else:
                    if sel_lang == "tr":
                        self.filesize = "Bilinmeyen Boyut"
                    elif sel_lang == "en":
                        self.filesize = "Unknown Size"
                print(self.filesize)

        # return self.filesize


async def check_connection(self):
    async with aiohttp.ClientSession() as session:
        url = str(self.urlbox.text())
        try:
            async with async_timeout.timeout(120):
                async with session.get(url) as response:
                    if response:
                        self.connection = True
                    else:
                        self.connection = False
        except Exception as e:
            print(e)
            hata = QMessageBox.warning(self.add_download_dialog, "Download Failed", str(
                e), QMessageBox.Ok, QMessageBox.Ok)
            self.connection = False


def download(self):
    url = str(self.urlbox.text())
    fdowndir = self.downdirectory.text()

    async def download_file(url):
        total_size = 0
        start_time = time.time()
        start = time.time()
        run_once = 0
        try:
            fdownname = fdowndir + "/" + self.filename
            async with aiohttp.ClientSession() as session:
                # async with async_timeout.timeout(None):
                async with session.get(url, timeout=None) as response:
                    with open(fdownname, 'wb') as fd:
                        async for data in response.content.iter_chunked(1024 * 16):
                            fd.write(data)
                            total_size += len(data)
                            downloaded = total_size / (1024 * 1024)
                            self.percentage = round(
                                ((downloaded / self.filesize) * 100), 2)
                            self.progressbar.setValue(self.percentage)
                            # print(
                            #    f'{time.time() - start:0.2f}s, downloaded: {total_size / (1024 * 1024):0.0f}MB, {self.percentage}%')

            self.duration = f"Finished in {time.time() - start_time:0.2f}"
            if self.sel_lang == "tr":
                basarili = QMessageBox.information(
                    self.add_download_dialog, "İndirme Başarılı", "İndirme başarılı bir şekilde tamamlandı!", QMessageBox.Close, QMessageBox.Close)
            elif self.sel_lang == "en":
                basarili = QMessageBox.information(
                    self.add_download_dialog, "Succesful", "Download Succesfuly Finished!", QMessageBox.Close, QMessageBox.Close)
            self.add_download_dialog.close()

            data = f"{self.filename}  {self.duration}"
            addData(data, fdowndir, self.filename)
            self.download_Cache()
        except Exception as e:
            print(e)
            self.connection = False

    def ifsurestart():
        if self.sel_lang == "tr":
            # .format(self.filename, self.filesize, fdowndir))
            download_info = QMessageBox.question(self.add_download_dialog, "İndirmeyi Başlat",
                                                 f"Dosya İsmi={self.filename}\nBoyut={self.filesize} MB\n\nİndirilecek Konum={fdowndir}\n\nİndirmeyi başlatmak için evete bas")
        elif self.sel_lang == "en":
            # .format(self.filename, self.filesize, fdowndir))
            download_info = QMessageBox.question(self.add_download_dialog, "Start Download",
                                                 f"Filename={self.filename}\nFilesize={self.filesize}\nDownload Dir={fdowndir}\n\nTo start download press Yes")
        if download_info == QMessageBox.Yes:
            self.downloadbutton.hide()
            loop = asyncio.get_event_loop()
            loop.run_until_complete(download_file(url))
            print(self.duration)
        self.filename = ""
        self.downloadbutton.show()

    # Start Download Thread
    try:
        checkconnectionloop = asyncio.get_event_loop()
        checkconnectionloop.run_until_complete(self.check_connection())
        if self.connection == False:
            connection_err = QMessageBox.warning(
                self.add_download_dialog, "İndirme Başarısız", "Bağlantınızı veya url'yi Kontrol Ediniz!", QMessageBox.Ok, QMessageBox.Ok)
        else:
            fnameloop = asyncio.get_event_loop()
            fnameloop.run_until_complete(self.detect_fname())
            fsizeloop = asyncio.get_event_loop()
            fsizeloop.run_until_complete(self.detect_fsize())

            myfile = Path(f"{fdowndir}/{self.filename}")

            if myfile.exists():
                # if isfile(f"{self.downdirectory}/{self.enterfilename}"):
                if self.sel_lang == "tr":
                    self.fileexists = QMessageBox.warning(
                        self.add_download_dialog, "Varolan Dosya", "Dosya zaten var. Lütfen başka bir dosya ismi giriniz. Yoksa o dosya silinip yerine indirilecek dosya gelecektir!", QMessageBox.Ok | QMessageBox.No, QMessageBox.Ok)
                elif self.sel_lang == "en":
                    self.fileexists = QMessageBox.warning(
                        self.add_download_dialog, "Existing File", "Please enter another NAME or existing file will be overridden", QMessageBox.Ok | QMessageBox.No, QMessageBox.Ok)
                if self.fileexists == QMessageBox.Yes:
                    pass
                elif self.fileexists == QMessageBox.No:
                    myfile.unlink()
                    ifsurestart()
            else:
                ifsurestart()

    except Exception as e:
        print(e)
        hata = QMessageBox.warning(self.add_download_dialog, "Download Failed", str(
            e), QMessageBox.Ok, QMessageBox.Ok)
