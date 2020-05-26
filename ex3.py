from PySide2.QtWidgets import *

class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle("IHM")
        self.setMinimumSize(500, 300)
        self.layout = QVBoxLayout()
        self.button = QPushButton("Changer le texte")
        self.textedit = QTextEdit("Le nombre de clics va être affiché ici")
        self.layout.addWidget(self.button)
        self.layout.addWidget(self.textedit)
        self.button.clicked.connect(self.buttonClicked)
        self.setLayout(self.layout)

        self.counter = 0


    def buttonClicked(self):
        self.counter += 1
        self.button.setText(f"Clic {self.counter}")
        self.textedit.setText(f"Click {self.counter}")

if __name__ == "__main__":
    application = QApplication([])
    window = Window()
    window.show()
    application.exec_()
