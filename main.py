import sys
import io

from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtGui import QColor, QPainter
from PyQt6.QtCore import QPointF
from random import randint, choice


class Design:
    def __init__(self, ex):
        a = """<?xml version="1.0" encoding="UTF-8"?>
        <ui version="4.0">
         <class>MainWindow</class>
         <widget class="QMainWindow" name="MainWindow">
          <property name="geometry">
           <rect>
            <x>0</x>
            <y>0</y>
            <width>602</width>
            <height>638</height>
           </rect>
          </property>
          <property name="windowTitle">
           <string>MainWindow</string>
          </property>
          <widget class="QWidget" name="centralwidget">
           <widget class="QPushButton" name="add">
            <property name="geometry">
             <rect>
              <x>250</x>
              <y>490</y>
              <width>131</width>
              <height>81</height>
             </rect>
            </property>
            <property name="text">
             <string>Круг</string>
            </property>
           </widget>
          </widget>
          <widget class="QMenuBar" name="menubar">
           <property name="geometry">
            <rect>
             <x>0</x>
             <y>0</y>
             <width>602</width>
             <height>21</height>
            </rect>
           </property>
          </widget>
          <widget class="QStatusBar" name="statusbar"/>
         </widget>
         <resources/>
         <connections/>
        </ui>"""

        f = io.StringIO(a)
        uic.loadUi(f, ex)


class Project(QMainWindow):
    def __init__(self):
        try:
            self.f = False
            super().__init__()
            self.d = Design(self)
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
                color = QColor(randint(0, 256), randint(0, 256), randint(0, 256))
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
