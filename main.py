import sys, Engine, Player

from PyQt5 import uic  # Импортируем uic
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QListWidget, QListWidgetItem, QWidget
from PyQt5.QtGui import QPixmap




class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('untitled.ui', self)  # Загружаем дизайн
        # Донастраиваем форму
        self.reloadForm()



    def reloadForm(self): # SetSettings
        self.label.setPixmap(QPixmap('Pictures/p.png'))
        self.label_3.setPixmap(QPixmap('Pictures/l.png'))
        self.label_5.setPixmap(QPixmap('Pictures/v.png'))
        self.label_6.setPixmap(QPixmap('Pictures/penUp.png'))
        self.label_8.setPixmap(QPixmap('Pictures/penDown.png'))

        self.btnRight.clicked.connect(lambda: Engine.add(self, 'r'))
        self.btnLeft.clicked.connect(lambda: Engine.add(self, 'l'))
        self.btnForvard.clicked.connect(lambda: Engine.add(self, 'f'))
        self.btnUp.clicked.connect(lambda: Engine.add(self, 'u'))
        self.btnDown.clicked.connect(lambda: Engine.add(self, 'd'))
        self.btnPlay.clicked.connect(lambda: Player.start(self))
        self.btnRemove.clicked.connect(lambda: Engine.remove(self))
        self.btnNew.clicked.connect(lambda: Engine.new(self))


        QtCore.Qt.Checked









    #     Рудимент
    def addToList(self):
        item = QListWidgetItem(self.listWidget)

        a = Forvard()
        item.setSizeHint(a.size())
        self.listWidget.setItemWidget(item, a)

        item = QListWidgetItem(self.listWidget)

        a = RotateRight()
        item.setSizeHint(a.size())
        self.listWidget.setItemWidget(item, a)

        item = QListWidgetItem(self.listWidget)

        a = RotateLeft()
        item.setSizeHint(a.size())
        self.listWidget.setItemWidget(item, a)

        item = QListWidgetItem(self.listWidget)

        a = PenUp()
        item.setSizeHint(a.size())
        self.listWidget.setItemWidget(item, a)

        item = QListWidgetItem(self.listWidget)

        a = PenDown()
        item.setSizeHint(a.size())
        self.listWidget.setItemWidget(item, a)

        item = QListWidgetItem(self.listWidget)

        a = PenDown()
        item.setSizeHint(a.size())
        self.listWidget.setItemWidget(item, a)



def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec_())
