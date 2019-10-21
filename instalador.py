from instalador_ui import *
from dialogoCrear_ui import *
from espera_ui import Ui_Dialog as WaitWindow

import os
import subprocess

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)

        # Cambiando el titulo
        self.setWindowTitle("Instalador de paquetes principales")

        # Conectando los RadioButtons
        self.radioButton.toggled.connect(lambda: self.tipoInstalacion(self.radioButton))
        self.radioButton_2.toggled.connect(lambda: self.tipoInstalacion(self.radioButton_2))
        self.radioButton_3.toggled.connect(lambda: self.tipoInstalacion(self.radioButton_3))

    def instalarWeb(self):

        ventana = DialogWindowWeb().exec_()

    def instalarDesktop(self):

        ventana = DialogWindowDesktop().exec_()

    def instalarIA(self):

        ventana = DialogWindowIA().exec_()

    def tipoInstalacion(self, opcion):

        # Desarrollo Web
        if opcion.text() == "Web":
            if opcion.isChecked():
                self.pushButton.clicked.connect(self.instalarWeb)

        # Desarrollo Desktop
        elif opcion.text() == "Desktop":
            if opcion.isChecked():
                self.pushButton.clicked.connect(self.instalarDesktop)

        # Desarrollo IA
        elif opcion.text() == "IA":

            if self.radioButton_3.isChecked():
                self.pushButton.clicked.connect(self.instalarIA)


class DialogWindowWeb(QtWidgets.QDialog, Ui_Dialog):

    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)

        # Cambiando el titulo
        self.setWindowTitle("Instalar paquetes para el Desarrollo Web")

        # Agregando funciones a los botones
        self.buttonBox.accepted.connect(self.crear)
        self.buttonBox.rejected.connect(self.salirWeb)

    def crear(self):
        os.system("python -m pip install pipenv")

        # Luego de instalar pipenv

        os.system("pipenv --three")

        os.system("pipenv install django psycopg2 pillow")

        os.system("pipenv lock -r > requirements.txt")

        os.system("pipenv lock -r -d > dev-requirements.txt")

    def salirWeb(self):
        self.close()


class DialogWindowDesktop(QtWidgets.QDialog, Ui_Dialog):

    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)

        # Cambiando el titulo
        self.setWindowTitle("Instalar paquetes para el Desarrollo de Escritorio")

        # Agregando funciones a los botones
        self.buttonBox.accepted.connect(self.crear)
        self.buttonBox.rejected.connect(self.salirDesktop)

    def crear(self):
        os.system("python -m pip install pipenv")

        # Luego de instalar pipenv

        os.system("pipenv --three")

        os.system("pipenv install pyqt5 pillow pyinstaller canvas")

        os.system("pipenv lock -r > requirements.txt")

        os.system("pipenv lock -r -d > dev-requirements.txt")

    def salirDesktop(self):
        self.close()


class DialogWindowIA(QtWidgets.QDialog, Ui_Dialog):

    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)

        # Cambiando el titulo
        self.setWindowTitle("Instalar paquetes para el Desarrollo de IA")

        # Agregando funciones a los botones
        self.buttonBox.accepted.connect(self.activate)

        self.buttonBox.rejected.connect(self.salirIA)

    def activate(self):

        DialogWindowWait().exec_()
        #os.system("python -m pip install pipenv")

        subprocess.run(['python', '-m', 'pip', 'install', 'pipenv'])

        # Luego de instalar pipenv
        subprocess.run(['pipenv', '--tree'])
        # os.system("pipenv --three")

        subprocess.run(['pipenv', 'install', 'numpy', 'matplotlib', 'pandas'])
        # os.system("pipenv install numpy pandas matplotlib")

        subprocess.run['pipenv', 'lock', '-r', '>', 'requirements.txt']
        # os.system("pipenv lock -r > requirements.txt")

        subprocess.run(['pipenv', 'lock', '-r', '-d', '>', 'dev-requirements.txt'])
        # os.system("pipenv lock -r -d > dev-requirements.txt")

        if subprocess.CompletedProcess() != -N:




    def salirIA(self):
        self.close()



class DialogWindowWait(QtWidgets.QDialog, WaitWindow):

    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)

        # Cambiando el titulo
        self.setWindowTitle("Instalando")


if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    window = MainWindow()

    window.show()

    app.exec_()
