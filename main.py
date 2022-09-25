import penUp, penDown, forvard, rotateRight, rotateLeft, PyQt5, sys, Player

from PyQt5 import uic  # Импортируем uic
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QListWidget, QListWidgetItem, QWidget
from PyQt5.QtGui import QPixmap


#Custom Widget*
class PenDown(QWidget, penDown.Ui_Form):
    def __init__(self,*args,**kwargs):
        QWidget.__init__(self,*args,**kwargs)
        self.setupUi(self)

class PenUp(QWidget, penUp.Ui_Form):
    def __init__(self,*args,**kwargs):
        QWidget.__init__(self,*args,**kwargs)
        self.setupUi(self)

class Forvard(QWidget, forvard.Ui_Form):
    def __init__(self,*args,**kwargs):
        QWidget.__init__(self,*args,**kwargs)
        self.setupUi(self)

class RotateRight(QWidget, rotateRight.Ui_Form):
    def __init__(self,*args,**kwargs):
        QWidget.__init__(self,*args,**kwargs)
        self.setupUi(self)

class RotateLeft(QWidget, rotateLeft.Ui_Form):
    def __init__(self, *args,**kwargs):
        QWidget.__init__(self,*args,**kwargs)
        self.setupUi(self)


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

        self.btnRight.clicked.connect(lambda: self.add('r'))
        self.btnLeft.clicked.connect(lambda: self.add('l'))
        self.btnForvard.clicked.connect(lambda: self.add('f'))
        self.btnUp.clicked.connect(lambda: self.add('u'))
        self.btnDown.clicked.connect(lambda: self.add('d'))
        self.btnPlay.clicked.connect(lambda: Player.start(self))







    def add(self, btn):
        print(btn)

        item = QListWidgetItem(self.listWidget)

        match btn:
            case 'r':
                a = RotateRight()
                a.labelRight.setText(self.labelRight.text())
                item.setSizeHint(a.size())
                item.setText(f'r{a.labelRight.text()}')
                self.listWidget.setItemWidget(item, a)
            case 'l':
                a = RotateLeft()
                a.labelLeft.setText(self.labelLeft.text())
                item.setSizeHint(a.size())
                item.setText(f'l{a.labelLeft.text()}')
                self.listWidget.setItemWidget(item, a)
            case 'f':
                a = Forvard()
                a.labelForvard.setText(self.labelForvard.text())
                item.setSizeHint(a.size())
                item.setText(f'f{a.labelForvard.text()}')
                self.listWidget.setItemWidget(item, a)
            case 'u':
                a = PenUp()
                item.setSizeHint(a.size())
                item.setText('u')
                self.listWidget.setItemWidget(item, a)
            case 'd':
                a = PenDown()
                item.setSizeHint(a.size())
                item.setText('d')
                self.listWidget.setItemWidget(item, a)

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
