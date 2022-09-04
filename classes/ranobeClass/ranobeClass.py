import io
import requests
import PIL.Image as Image

from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout, QListWidgetItem
from PyQt6.QtCore import QRect, QSize, Qt
from PyQt6.QtGui import QPixmap, QFont, QImage



class ranobeClass():
    def __init__(self, name, coverUrl, volume, chapters, id):
        self._name = name
        self._id = id
        self._manyVolume = volume
        self._chapters = chapters
        self._item, self._widget = self.newRanobeCoverWidget(name, coverUrl)

    def newRanobeCoverWidget(self, name, coverUrl):

        widget = QWidget()
        print(coverUrl)
        try:
            img = QImage()
            img.loadFromData(requests.get(coverUrl).content)
        except:
            img = 'trash/default_cover.jpg'



        widgetImage = QLabel()
        widgetImage.setPixmap(QPixmap(img))
        widgetImage.setScaledContents(True)
        widgetImage.setFixedSize(QSize(240, 341))


        widgetText = QLabel()
        widgetText.setGeometry(QRect(0, 341, 240, 39))
        widgetText.setAlignment(Qt.AlignmentFlag.AlignCenter)
        widgetText.setFont(QFont('Courier', 8 if len(name) < 35 else 7))
        widgetText.setWordWrap(True)
        widgetText.setText(name if len(name) < 35 else name[0:35])

        widgetLayout = QVBoxLayout()
        widgetLayout.addWidget(widgetImage)
        widgetLayout.addWidget(widgetText)
        widgetLayout.addStretch()

        widget.setLayout(widgetLayout)

        listWidgetItem = QListWidgetItem()
        listWidgetItem.setSizeHint(QSize(260, 350))

        return listWidgetItem, widget




    def getItem(self):
        return self._item

    def getWidget(self):
        return self._widget