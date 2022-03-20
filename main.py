#!/usr/bin/python3
# -*- coding: utf-8 -*-
 
import sys

from pytube import YouTube
 
from PyQt5.QtWidgets import QApplication, QMainWindow
from mainwindow import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent = None):
        super(MainWindow, self).__init__(parent)

        self.setupUi(self)

    def parse_url(self):
        self.yt = YouTube(self.url.text())
        self.title.setText(self.yt.title)

        self.console.append(f'Title: {self.yt.title}')
        self.console.append(f'Author: {self.yt.author}')
        self.console.append(f'Date: {self.yt.publish_date}')

if __name__ == '__main__':
    #每一pyqt5应用程序必须创建一个应用程序对象。sys.argv参数是一个列表，从命令行输入参数。
    app = QApplication(sys.argv)
    
    win = MainWindow()
    
    #显示在屏幕上
    win.show()
    
    #系统exit()方法确保应用程序干净的退出
    #的exec_()方法有下划线。因为执行是一个Python关键词。因此，exec_()代替
    sys.exit(app.exec_())
