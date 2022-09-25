from PyQt5.QtWidgets import QFileDialog
import pickle, os, Engine


def new(self):
    self.isAnim.setCheckState(2)
    self.isTurtle.setCheckState(2)
    self.listWidget.clear()
    # for i in range(self.listWidget.count()):
    #     self.listWidget.takeItem(self.listWidget.row(self.listWidget.item(i)))


def opend(self):
    fname = QFileDialog.getOpenFileName(self, filter='*.trtsv')
    print(fname[0])

    try:
        with open(fname[0], "rb") as f:
            data = pickle.load(f)
        setData(self, data)

    except Exception as ex:
        print("Error during unpickling object (Possibly unsupported):", ex)


def save(self):
    data = getData(self)
    fname = QFileDialog.getSaveFileName(self, filter='*.trtsv')
    print(fname[0], 'save')

    try:
        if not os.path.exists(fname[0]):
            open(fname[0], 'w').close()
        with open(fname[0], 'wb') as f:
            pickle.dump(data, f)
    except Exception as ex:
        print("Error during pickling object (Possibly unsupported):", ex)


def getData(self) -> list:
    lst = []
    for i in range(self.listWidget.count()):
        lst.append(self.listWidget.item(i).text())
    return lst


def setData(self, data):
    for i in data:
        Engine.load(self, i)
