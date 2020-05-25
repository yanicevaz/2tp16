from PySide2.QtWidgets import *
from PySide2.QtCore import Qt


class Window(QWidget):

    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle("IHM")
        self.setMinimumSize(100, 50)
        self.layout = QHBoxLayout()
        self.progressbar = QProgressBar()
        self.slider = QSlider(Qt.Vertical)
        self.layout.addWidget(self.progressbar)
        self.layout.addWidget(self.slider)
        self.slider.valueChanged.connect(self.Changeprogressbar)
        self.setLayout(self.layout)

    def Changeprogressbar(self):
        self.progressbar.setValue(self.slider.value())
        return

    def Signal(self):
        self.valueChanged



if __name__ == "__main__":
    app = QApplication([])
    win = Window()
    win.show()
    app.exec_()
