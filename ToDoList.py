import sys
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QMessageBox

class ToDoList(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("ToDoList.ui",self)
        self.btnAgregar.clicked.connect(self.AgregarTarea)
        self.btnEliminar.clicked.connect(self.EliminarTarea)
        self.btnActualizar.clicked.connect(self.ActualizarTarea)

    def AgregarTarea(self):
        tarea = self.edtTarea.text()
        self.lstTareas.addItem(tarea)
        self.edtTarea.clear()
        self.edtTarea.setFocus()

    def EliminarTarea(self):
        indiceTareaBorrar = self.lstTareas.currentRow()
        self.lstTareas.takeItem(indiceTareaBorrar)

    def ActualizarTarea(self):
        indiceTareaActualizar = self.lstTareas.currentRow()
        nuevaTarea = self.edtTarea.text()
        self.lstTareas.item(indiceTareaActualizar).setText(nuevaTarea)
        self.edtTarea.clear()
        self.edtTarea.setFocus()
        



#hola este es mi codigo 1965 xd






        #indice = self.lstTareas.currentRow()
        #QMessageBox.information(self,"Notificacion",f"La tarea presionada es la que tiene el indice:{indice}")
