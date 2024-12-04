import sys

from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtGui import QColor, QPainter
from PyQt6.QtCore import QPointF
from random import randint, choice


class Project(QMainWindow):
    def __init__(self):
        try:
            self.f = False
            super().__init__()
            uic.loadUi('UI.ui', self)
            self.add.clicked.connect(self.run)
        except Exception as e:
            print('%s' % e)

    def paintEvent(self, event):
        try:
            if self.f is True:
                qp = QPainter()
                qp.begin(self)
                x = 300
                y = 300
                r = choice(range(20, 200))
                color = QColor(255, 255, 0)
                qp.setBrush(color)
                qp.drawEllipse(QPointF(float(x), float(y)), r * 2, r * 2)
                qp.end()
                self.f = False
        except Exception as e:
            print('%s' % e)

    def run(self):
        self.f = True
        self.update()




if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Project()
    ex.show()
    sys.exit(app.exec())
