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
        MainWindow.resize(643, 605)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setMaximumSize(QtCore.QSize(54, 16))
        self.label_3.setObjectName("label_3")
        self.gridLayout_3.addWidget(self.label_3, 0, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setObjectName("label_8")
        self.gridLayout_3.addWidget(self.label_8, 1, 0, 1, 1)
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.gridLayout_3.addWidget(self.progressBar, 2, 0, 1, 2)
        self.download_btn = QtWidgets.QPushButton(self.centralwidget)
        self.download_btn.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.download_btn.sizePolicy().hasHeightForWidth())
        self.download_btn.setSizePolicy(sizePolicy)
        self.download_btn.setStyleSheet("")
        self.download_btn.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("image/download.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.download_btn.setIcon(icon)
        self.download_btn.setIconSize(QtCore.QSize(127, 31))
        self.download_btn.setFlat(True)
        self.download_btn.setObjectName("download_btn")
        self.gridLayout_3.addWidget(self.download_btn, 2, 2, 1, 1)
        self.resolutions = QtWidgets.QComboBox(self.centralwidget)
        self.resolutions.setObjectName("resolutions")
        self.resolutions.addItem("")
        self.resolutions.addItem("")
        self.gridLayout_3.addWidget(self.resolutions, 0, 1, 1, 2)
        self.Captions = QtWidgets.QComboBox(self.centralwidget)
        self.Captions.setObjectName("Captions")
        self.gridLayout_3.addWidget(self.Captions, 1, 1, 1, 2)
        self.gridLayout_4.addLayout(self.gridLayout_3, 2, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.url = QtWidgets.QLineEdit(self.centralwidget)
        self.url.setObjectName("url")
        self.horizontalLayout.addWidget(self.url)
        self.gridLayout_4.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.console = QtWidgets.QTextBrowser(self.centralwidget)
        self.console.setObjectName("console")
        self.gridLayout_4.addWidget(self.console, 3, 0, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.title = QtWidgets.QLineEdit(self.groupBox)
        self.title.setObjectName("title")
        self.gridLayout.addWidget(self.title, 0, 1, 1, 1)
        self.thumbnail = QtWidgets.QLabel(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.thumbnail.sizePolicy().hasHeightForWidth())
        self.thumbnail.setSizePolicy(sizePolicy)
        self.thumbnail.setMinimumSize(QtCore.QSize(281, 171))
        self.thumbnail.setMaximumSize(QtCore.QSize(281, 171))
        self.thumbnail.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.thumbnail.setText("")
        self.thumbnail.setPixmap(QtGui.QPixmap("image/tumbnail.png"))
        self.thumbnail.setScaledContents(True)
        self.thumbnail.setAlignment(QtCore.Qt.AlignCenter)
        self.thumbnail.setObjectName("thumbnail")
        self.gridLayout.addWidget(self.thumbnail, 0, 2, 6, 1)
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 1, 0, 1, 1)
        self.author = QtWidgets.QLineEdit(self.groupBox)
        self.author.setEnabled(False)
        self.author.setObjectName("author")
        self.gridLayout.addWidget(self.author, 1, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 2, 0, 1, 1)
        self.date = QtWidgets.QLineEdit(self.groupBox)
        self.date.setEnabled(False)
        self.date.setText("")
        self.date.setObjectName("date")
        self.gridLayout.addWidget(self.date, 2, 1, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.groupBox)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 3, 0, 1, 1)
        self.size = QtWidgets.QLineEdit(self.groupBox)
        self.size.setEnabled(False)
        self.size.setText("")
        self.size.setObjectName("size")
        self.gridLayout.addWidget(self.size, 3, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 4, 0, 1, 1)
        self.length = QtWidgets.QLineEdit(self.groupBox)
        self.length.setEnabled(False)
        self.length.setText("")
        self.length.setObjectName("length")
        self.gridLayout.addWidget(self.length, 4, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 5, 0, 1, 1)
        self.views = QtWidgets.QLineEdit(self.groupBox)
        self.views.setEnabled(False)
        self.views.setText("")
        self.views.setObjectName("views")
        self.gridLayout.addWidget(self.views, 5, 1, 1, 1)
        self.gridLayout_4.addWidget(self.groupBox, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 643, 21))
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
        self.label_3.setText(_translate("MainWindow", "Resolution:"))
        self.label_8.setText(_translate("MainWindow", "Caption:"))
        self.resolutions.setItemText(0, _translate("MainWindow", "Highest Resolution"))
        self.resolutions.setItemText(1, _translate("MainWindow", "Best Available"))
        self.label.setText(_translate("MainWindow", "URL:"))
        self.groupBox.setTitle(_translate("MainWindow", "Info"))
        self.label_2.setText(_translate("MainWindow", "Title:"))
        self.label_4.setText(_translate("MainWindow", "Author:"))
        self.label_5.setText(_translate("MainWindow", "Date:"))
        self.label_9.setText(_translate("MainWindow", "Size:"))
        self.label_6.setText(_translate("MainWindow", "Length:"))
        self.label_7.setText(_translate("MainWindow", "Views:"))
