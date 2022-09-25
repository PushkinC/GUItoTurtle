from PyQt5.QtWidgets import QFileDialog
import dill, os


def new(self):
    pass


def opend(self):
    fname = QFileDialog.getOpenFileName(self)
    print(fname[0])

    # try:
    with open(fname[0], "rb") as f:
        data = dill.load(f)
    self.listWidget = data

    # except Exception as ex:
    #     print("Error during unpickling object (Possibly unsupported):", ex)


def save(self):
    data = self.listWidget
    fname = QFileDialog.getSaveFileName(self)
    print(fname[0], 'save')

    # try:
    if not os.path.exists(fname[0]):
        open(fname[0], 'w').close()
    with open(fname[0], 'wb') as f:
        dill.dump(data, f)
    # except Exception as ex:
    #     print("Error during pickling object (Possibly unsupported):", ex)


