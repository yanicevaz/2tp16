from PySide2.QtWidgets import *

class Window(QWidget):

    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle("IHM")
        self.setMinimumSize(500, 300)
        self.layout = QVBoxLayout()
        self.button = QPushButton("Changer mon texte")
        self.textedit = QTextEdit("Le nombre de clics va être affiché ici")
        self.layout.addWidget(self.button)
        self.layout.addWidget(self.textedit)
        self.button.clicked.connect(self.buttonClicked)
        self.setLayout(self.layout)

    #def buttonClicked(self):
    #    self.close()
    #    return
    def buttonClicked(self):
        if self.button.text() == "Changer mon texte":
            self.button.setText("Clic 1")
        else:
            nb = int((self.button.text())[5:]) + 1
            self.button.setText("Clic "+str(nb))
        self.textedit.setText(self.button.text())
        return

if __name__ == "__main__":
    app = QApplication([])
    win = Window()
    win.show()
    app.exec_()
