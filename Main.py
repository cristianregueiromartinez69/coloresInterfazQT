import random
import sys
import math
from cProfile import label

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPalette, QColor
from PyQt6.QtWidgets import (QMainWindow, QApplication, QVBoxLayout, QPushButton, QWidget, QLabel, QLineEdit,
                             QHBoxLayout)

from Marcos import fila1, fila2, fila3

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Colores dividivos")
        self.setFixedSize(800,600)

        fondo_principal = QHBoxLayout()

        #añadimos los layouts creados en otra clase
        fondo_principal.addLayout(fila1())
        fondo_principal.addLayout(fila2())
        fondo_principal.addLayout(fila3())

        container = QWidget()
        container.setLayout(fondo_principal)
        self.setCentralWidget(container)

        self.show()

if __name__ == "__main__":
    aplicacion = QApplication(sys.argv)
    fiestra = MyApp()
    aplicacion.exec()
