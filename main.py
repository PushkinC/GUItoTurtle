import sys, Engine, Player, File
from PyQt5 import uic, QtGui  # Импортируем uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QPixmap, QPainter, QIntValidator, QIcon
import ui_file


class MyWidget(QMainWindow, ui_file.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        # uic.loadUi('untitled.ui', self)  # Загружаем дизайн
        self.setupUi(self)
        # Донастраиваем форму
        self.reloadForm()

    def reloadForm(self):  # SetSettings
        self.label.setPixmap(QPixmap('Pictures/p.png'))
        self.label_3.setPixmap(QPixmap('Pictures/l.png'))
        self.label_5.setPixmap(QPixmap('Pictures/v.png'))
        self.label_6.setPixmap(QPixmap('Pictures/penUp.png'))
        self.label_8.setPixmap(QPixmap('Pictures/penDown.png'))

        self.textForvard.setValidator(QIntValidator(1, 9999, self))
        self.textRight.setValidator(QIntValidator(1, 359))
        self.textLeft.setValidator(QIntValidator(1, 359))

        self.setWindowIcon(QIcon('Pictures/icon.ico'))


        self.btnRight.clicked.connect(lambda: Engine.add(self, 'r'))
        self.btnLeft.clicked.connect(lambda: Engine.add(self, 'l'))
        self.btnForvard.clicked.connect(lambda: Engine.add(self, 'f'))
        self.btnUp.clicked.connect(lambda: Engine.add(self, 'u'))
        self.btnDown.clicked.connect(lambda: Engine.add(self, 'd'))
        self.btnPlay.clicked.connect(lambda: Player.start(self))
        self.btnRemove.clicked.connect(lambda: Engine.remove(self))
        self.btnNew.clicked.connect(lambda: Engine.new(self))

        self.newFileBtn.triggered.connect(lambda: File.new(self))
        self.openFileBtn.triggered.connect(lambda: File.opend(self))
        self.saveFileBtn.triggered.connect(lambda: File.save(self))





def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec_())
