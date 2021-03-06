#!/usr/bin/python3
# -*- coding: utf-8 -*-
 
import sys
import time
import urllib
from matplotlib.pyplot import yticks

from pytube import YouTube, StreamQuery
import pytube.request
 
from PyQt5 import QtGui, QtCore 
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPixmap, QMovie, QImage

from mainwindow import Ui_MainWindow

# Change the value here to something smaller to decrease chunk sizes,
#  thus increasing the number of times that the progress callback occurs
pytube.request.default_range_size = 1*1024*1024  # 9MB chunk size

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent = None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)

        self.filesize = []

        self.progressBar.setValue(0)

    def update_info(self, title, author, date, length, views, size, image, streams, yt):
        self.yt = yt

        self.title.setText(title)
        self.author.setText(author)
        self.date.setText(date)
        self.length.setText(str(length))
        self.views.setText(str(views))
        self.thumbnail.setPixmap(QPixmap(image))

        self.filesize = size.copy()
        self.size.setText(str(self.filesize[0]))

        self.streams = streams
        for i in self.streams:
            self.resolutions.addItem(f'{i}')

        self.console.append(f'Parsing YouTube URL is finished')        
        self.download_btn.setEnabled(True)

        self.parse_thread.stop()

    def parse_url(self):
        if not self.url.text().startswith('https://www.youtube.com/'):
            self.console.append(f'the input URL {self.url.text()} is not a valid YouTube URL, please input another URL again.')
            self.url.clear()
            return 

        self.console.append(f'Start to parse YouTube URL {self.url.text()}')

        self.parse_thread = ParseThreadClass(parent=None, url=self.url.text())
        self.parse_thread.start()
        self.parse_thread.parse_signal.connect(self.update_info)

    def resolution_select(self, index):
        self.size.setText(str(self.filesize[index]))

    def download(self):
        self.download_thread = DownloadThreadClass(parent=None, index=self.resolutions.currentIndex(), streams=self.streams, yt=self.yt)
        self.download_thread.start()
        self.download_thread.download_signal.connect(self.download_progress)
        self.download_thread.complete_signal.connect(self.download_complete)

    def download_complete(self):
        self.console.append("Download completes!")
        self.download_thread.stop()

    def download_progress(self, percentage):
        self.progressBar.setValue(int(percentage*100))

class ParseThreadClass(QtCore.QThread):
    parse_signal = QtCore.pyqtSignal(str, str, str, float, int, list, QImage, StreamQuery, YouTube)

    def __init__(self, parent=None, url=None):
        super(ParseThreadClass, self).__init__(parent)
        self.is_running = True
        self.url = url
        self.filesize = []

    def run(self):
        print('Starting parse thread...')

        yt = YouTube(self.url)

        title   = yt.title
        author  = yt.author
        date    = str(yt.publish_date)
        length  = yt.length
        views   = yt.views

        ytthumbnail = urllib.request.urlopen(yt.thumbnail_url).read()

        image = QImage()
        image.loadFromData(ytthumbnail)

        self.streams = yt.streams

        self.filesize.append(self.streams.get_highest_resolution().filesize)
        self.filesize.append(self.streams.first().filesize)

        for i in self.streams:
            print(i.filesize)
            self.filesize.append(i.filesize)

        self.parse_signal.emit(title, author, date, length, views, self.filesize, image, self.streams, yt) 
    
    def stop(self):
        self.is_running = False
        print('Stopping parse thread...')
        self.terminate()     

class DownloadThreadClass(QtCore.QThread):
    download_signal = QtCore.pyqtSignal(float)
    complete_signal = QtCore.pyqtSignal()

    def __init__(self, parent=None, index=None, streams=None, yt=None):
        super(DownloadThreadClass, self).__init__(parent)
        self.is_running = True
        self.index = index
        self.streams = streams
        self.yt = yt

        self.yt.register_on_progress_callback(self.progress_Check)
        self.yt.register_on_complete_callback(self.complete)

    def run(self):
        print('Starting download thread...')

        if self.index == 0:
            self.filesize = self.streams.get_highest_resolution().filesize
            self.streams.get_highest_resolution().download()
        elif self.index == 1:
            self.filesize = self.streams.first().filesize
            self.streams.first().download()
        else:
            self.filesize = self.streams[self.index-2].filesize
            self.streams[self.index-2].download()

    def stop(self):
        self.is_running = False
        print('Stopping download thread...')
        self.terminate()

    # on_progress_callback takes 4 parameters.
    def progress_Check(self, stream = None, chunk = None, bytes_remaining = None):
        #Gets the percentage of the file that has been downloaded.
        # percent = (100*(self.file_size-remaining))/self.file_size
        # print("{:00.0f}% downloaded".format(percent))        
        print(bytes_remaining)      
        self.download_signal.emit((self.filesize-bytes_remaining)/self.filesize) 

    def complete(self, stream = None, file_path = None):
        self.complete_signal.emit() 


if __name__ == '__main__':
    #??????pyqt5???????????????????????????????????????????????????sys.argv???????????????????????????????????????????????????
    app = QApplication(sys.argv)
    
    win = MainWindow()
    
    win.setWindowIcon(QtGui.QIcon('image\youtube_icon.png'))

    #??????????????????
    win.show()
    
    #??????exit()???????????????????????????????????????
    #???exec_()??????????????????????????????????????????Python?????????????????????exec_()??????
    sys.exit(app.exec_())
