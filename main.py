import sys

from PyQt6.QtWidgets import QApplication, QDialog, QListWidgetItem
from PyQt6.QtCore import QRect, QSize
from PyQt6.QtGui import QIcon

from template.mainWindow.mainWindow import Ui_MainWindow
from classes.ranobeClass.ranobeClass import ranobeClass
from ranobelibViewer.ranobelibParser import parseHomePage, searchRanobe

class mainWindow(QDialog):

    def __init__(self):
        super(mainWindow, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.searchButton.clicked.connect(self.searchRanobe)
        self.ui.searchResult.clicked.connect(self.clickOnResult)
        self.ui.recomendList.clicked.connect(self.clickOnRecomendation)

        self.loadRecomendationRanobe()


    def loadRecomendationRanobe(self):
        recList = parseHomePage()

        for i in range(len(recList)):
            ran = ranobeClass(name=recList[i]['name'], coverUrl=recList[i]['coverUrl'], volume=recList[i]['vovule'], chapters=recList[i]['chapters'], id=recList[i]['id'])

            self.ui.recomendList.addItem(ran.getItem())
            self.ui.recomendList.setItemWidget(ran.getItem(), ran.getWidget())



    def clickOnRecomendation(self):
        if self.ui.recomendList:
            item = self.ui.recomendList.currentIndex()
            print(item.row())

    def clickOnResult(self):
        if self.ui.searchResult:
            item = self.ui.searchResult.currentIndex()
            print(item.row())

    def searchRanobe(self):
        self.ui.searchResult.clear()
        if self.ui.searchEdit.text():

            print(self.ui.searchEdit.text())

            res = searchRanobe(self.ui.searchEdit.text())

            for i in range(len(res)):
                self.ui.searchResult.addItem(QListWidgetItem(res[i].name))






if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = mainWindow()
    window.show()

    sys.exit(app.exec())
