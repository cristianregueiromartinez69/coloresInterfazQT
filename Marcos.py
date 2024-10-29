from PyQt6.QtWidgets import QFrame, QVBoxLayout

'''
En esta clase tenemos 3 metodos
cada 1 de ellos devuelve un layout
'''
def fila1():
    layout = QVBoxLayout()

    marco1 = QFrame() #objeto frame
    marco1.setStyleSheet("background-color: red") #le ponemos un color de fondo
    marco1.setFixedSize(200,100) #establecemos las dimensiones

    marco2 = QFrame()
    marco2.setStyleSheet("background-color: yellow")
    marco2.setFixedSize(200, 100)

    marco3 = QFrame()
    marco3.setStyleSheet("background-color: purple")
    marco3.setFixedSize(200, 100)

    layout.addWidget(marco1)
    layout.addWidget(marco2)
    layout.addWidget(marco3)
    return layout

'''
Lo mismo en los demás métodos
hacemos frames, ponemos color de fondo y añadimos al layout
'''
def fila2():
    layout = QVBoxLayout()

    marco1 = QFrame()
    marco1.setStyleSheet("background-color: green")
    marco1.setFixedSize(200,450)

    layout.addWidget(marco1)

    return layout

def fila3():
    layout = QVBoxLayout()

    marco1 = QFrame()
    marco1.setStyleSheet("background-color: red")
    marco1.setFixedSize(200,190)

    marco2 = QFrame()
    marco2.setStyleSheet("background-color: purple")
    marco2.setFixedSize(200, 190)


    layout.addWidget(marco1)
    layout.addWidget(marco2)
    return layout

