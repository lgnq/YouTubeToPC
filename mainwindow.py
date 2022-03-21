# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 480)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 0, 0, 1, 1)
        self.author = QtWidgets.QLineEdit(self.centralwidget)
        self.author.setEnabled(False)
        self.author.setObjectName("author")
        self.gridLayout_2.addWidget(self.author, 0, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 1, 0, 1, 1)
        self.date = QtWidgets.QLineEdit(self.centralwidget)
        self.date.setEnabled(False)
        self.date.setText("")
        self.date.setObjectName("date")
        self.gridLayout_2.addWidget(self.date, 1, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 2, 0, 1, 1)
        self.length = QtWidgets.QLineEdit(self.centralwidget)
        self.length.setEnabled(False)
        self.length.setText("")
        self.length.setObjectName("length")
        self.gridLayout_2.addWidget(self.length, 2, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 3, 0, 1, 1)
        self.views = QtWidgets.QLineEdit(self.centralwidget)
        self.views.setEnabled(False)
        self.views.setText("")
        self.views.setObjectName("views")
        self.gridLayout_2.addWidget(self.views, 3, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 4, 0, 1, 1)
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.gridLayout_2.addWidget(self.comboBox, 4, 1, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_2, 1, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem, 2, 0, 1, 1)
        self.download_btn = QtWidgets.QPushButton(self.centralwidget)
        self.download_btn.setEnabled(False)
        self.download_btn.setStyleSheet("background-color: rgb(255, 0, 0);\n"
"font: 8pt \"Goudy Stout\";")
        self.download_btn.setObjectName("download_btn")
        self.gridLayout_3.addWidget(self.download_btn, 2, 1, 1, 1)
        self.console = QtWidgets.QTextBrowser(self.centralwidget)
        self.console.setObjectName("console")
        self.gridLayout_3.addWidget(self.console, 3, 0, 1, 2)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.url = QtWidgets.QLineEdit(self.centralwidget)
        self.url.setObjectName("url")
        self.gridLayout.addWidget(self.url, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.title = QtWidgets.QLineEdit(self.centralwidget)
        self.title.setObjectName("title")
        self.gridLayout.addWidget(self.title, 1, 1, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout, 0, 0, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.url.returnPressed.connect(MainWindow.parse_url)
        self.download_btn.clicked.connect(MainWindow.download)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "YouTubeToPC"))
        self.label_4.setText(_translate("MainWindow", "Author:"))
        self.label_5.setText(_translate("MainWindow", "Date:"))
        self.label_6.setText(_translate("MainWindow", "Length:"))
        self.label_7.setText(_translate("MainWindow", "Views:"))
        self.label_3.setText(_translate("MainWindow", "Resolution:"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Highest Resolution"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Best Available"))
        self.download_btn.setText(_translate("MainWindow", "DOWNLOAD"))
        self.label.setText(_translate("MainWindow", "URL:"))
        self.label_2.setText(_translate("MainWindow", "Title:"))
