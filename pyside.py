import sys
import numpy as np
from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QPushButton, QHBoxLayout, QApplication
from matplotlib.figure import Figure
from matplotlib.backends.backend_qtagg import FigureCanvas
class MyWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Curve Tracer V1.0")

        # On défini le widget central avec un layout de type QVBoxLayout
        mainWidget = QWidget()
        self.setCentralWidget(mainWidget)
        vbox = QVBoxLayout(mainWidget)

        # On y ajoute deux boutons dans un layout QHBoxLayout
        self.__btnSinus = QPushButton("Sinus")
        self.__btnSinus.clicked.connect(self.btnSinusClicked)
        self.__btnCosinus = QPushButton("Cosinus")
        self.__btnCosinus.clicked.connect(self.btnCosinusClicked)

        hbox = QHBoxLayout()
        hbox.addWidget(self.__btnSinus)
        hbox.addWidget(self.__btnCosinus)
        vbox.addLayout(hbox)

        # On ajoute le canvas MatPlotLib en dessous de la barre de boutons
        self.__canvas = FigureCanvas(Figure(figsize=(4, 3)))
        vbox.addWidget(self.__canvas)
        self.__plt = self.__canvas.figure.subplots()

        # On connecte un gestionnaire d'événements (un slot) au clic sur le canvas.
        # mpl_connect == MatPlotLib_connect  ;-)
        self.__canvas.mpl_connect("button_press_event", self.canvasClicked)

        # On force le tracé de la courbe Sinus à l'ouverture de la fenêtre
        self.btnSinusClicked()

    # Un slot pour réagir au clic sur le canvas MatPlotLib
    def canvasClicked(self, event):
        self.__plt.scatter(event.xdata, event.ydata, marker="+", s=100)
        self.__canvas.draw()

    # Un slot pour réagir au clic sur le bouton btnSinus
    def btnSinusClicked(self):
        self.__plt.clear()
        x = np.linspace(-10, 10, 1000)
        y = np.sin(x)
        self.__plt.plot(x, y, "r")
        self.__canvas.draw()

    # Un slot pour réagir au clic sur le bont btnCosinus
    def btnCosinusClicked(self):
        self.__plt.clear()
        x = np.linspace(-10, 10, 1000)
        y = np.cos(x)
        self.__plt.plot(x, y, "b--")
        self.__canvas.draw()


# Démarrage de la fenêtre
if __name__ == "__main__":
    app = QApplication(sys.argv)

    myWindow = MyWindow()
    myWindow.show()

    sys.exit(app.exec())
