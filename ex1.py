from PySide2.QtWidgets import *
import random

class Window(QWidget):

    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle("Cycles de l'ISEN Yncréa Ouest")
        self.setMinimumSize(500, 300)
        self.layout = QVBoxLayout()
        self.label = QLabel(random.choice(["CSI", "CIR", "BIOST", "CENT", "BIAST", "EST"]))
        self.button = QPushButton("Changer le Cycle")
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.button)
        self.button.clicked.connect(self.buttonClicked)
        self.setLayout(self.layout)

    def buttonClicked(self):
        lst = ["CSI", "CIR", "BIOST", "CENT", "BIAST"]
        new = random.choice(lst)
        self.label.setText(new)
        return


if __name__ == "__main__":
    application = QApplication([])
    window = Window()
    window.show()
    application.exec_()
