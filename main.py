#!/usr/bin/python3
# -*- coding: utf-8 -*-
 
import sys
import urllib

from pytube import YouTube
 
from PyQt5 import QtGui 
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPixmap, QMovie, QImage

from mainwindow import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent = None):
        super(MainWindow, self).__init__(parent)

        self.setupUi(self)

    def parse_url(self):
        if not self.url.text().startswith('https://www.youtube.com/'):
            self.console.append(f'the input URL {self.url.text()} is not a valid YouTube URL, please input another URL again.')
            self.url.clear()
            return 

        self.console.append(f'Start to parse YouTube URL {self.url.text()}')

        self.yt = YouTube(self.url.text())
        self.title.setText(self.yt.title)
        
        ytthumbnail = urllib.request.urlopen(self.yt.thumbnail_url).read()

        image = QImage()
        image.loadFromData(ytthumbnail)

        self.thumbnail.setPixmap(QPixmap(image))

        self.author.setText(self.yt.author)
        self.date.setText(str(self.yt.publish_date))
        self.length.setText(str(self.yt.length))
        self.views.setText(str(self.yt.views))

        for i in self.yt.streams:
            self.comboBox.addItem(f'{i}')

        self.console.append(f'Parsing YouTube URL is finished')

        self.download_btn.setEnabled(True)

    def download(self):
        if self.comboBox.currentText() == 'Highest Resolution':
            self.yt.streams.get_highest_resolution().download()
        elif self.comboBox.currentText() == 'Best Available':
            self.yt.streams.first().download()
        else:
            self.yt.streams[self.comboBox.currentIndex()-2].download()

        self.console.append("Download completes!")

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
