import sys

from PyQt6.QtWidgets import QApplication, QDialog, QListWidgetItem
from PyQt6.QtCore import QRect, QSize
from PyQt6.QtGui import QIcon

from template.mainWindow.mainWindow import Ui_MainWindow
from template.ranobeView.ranobeView import Ui_ranobeView

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



    def loadRecomendationRanobe(self):
        self.ui.recList = parseHomePage()

        for i in range(len(self.ui.recList)):
            ran = ranobeClass(
                name=self.ui.recList[i]['name'],
                coverUrl=self.ui.recList[i]['coverUrl'],
                volume=self.ui.recList[i]['vovule'],
                chapters=self.ui.recList[i]['chapters'],
                id=self.ui.recList[i]['id']
            )

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


            self.ui.searchResultList = searchRanobe(self.ui.searchEdit.text())

            for i in range(len(self.ui.searchResultList)):
                self.ui.searchResult.addItem(QListWidgetItem(self.ui.searchResultList[i].name))

    def initRanobeView(self, id):
        self.uiView = Ui_ranobeView()
        self.uiView.setupUi(self)








if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = mainWindow()
    window.show()
    window.loadRecomendationRanobe()

    sys.exit(app.exec())
