# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUIActualizarEspecie.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ActualizarEspecie(object):
    def setupUi(self, ActualizarEspecie):
        ActualizarEspecie.setObjectName("ActualizarEspecie")
        ActualizarEspecie.resize(495, 164)
        self.centralwidget = QtWidgets.QWidget(ActualizarEspecie)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(90, 40, 191, 22))
        self.lineEdit.setObjectName("lineEdit")
        self.btnActualizar = QtWidgets.QPushButton(self.centralwidget)
        self.btnActualizar.setGeometry(QtCore.QRect(310, 40, 93, 28))
        self.btnActualizar.setObjectName("btnActualizar")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(90, 20, 55, 16))
        self.label.setObjectName("label")
        self.btnBuscar = QtWidgets.QPushButton(self.centralwidget)
        self.btnBuscar.setGeometry(QtCore.QRect(310, 100, 93, 28))
        self.btnBuscar.setObjectName("btnBuscar")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(90, 80, 55, 16))
        self.label_2.setObjectName("label_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(90, 100, 191, 22))
        self.lineEdit_2.setObjectName("lineEdit_2")
        ActualizarEspecie.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(ActualizarEspecie)
        self.statusbar.setObjectName("statusbar")
        ActualizarEspecie.setStatusBar(self.statusbar)

           #Accion del boton
        self.btnActualizar.clicked.connect(self.updateEspecie)

        self.retranslateUi(ActualizarEspecie)
        QtCore.QMetaObject.connectSlotsByName(ActualizarEspecie)

    def retranslateUi(self, ActualizarEspecie):
        _translate = QtCore.QCoreApplication.translate
        ActualizarEspecie.setWindowTitle(_translate("ActualizarEspecie", "Actualizar Especie"))
        self.btnActualizar.setText(_translate("ActualizarEspecie", "Actualizar"))
        self.label.setText(_translate("ActualizarEspecie", "ID"))
        self.btnBuscar.setText(_translate("ActualizarEspecie", "Buscar"))
        self.label_2.setText(_translate("ActualizarEspecie", "Nombre"))

    def updateEspecie(self):
        ID = self.txtID.text()
        nom  = self.txtNombre.text()



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ActualizarEspecie = QtWidgets.QMainWindow()
    ui = Ui_ActualizarEspecie()
    ui.setupUi(ActualizarEspecie)
    ActualizarEspecie.show()
    sys.exit(app.exec_())
