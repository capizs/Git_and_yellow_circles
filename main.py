import sys
from UI import Ui_MainWindow
from random import randint
from PyQt5.QtGui import QColor, QPainter
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QMainWindow


class MyWidget(QWidget, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.flag = False
        self.add_circle.clicked.connect(self.add)


    def paintEvent(self, event):
        if self.flag:
            qp=QPainter()
            qp.begin(self)
            qp.setBrush(QColor(255, 255, 0))
            r = randint(0, 150)
            qp.drawEllipse(randint(0, 400 - r), randint(0, 400 - r), r, r)
            qp.end()

    def add(self):
        self.flag = True
        self.update()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())
