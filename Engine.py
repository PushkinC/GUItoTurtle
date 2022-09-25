import penUp, penDown, forvard, rotateRight, rotateLeft
from PyQt5.QtWidgets import QListWidgetItem, QWidget


# Custom Widgets
class PenDown(QWidget, penDown.Ui_Form):
    def __init__(self, *args, **kwargs):
        QWidget.__init__(self, *args, **kwargs)
        self.setupUi(self)


class PenUp(QWidget, penUp.Ui_Form):
    def __init__(self, *args, **kwargs):
        QWidget.__init__(self, *args, **kwargs)
        self.setupUi(self)


class Forvard(QWidget, forvard.Ui_Form):
    def __init__(self, *args, **kwargs):
        QWidget.__init__(self, *args, **kwargs)
        self.setupUi(self)


class RotateRight(QWidget, rotateRight.Ui_Form):
    def __init__(self, *args, **kwargs):
        QWidget.__init__(self, *args, **kwargs)
        self.setupUi(self)


class RotateLeft(QWidget, rotateLeft.Ui_Form):
    def __init__(self, *args, **kwargs):
        QWidget.__init__(self, *args, **kwargs)
        self.setupUi(self)


def add(self, btn):
    # Если есть новый элемент
    self.btnNew.setEnabled(True)
    for i in range(self.listWidget.count()):
        if self.listWidget.item(i).text() == 'new':
            item = self.listWidget.item(i)
            match btn:
                case 'r':
                    a = RotateRight()
                    a.labelRight.setText(self.labelRight.text())
                    item.setSizeHint(a.size())
                    item.setText(f'r{a.labelRight.text()}')
                    self.listWidget.setItemWidget(item, a)
                    return
                case 'l':
                    a = RotateLeft()
                    a.labelLeft.setText(self.labelLeft.text())
                    item.setSizeHint(a.size())
                    item.setText(f'l{a.labelLeft.text()}')
                    self.listWidget.setItemWidget(item, a)
                    return
                case 'f':
                    a = Forvard()
                    a.labelForvard.setText(self.labelForvard.text())
                    item.setSizeHint(a.size())
                    item.setText(f'f{a.labelForvard.text()}')
                    self.listWidget.setItemWidget(item, a)
                    return
                case 'u':
                    a = PenUp()
                    item.setSizeHint(a.size())
                    item.setText('u')
                    self.listWidget.setItemWidget(item, a)
                    return
                case 'd':
                    a = PenDown()
                    item.setSizeHint(a.size())
                    item.setText('d')
                    self.listWidget.setItemWidget(item, a)
                    return

    # Просто добавление
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


def remove(self):
    listItems = self.listWidget.selectedItems()
    if not listItems: return

    for item in listItems:
        self.listWidget.takeItem(self.listWidget.row(item))  # Строка удаления


def new(self):
    listItem = self.listWidget.selectedItems()
    if not listItem: return

    listItem = listItem[0]

    for i in range(self.listWidget.count()):
        if listItem == self.listWidget.item(i):
            id = i
            break

    self.listWidget.insertItem(id, 'new')
    self.btnNew.setEnabled(False)