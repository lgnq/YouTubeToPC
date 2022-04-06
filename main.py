#!/usr/bin/python3
# -*- coding: utf-8 -*-
 
import sys
import time
import urllib

from pytube import YouTube, StreamQuery
 
from PyQt5 import QtGui, QtCore 
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPixmap, QMovie, QImage

from mainwindow import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent = None):
        super(MainWindow, self).__init__(parent)

        self.setupUi(self)

    # on_progress_callback takes 4 parameters.
    def progress_Check(self, stream = None, chunk = None, file_handle = None, remaining = None):
        #Gets the percentage of the file that has been downloaded.
        # percent = (100*(self.file_size-remaining))/self.file_size
        # print("{:00.0f}% downloaded".format(percent))        
        print(remaining)

    def update_info(self, title, author, date, length, views, image, streams):
        self.title.setText(title)

        self.thumbnail.setPixmap(QPixmap(image))

        self.author.setText(author)
        self.date.setText(date)
        self.length.setText(str(length))
        self.views.setText(str(views))
        self.streams = streams

        for i in self.streams:
            self.resolutions.addItem(f'{i}')

        self.console.append(f'Parsing YouTube URL is finished')        
        self.download_btn.setEnabled(True)

        self.thread.stop()

    def parse_url(self):
        if not self.url.text().startswith('https://www.youtube.com/'):
            self.console.append(f'the input URL {self.url.text()} is not a valid YouTube URL, please input another URL again.')
            self.url.clear()
            return 

        self.console.append(f'Start to parse YouTube URL {self.url.text()}')

        self.parse_thread = ParseThreadClass(parent=None, url=self.url.text())
        self.parse_thread.start()
        self.parse_thread.parse_signal.connect(self.update_info)

    def download(self):
        # if self.resolutions.currentText() == 'Highest Resolution':
        #     self.yt.streams.get_highest_resolution().download()
        # elif self.resolutions.currentText() == 'Best Available':
        #     self.yt.streams.first().download()
        # else:
        #     self.yt.streams[self.resolutions.currentIndex()-2].download()

        self.download_thread = DownloadThreadClass(parent=None, index=self.resolutions.currentIndex(), streams=self.streams)
        self.download_thread.start()
        self.download_thread.download_signal.connect(self.download_complete)

    def download_complete(self):
        self.console.append("Download completes!")

class ParseThreadClass(QtCore.QThread):
    parse_signal = QtCore.pyqtSignal(str, str, str, float, int, QImage, StreamQuery)

    def __init__(self, parent=None, url=None):
        super(ParseThreadClass, self).__init__(parent)
        self.is_running = True
        self.url = url

    def run(self):
        print('Starting thread...')

        yt = YouTube(self.url)

        title   = yt.title
        author  = yt.author
        date    = str(yt.publish_date)
        length  = yt.length
        views   = yt.views

        ytthumbnail = urllib.request.urlopen(yt.thumbnail_url).read()

        image = QImage()
        image.loadFromData(ytthumbnail)

        streams = yt.streams

        self.parse_signal.emit(title, author, date, length, views, image, streams) 
    
    def stop(self):
        self.is_running = False
        print('Stopping thread...')
        self.terminate()        

class DownloadThreadClass(QtCore.QThread):
    download_signal = QtCore.pyqtSignal()

    def __init__(self, parent=None, index=None, streams=None):
        super(DownloadThreadClass, self).__init__(parent)
        self.is_running = True
        self.index = index
        self.streams = streams

    def run(self):
        print('Starting thread...')

        if self.index == 0:
            self.streams.get_highest_resolution().download()
        elif self.index == 1:
            self.streams.first().download()
        else:
            self.streams[self.index-2].download()

        # while True:
        #     self.download_signal.emit() 
        #     time.sleep(1)

    def stop(self):
        self.is_running = False
        print('Stopping thread...')
        self.terminate()

if __name__ == '__main__':
    #每一pyqt5应用程序必须创建一个应用程序对象。sys.argv参数是一个列表，从命令行输入参数。
    app = QApplication(sys.argv)
    
    win = MainWindow()
    
    win.setWindowIcon(QtGui.QIcon('image\youtube_icon.png'))

    #显示在屏幕上
    win.show()
    
    #系统exit()方法确保应用程序干净的退出
    #的exec_()方法有下划线。因为执行是一个Python关键词。因此，exec_()代替
    sys.exit(app.exec_())
