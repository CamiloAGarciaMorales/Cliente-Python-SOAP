# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUIListarJugadores.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ListarJugadores(object):
    def setupUi(self, ListarJugadores):
        ListarJugadores.setObjectName("ListarJugadores")
        ListarJugadores.resize(892, 548)
        self.centralwidget = QtWidgets.QWidget(ListarJugadores)
        self.centralwidget.setObjectName("centralwidget")
        self.tbListaJugadores = QtWidgets.QTableWidget(self.centralwidget)
        self.tbListaJugadores.setGeometry(QtCore.QRect(10, 40, 861, 411))
        self.tbListaJugadores.setObjectName("tbListaJugadores")
        self.tbListaJugadores.setColumnCount(0)
        self.tbListaJugadores.setRowCount(0)
        self.btnListar = QtWidgets.QPushButton(self.centralwidget)
        self.btnListar.setGeometry(QtCore.QRect(380, 480, 93, 28))
        self.btnListar.setObjectName("btnListar")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(390, 10, 101, 21))
        self.label.setObjectName("label")
        ListarJugadores.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(ListarJugadores)
        self.statusbar.setObjectName("statusbar")
        ListarJugadores.setStatusBar(self.statusbar)

        self.retranslateUi(ListarJugadores)
        QtCore.QMetaObject.connectSlotsByName(ListarJugadores)

    def retranslateUi(self, ListarJugadores):
        _translate = QtCore.QCoreApplication.translate
        ListarJugadores.setWindowTitle(_translate("ListarJugadores", "Listar Jugadores"))
        self.btnListar.setText(_translate("ListarJugadores", "Listar"))
        self.label.setText(_translate("ListarJugadores", "Lista Jugadores"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ListarJugadores = QtWidgets.QMainWindow()
    ui = Ui_ListarJugadores()
    ui.setupUi(ListarJugadores)
    ListarJugadores.show()
    sys.exit(app.exec_())
