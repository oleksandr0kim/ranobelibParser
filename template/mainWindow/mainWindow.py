# Form implementation generated from reading ui file 'mainWindow.ui'
#
# Created by: PyQt6 UI code generator 6.3.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 560)
        MainWindow.setMinimumSize(QtCore.QSize(800, 560))
        MainWindow.setMaximumSize(QtCore.QSize(800, 560))
        MainWindow.setAcceptDrops(False)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("template/icon/mainWinIcon.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("#MainWindow{\n"
"    background:  #272727;\n"
"}\n"
"")
        self.recomendList = QtWidgets.QListWidget(MainWindow)
        self.recomendList.setGeometry(QtCore.QRect(10, 170, 780, 380))
        self.recomendList.setStyleSheet("#recomendList{\n"
"    background: #48494a;\n"
"}")
        self.recomendList.setFlow(QtWidgets.QListView.Flow.LeftToRight)
        self.recomendList.setObjectName("recomendList")
        self.recomendList.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.searchResult = QtWidgets.QListWidget(MainWindow)
        self.searchResult.setGeometry(QtCore.QRect(10, 66, 675, 100))
        self.searchResult.setStyleSheet("#searchResult{\n"
"    background: #48494a;\n"
"}")
        self.searchResult.setObjectName("searchResult")
        self.searchResult.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.searchResult.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.searchEdit = QtWidgets.QLineEdit(MainWindow)
        self.searchEdit.setGeometry(QtCore.QRect(10, 30, 675, 35))
        self.searchEdit.setStyleSheet("#searchEdit{\n"
"    background: #000000;\n"
"    color: #ffffff;\n"
"    font-size: 18px;\n"
"}")
        self.searchEdit.setObjectName("searchEdit")
        self.searchButton = QtWidgets.QPushButton(MainWindow)
        self.searchButton.setGeometry(QtCore.QRect(690, 30, 100, 35))
        self.searchButton.setStyleSheet("#searchButton{\n"
"    background-color: #000000;\n"
"    font-family: monospace;\n"
"    color: #ffffff;\n"
"}\n"
"\n"
"#searchButton:hover{\n"
"    background-color: #666;\n"
"    color: #272727;\n"
"}\n"
"\n"
"")
        self.searchButton.setObjectName("searchButton")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "RenobeParser"))
        self.searchButton.setText(_translate("MainWindow", "Search"))
