# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUIPrincipal.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from guiAgregarJugador import Ui_AgregarJugador
from guiAgregarPersonaje import Ui_AgregarPersonaje
from guiAgregarEspecie import Ui_AgregarEspecie
from guiEliminarJugador import Ui_EliminarJugador
from guiEliminarPersonaje import Ui_EliminarPersonaje
from guiEliminarEspecie import Ui_EliminarEspecie
from guiActualizarJugador import Ui_ActualizarJugador
from guiActualizarPersonaje import Ui_ActualizarPersonaje
from guiActualizarEspecie import Ui_ActualizarEspecie
from guiListarJugadores import Ui_ListarJugadores
from guiListarPersonajes import Ui_ListarPersonajes
from guiGraficar import Ui_GraficarTodo 



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        self.menuAGREGAR = QtWidgets.QMenu(self.menubar)
        self.menuAGREGAR.setObjectName("menuAGREGAR")
        self.menuEliminar = QtWidgets.QMenu(self.menubar)
        self.menuEliminar.setObjectName("menuEliminar")
        self.menuActualizar = QtWidgets.QMenu(self.menubar)
        self.menuActualizar.setObjectName("menuActualizar")
        self.menuListar = QtWidgets.QMenu(self.menubar)
        self.menuListar.setObjectName("menuListar")
        MainWindow.setMenuBar(self.menubar)
        self.actionAgregar_Jugador = QtWidgets.QAction(MainWindow)
        self.actionAgregar_Jugador.setObjectName("actionAgregar_Jugador")
        self.actionAgregar_Personaje = QtWidgets.QAction(MainWindow)
        self.actionAgregar_Personaje.setObjectName("actionAgregar_Personaje")
        self.actionAgregar_Especie = QtWidgets.QAction(MainWindow)
        self.actionAgregar_Especie.setObjectName("actionAgregar_Especie")
        self.actionEliminar_Jugador = QtWidgets.QAction(MainWindow)
        self.actionEliminar_Jugador.setObjectName("actionEliminar_Jugador")
        self.actionEliminar_Personaje = QtWidgets.QAction(MainWindow)
        self.actionEliminar_Personaje.setObjectName("actionEliminar_Personaje")
        self.actionEliminar_Especie = QtWidgets.QAction(MainWindow)
        self.actionEliminar_Especie.setObjectName("actionEliminar_Especie")
        self.actionActualizar_Jugador = QtWidgets.QAction(MainWindow)
        self.actionActualizar_Jugador.setObjectName("actionActualizar_Jugador")
        self.actionActualizar_Personaje = QtWidgets.QAction(MainWindow)
        self.actionActualizar_Personaje.setObjectName("actionActualizar_Personaje")
        self.actionActualizar_Especie = QtWidgets.QAction(MainWindow)
        self.actionActualizar_Especie.setObjectName("actionActualizar_Especie")
        self.actionListar_Jugadores = QtWidgets.QAction(MainWindow)
        self.actionListar_Jugadores.setObjectName("actionListar_Jugadores")
        self.actionListar_Personajes = QtWidgets.QAction(MainWindow)
        self.actionListar_Personajes.setObjectName("actionListar_Personajes")
        self.actionGraficar = QtWidgets.QAction(MainWindow)
        self.actionGraficar.setObjectName("actionGraficar")
        self.menuAGREGAR.addAction(self.actionAgregar_Jugador)
        self.menuAGREGAR.addAction(self.actionAgregar_Personaje)
        self.menuAGREGAR.addAction(self.actionAgregar_Especie)
        self.menuEliminar.addAction(self.actionEliminar_Jugador)
        self.menuEliminar.addAction(self.actionEliminar_Personaje)
        self.menuEliminar.addAction(self.actionEliminar_Especie)
        self.menuActualizar.addAction(self.actionActualizar_Jugador)
        self.menuActualizar.addAction(self.actionActualizar_Personaje)
        self.menuActualizar.addAction(self.actionActualizar_Especie)
        self.menuListar.addAction(self.actionListar_Jugadores)
        self.menuListar.addAction(self.actionListar_Personajes)
        self.menuListar.addAction(self.actionGraficar)
        self.menubar.addAction(self.menuAGREGAR.menuAction())
        self.menubar.addAction(self.menuEliminar.menuAction())
        self.menubar.addAction(self.menuActualizar.menuAction())
        self.menubar.addAction(self.menuListar.menuAction())
       
        self.actionAgregar_Jugador.triggered.connect(self.abrirAgreJugador)
        self.actionAgregar_Personaje.triggered.connect(self.abrirAgrePersonaje)
        self.actionAgregar_Especie.triggered.connect(self.abrirAgreEspecie)
        self.actionEliminar_Jugador.triggered.connect(self.abrirElemJugador)
        self.actionEliminar_Personaje.triggered.connect(self.abrirElemPersonaje)
        self.actionEliminar_Especie.triggered.connect(self.abrirElemEspecie)
        self.actionActualizar_Jugador.triggered.connect(self.abrirActuJugador)
        self.actionActualizar_Personaje.triggered.connect(self.abrirActuPersonaje)
        self.actionActualizar_Especie.triggered.connect(self.abrirActuEspecie)
        self.actionListar_Jugadores.triggered.connect(self.abrirListarJugadores)
        self.actionListar_Personajes.triggered.connect(self.abrirListarPersonajes)
        self.actionGraficar.triggered.connect(self.abrirGraficar)
        
        


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Principal"))
        self.menuAGREGAR.setTitle(_translate("MainWindow", "Agregar"))
        self.menuEliminar.setTitle(_translate("MainWindow", "Eliminar"))
        self.menuActualizar.setTitle(_translate("MainWindow", "Actualizar"))
        self.menuListar.setTitle(_translate("MainWindow", "Listar"))
        self.actionAgregar_Jugador.setText(_translate("MainWindow", "Agregar Jugador"))
        self.actionAgregar_Personaje.setText(_translate("MainWindow", "Agregar Personaje"))
        self.actionAgregar_Especie.setText(_translate("MainWindow", "Agregar Especie"))
        self.actionEliminar_Jugador.setText(_translate("MainWindow", "Eliminar Jugador"))
        self.actionEliminar_Personaje.setText(_translate("MainWindow", "Eliminar Personaje"))
        self.actionEliminar_Especie.setText(_translate("MainWindow", "Eliminar Especie"))
        self.actionActualizar_Jugador.setText(_translate("MainWindow", "Actualizar Jugador"))
        self.actionActualizar_Personaje.setText(_translate("MainWindow", "Actualizar Personaje"))
        self.actionActualizar_Especie.setText(_translate("MainWindow", "Actualizar Especie"))
        self.actionListar_Jugadores.setText(_translate("MainWindow", "Listar Jugadores"))
        self.actionListar_Personajes.setText(_translate("MainWindow", "Listar Personajes"))
        self.actionGraficar.setText(_translate("MainWindow", "Graficar"))

        #Metodos de conexion entre ventanas
    def abrirAgreJugador(self):
        self.guiAgregarJugador = QtWidgets.QMainWindow()
        self.ui = Ui_AgregarJugador()
        self.ui.setupUi(self.guiAgregarJugador)
        self.guiAgregarJugador.show()
    def abrirAgrePersonaje(self):
        self.guiAgregarPersonaje = QtWidgets.QMainWindow()
        self.ui = Ui_AgregarPersonaje()
        self.ui.setupUi(self.guiAgregarPersonaje)
        self.guiAgregarPersonaje.show()    
    def abrirAgreEspecie(self):
        self.guiAgregarEspecie = QtWidgets.QMainWindow()
        self.ui = Ui_AgregarEspecie()
        self.ui.setupUi(self.guiAgregarEspecie)
        self.guiAgregarEspecie.show()  
    def abrirElemJugador(self):
        self.guiEliminarJugador = QtWidgets.QMainWindow()
        self.ui = Ui_EliminarJugador()
        self.ui.setupUi(self.guiEliminarJugador)
        self.guiEliminarJugador.show()
    def abrirElemPersonaje(self):
        self.guiEliminarPersonaje = QtWidgets.QMainWindow()
        self.ui = Ui_EliminarPersonaje()
        self.ui.setupUi(self.guiEliminarPersonaje)
        self.guiEliminarPersonaje.show() 
    def abrirElemEspecie(self):
        self.guiEliminarEspecie = QtWidgets.QMainWindow()
        self.ui = Ui_EliminarEspecie()
        self.ui.setupUi(self.guiEliminarEspecie)
        self.guiEliminarEspecie.show()        
    def abrirActuJugador(self):
        self.guiActualizarJugador = QtWidgets.QMainWindow()
        self.ui = Ui_ActualizarJugador()
        self.ui.setupUi(self.guiActualizarJugador)
        self.guiActualizarJugador.show()
    def abrirActuPersonaje(self):
        self.guiActualizarPersonaje = QtWidgets.QMainWindow()
        self.ui = Ui_ActualizarPersonaje()
        self.ui.setupUi(self.guiActualizarPersonaje)
        self.guiActualizarPersonaje.show()
    def abrirActuEspecie(self):
        self.guiActualizarEspecie = QtWidgets.QMainWindow()
        self.ui = Ui_ActualizarEspecie()
        self.ui.setupUi(self.guiActualizarEspecie)
        self.guiActualizarEspecie.show()
    def abrirListarJugadores(self):
        self.guiListarJugadores = QtWidgets.QMainWindow()
        self.ui = Ui_ListarJugadores()
        self.ui.setupUi(self.guiListarJugadores)
        self.guiListarJugadores.show()
    def abrirListarPersonajes(self):
        self.guiListarPersonajes = QtWidgets.QMainWindow()
        self.ui = Ui_ListarPersonajes()
        self.ui.setupUi(self.guiListarPersonajes)
        self.guiListarPersonajes.show()   
    def abrirGraficar(self):
        self.guiGraficar = QtWidgets.QMainWindow()
        self.ui = Ui_GraficarTodo()
        self.ui.setupUi(self.guiGraficar)
        self.guiGraficar.show()      


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
