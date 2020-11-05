# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------
# Autor:	Cristian Cala Sierra

import sys
from PyQt5 import QtGui, QtWidgets
from PyQt5.QtGui import (QFont, QIcon, QPalette, QBrush, QColor, QPixmap, QRegion, QClipboard,
						 QRegExpValidator, QImage)
from PyQt5.QtCore import (Qt, QDir, pyqtSignal, QFile, QByteArray,QIODevice,QBuffer,QDate, QTime, QSize, QTimer, QRect, QRegExp, QTranslator,QLocale,
						  QLocale, QLibraryInfo, QFileInfo, QDir,QPropertyAnimation,QTranslator,QAbstractAnimation, QLocale)

from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QDialog, QTableWidget, QMenu, 
							 QTableWidgetItem, QAbstractItemView, QLineEdit, QPushButton,
							 QActionGroup, QAction, QMessageBox, QFrame, QStyle, QGridLayout,
							 QVBoxLayout, QHBoxLayout, QLabel, QToolButton, QGroupBox,
							 QDateEdit, QComboBox, QCheckBox, QTextEdit, QRadioButton, QScrollArea, QFileDialog,QGraphicsEffect, QVBoxLayout, 
							 QGraphicsDropShadowEffect, QGraphicsBlurEffect,)


class Interface(QMainWindow):
	def __init__(self, parent=None):
		QMainWindow.__init__(self)
		self.setWindowIcon(QIcon(""))
		self.setWindowTitle("G-Calculator")
		self.setWindowFlags(Qt.WindowTitleHint | Qt.WindowCloseButtonHint | Qt.WindowMinimizeButtonHint)
		self.setFixedSize(670, 650)
		self.setWindowFlags((Qt.FramelessWindowHint))
		self.setStyleSheet("QMainWindow{\n"
		"background-color: qlineargradient(spread:pad, x1:0.063, y1:0.346591, x2:0.982955, y2:0.477, stop:0 rgba(220,20,60,1), stop:1 rgba(102,0,0,1));\n"
		"border-radius: 22px;"
		"}\n"
		"")
		self.initUi()

	def initUi(self):
		# Stilos
		#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#
		frame = ("QFrame{\n"
				"color:#1b231f;\n"
				"background-color: rgba(255,255,255,0.8);\n"
				"border-radius: 22px;\n"
				"}")
		frame_2 = ("QFrame{\n"
				"color:#1b231f;\n"
				"background-color: rgba(255,255,255,1);\n"
				"border-radius: 10px;\n"
				"}")
		frame_3 = ("QFrame{\n"
				"color:#1b231f;\n"
				"background-color: rgba(0,0,0,0.8);\n"
				"border-radius: 10px;\n"
				"}")

		label_titulo = ("QLabel{\n"
				"color:rgb(24, 24, 24);\n"
				"}")

		botonCierre = ("QPushButton{\n"
						"border:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
						"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
						"color:rgb(255, 255, 255);\n"
						"}\n"
						"QPushButton:hover{\n"
						"background-color:rgb(255, 0, 0);\n"
						"color:rgb(255, 255, 255);\n"
						"}")

		botonStandar = ("QPushButton{\n"
						"border:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
						"background-color: rgba(255,255,255,1);\n"
						"border-radius: 10px;"
						"color:rgb(0, 0, 0);\n"
						"}\n"
						"QPushButton:hover{\n"
						"background-color:rgb(10, 0, 0);\n"
						"color:rgb(255, 255, 255);\n"
						"}")
		botonSpecial = ("QPushButton{\n"
						"border:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
						"background-color: rgba(207, 0, 89);\n"
						"border-radius: 10px;"
						"color:rgb(0, 0, 0);\n"
						"}\n"
						"QPushButton:hover{\n"
						"background-color:rgb(71,13,191);\n"
						"color:rgb(255, 255, 255);\n"
						"}")
#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#

		self.frame_principal = QFrame(self)
		self.frame_principal.setGeometry(QRect(30,120,610,500))
		self.frame_principal.setStyleSheet(frame)
		self.frame_principal.move(30, 100)

		# Label y frame del encabezado
		self.frame_titulo = QFrame(self)
		self.frame_titulo.setGeometry(QRect(30,30,135,50))
		self.frame_titulo.setStyleSheet(frame_2)
		self.frame_titulo.move(268,20)
		self.sombra_2 = QGraphicsDropShadowEffect()
		self.sombra_2.setBlurRadius(23)
		self.frame_titulo.setGraphicsEffect(self.sombra_2)

		self.Label = QLabel(self)
		self.Label.setGeometry(QRect(30,30,121,51))
		self.Label.setText("G-Calculator")
		self.Label.setStyleSheet(label_titulo)
		self.Label.setFont(QtGui.QFont("Lobster", 17, QtGui.QFont.Bold))
		self.Label.move(280, 20)
		self.sombra  = QGraphicsDropShadowEffect()        
		self.sombra.setBlurRadius(22)
		self.Label.setGraphicsEffect(self.sombra)

		self.botonCerrar = QPushButton(self)
		self.botonCerrar.setGeometry(QRect(30,30,40,30))
		self.botonCerrar.setIcon(QIcon("icons/close.svg"))
		self.botonCerrar.move(590,10)
		self.botonCerrar.setStyleSheet(botonCierre)

		self.botonMinimizar = QPushButton(self)
		self.botonMinimizar.setIcon(QIcon("icons/shuffle.svg"))
		self.botonMinimizar.setGeometry(QRect(30,30,30,30))
		self.botonMinimizar.move(560,10)
		self.botonMinimizar.setStyleSheet(botonCierre)

		self.acercaDe = QPushButton(self)
		self.acercaDe.setIcon(QIcon("icons/menu.svg"))
		self.acercaDe.setGeometry(QRect(30,30,30,30))
		self.acercaDe.move(10,10)
		self.acercaDe.setStyleSheet(botonCierre)

		# botones del contenido numérico#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#
		self.frame_pantalla = QFrame(self.frame_principal)
		self.frame_pantalla.setGeometry(QRect(40,40,520,120))
		self.frame_pantalla.setStyleSheet(frame_3)
		self.frame_pantalla.move(45, 10)
		self.sombra_3 = QGraphicsDropShadowEffect()
		self.sombra_3.setBlurRadius(22)
		self.frame_pantalla.setGraphicsEffect(self.sombra_3)

		self.boton_Nro1 = QPushButton(self.frame_principal)
		self.boton_Nro1.setGeometry(QRect(40,40,50,50))
		self.boton_Nro1.setStyleSheet(botonStandar)
		self.boton_Nro1.setFont(QtGui.QFont("Lobster", 14, QtGui.QFont.Bold))
		self.boton_Nro1.setText("1")
		self.boton_Nro1.move(45,160)
		self.sombra_4 = QGraphicsDropShadowEffect()
		self.sombra_4.setBlurRadius(22)
		self.boton_Nro1.setGraphicsEffect(self.sombra_4)

		self.boton_Nro2 = QPushButton(self.frame_principal)
		self.boton_Nro2.setGeometry(QRect(40,40,50,50))
		self.boton_Nro2.setStyleSheet(botonStandar)
		self.boton_Nro2.setFont(QtGui.QFont("Lobster", 14, QtGui.QFont.Bold))
		self.boton_Nro2.setText("2")
		self.boton_Nro2.move(110,160)
		self.sombra_5 = QGraphicsDropShadowEffect()
		self.sombra_5.setBlurRadius(22)
		self.boton_Nro2.setGraphicsEffect(self.sombra_5)

		self.boton_Nro3 = QPushButton(self.frame_principal)
		self.boton_Nro3.setGeometry(QRect(40,40,50,50))
		self.boton_Nro3.setStyleSheet(botonStandar)
		self.boton_Nro3.setFont(QtGui.QFont("Lobster", 14, QtGui.QFont.Bold))
		self.boton_Nro3.setText("3")
		self.boton_Nro3.move(175,160)
		self.sombra_6 = QGraphicsDropShadowEffect()
		self.sombra_6.setBlurRadius(22)
		self.boton_Nro3.setGraphicsEffect(self.sombra_6)	

		self.boton_Nro4 = QPushButton(self.frame_principal)
		self.boton_Nro4.setGeometry(QRect(40,40,50,50))
		self.boton_Nro4.setStyleSheet(botonStandar)
		self.boton_Nro4.setFont(QtGui.QFont("Lobster", 14, QtGui.QFont.Bold))
		self.boton_Nro4.setText("4")
		self.boton_Nro4.move(45,230)
		self.sombra_7 = QGraphicsDropShadowEffect()
		self.sombra_7.setBlurRadius(22)
		self.boton_Nro4.setGraphicsEffect(self.sombra_7)

		self.boton_Nro5 = QPushButton(self.frame_principal)
		self.boton_Nro5.setGeometry(QRect(40,40,50,50))
		self.boton_Nro5.setStyleSheet(botonStandar)
		self.boton_Nro5.setFont(QtGui.QFont("Lobster", 14, QtGui.QFont.Bold))
		self.boton_Nro5.setText("5")
		self.boton_Nro5.move(110,230)
		self.sombra_8 = QGraphicsDropShadowEffect()
		self.sombra_8.setBlurRadius(22)
		self.boton_Nro5.setGraphicsEffect(self.sombra_8)	

		self.boton_Nro6 = QPushButton(self.frame_principal)
		self.boton_Nro6.setGeometry(QRect(40,40,50,50))
		self.boton_Nro6.setStyleSheet(botonStandar)
		self.boton_Nro6.setFont(QtGui.QFont("Lobster", 14, QtGui.QFont.Bold))
		self.boton_Nro6.setText("6")
		self.boton_Nro6.move(175,230)
		self.sombra_9 = QGraphicsDropShadowEffect()
		self.sombra_9.setBlurRadius(22)
		self.boton_Nro6.setGraphicsEffect(self.sombra_9)

		self.boton_Nro7 = QPushButton(self.frame_principal)
		self.boton_Nro7.setGeometry(QRect(40,40,50,50))
		self.boton_Nro7.setStyleSheet(botonStandar)
		self.boton_Nro7.setFont(QtGui.QFont("Lobster", 14, QtGui.QFont.Bold))
		self.boton_Nro7.setText("7")
		self.boton_Nro7.move(45,300)
		self.sombra_10 = QGraphicsDropShadowEffect()
		self.sombra_10.setBlurRadius(22)
		self.boton_Nro7.setGraphicsEffect(self.sombra_10)

		self.boton_Nro8 = QPushButton(self.frame_principal)
		self.boton_Nro8.setGeometry(QRect(40,40,50,50))
		self.boton_Nro8.setStyleSheet(botonStandar)
		self.boton_Nro8.setFont(QtGui.QFont("Lobster", 14, QtGui.QFont.Bold))
		self.boton_Nro8.setText("8")
		self.boton_Nro8.move(110,300)
		self.sombra_11 = QGraphicsDropShadowEffect()
		self.sombra_11.setBlurRadius(22)
		self.boton_Nro8.setGraphicsEffect(self.sombra_11)

		self.boton_Nro9 = QPushButton(self.frame_principal)
		self.boton_Nro9.setGeometry(QRect(40,40,50,50))
		self.boton_Nro9.setStyleSheet(botonStandar)
		self.boton_Nro9.setFont(QtGui.QFont("Lobster", 14, QtGui.QFont.Bold))
		self.boton_Nro9.setText("9")
		self.boton_Nro9.move(175,300)
		self.sombra_12 = QGraphicsDropShadowEffect()
		self.sombra_12.setBlurRadius(22)
		self.boton_Nro9.setGraphicsEffect(self.sombra_12)

		self.boton_Point = QPushButton(self.frame_principal)
		self.boton_Point.setGeometry(QRect(40,40,50,50))
		self.boton_Point.setStyleSheet(botonStandar)
		self.boton_Point.setFont(QtGui.QFont("Lobster", 14, QtGui.QFont.Bold))
		self.boton_Point.setText(".")
		self.boton_Point.move(45,370)
		self.sombra_13 = QGraphicsDropShadowEffect()
		self.sombra_13.setBlurRadius(22)
		self.boton_Point.setGraphicsEffect(self.sombra_13)

		self.boton_Nro0 = QPushButton(self.frame_principal)
		self.boton_Nro0.setGeometry(QRect(40,40,50,50))
		self.boton_Nro0.setStyleSheet(botonStandar)
		self.boton_Nro0.setFont(QtGui.QFont("Lobster", 14, QtGui.QFont.Bold))
		self.boton_Nro0.setText("0")
		self.boton_Nro0.move(110,370)
		self.sombra_14 = QGraphicsDropShadowEffect()
		self.sombra_14.setBlurRadius(22)
		self.boton_Nro0.setGraphicsEffect(self.sombra_14)

		self.boton_Equal = QPushButton(self.frame_principal)
		self.boton_Equal.setGeometry(QRect(40,40,50,50))
		self.boton_Equal.setStyleSheet(botonSpecial)
		self.boton_Equal.setFont(QtGui.QFont("Lobster", 14, QtGui.QFont.Bold))
		self.boton_Equal.setText("=")
		self.boton_Equal.move(175,370)
		self.sombra_15 = QGraphicsDropShadowEffect()
		self.sombra_15.setBlurRadius(22)
		self.boton_Equal.setGraphicsEffect(self.sombra_15)

		self.boton_Clear = QPushButton(self.frame_principal)
		self.boton_Clear.setGeometry(QRect(40,40,50,50))
		self.boton_Clear.setStyleSheet(botonSpecial)
		self.boton_Clear.setFont(QtGui.QFont("Lobster", 14, QtGui.QFont.Bold))
		self.boton_Clear.setText("DEL")
		self.boton_Clear.move(250,160)
		self.sombra_16 = QGraphicsDropShadowEffect()
		self.sombra_16.setBlurRadius(22)
		self.boton_Clear.setGraphicsEffect(self.sombra_16)

		self.boton_Clear2 = QPushButton(self.frame_principal)
		self.boton_Clear2.setGeometry(QRect(40,40,50,50))
		self.boton_Clear2.setStyleSheet(botonSpecial)
		self.boton_Clear2.setFont(QtGui.QFont("Lobster", 14, QtGui.QFont.Bold))
		self.boton_Clear2.setText("Clear")
		self.boton_Clear2.move(315,160)
		self.sombra_17 = QGraphicsDropShadowEffect()
		self.sombra_17.setBlurRadius(22)
		self.boton_Clear2.setGraphicsEffect(self.sombra_17)

		self.boton_suma = QPushButton(self.frame_principal)
		self.boton_suma.setGeometry(QRect(40,40,50,50))
		self.boton_suma.setStyleSheet(botonStandar)
		self.boton_suma.setFont(QtGui.QFont("Lobster", 14, QtGui.QFont.Bold))
		self.boton_suma.setText("+")
		self.boton_suma.move(250,230)
		self.sombra_19 = QGraphicsDropShadowEffect()
		self.sombra_19.setBlurRadius(22)
		self.boton_suma.setGraphicsEffect(self.sombra_19)

		self.boton_Resta = QPushButton(self.frame_principal)
		self.boton_Resta.setGeometry(QRect(40,40,50,50))
		self.boton_Resta.setStyleSheet(botonStandar)
		self.boton_Resta.setFont(QtGui.QFont("Lobster", 14, QtGui.QFont.Bold))
		self.boton_Resta.setText("-")
		self.boton_Resta.move(315,230)
		self.sombra_20 = QGraphicsDropShadowEffect()
		self.sombra_20.setBlurRadius(22)
		self.boton_Resta.setGraphicsEffect(self.sombra_20)

		self.boton_Divide = QPushButton(self.frame_principal)
		self.boton_Divide.setGeometry(QRect(40,40,50,50))
		self.boton_Divide.setStyleSheet(botonStandar)
		self.boton_Divide.setFont(QtGui.QFont("Lobster", 14, QtGui.QFont.Bold))
		self.boton_Divide.setText("/")
		self.boton_Divide.move(250,300)
		self.sombra_21 = QGraphicsDropShadowEffect()
		self.sombra_21.setBlurRadius(22)
		self.boton_Divide.setGraphicsEffect(self.sombra_21)

		self.boton_X = QPushButton(self.frame_principal)
		self.boton_X.setGeometry(QRect(40,40,50,50))
		self.boton_X.setStyleSheet(botonStandar)
		self.boton_X.setFont(QtGui.QFont("Lobster", 14, QtGui.QFont.Bold))
		self.boton_X.setText("X")
		self.boton_X.move(315,300)
		self.sombra_18 = QGraphicsDropShadowEffect()
		self.sombra_18.setBlurRadius(22)
		self.boton_X.setGraphicsEffect(self.sombra_18)

		self.boton_parent = QPushButton(self.frame_principal)
		self.boton_parent.setGeometry(QRect(40,40,50,50))
		self.boton_parent.setStyleSheet(botonStandar)
		self.boton_parent.setFont(QtGui.QFont("Lobster", 14, QtGui.QFont.Bold))
		self.boton_parent.setText("(")
		self.boton_parent.move(250,370)
		self.sombra_19 = QGraphicsDropShadowEffect()
		self.sombra_19.setBlurRadius(22)
		self.boton_parent.setGraphicsEffect(self.sombra_19)

		self.boton_parent2 = QPushButton(self.frame_principal)
		self.boton_parent2.setGeometry(QRect(40,40,50,50))
		self.boton_parent2.setStyleSheet(botonStandar)
		self.boton_parent2.setFont(QtGui.QFont("Lobster", 14, QtGui.QFont.Bold))
		self.boton_parent2.setText(")")
		self.boton_parent2.move(315,370)
		self.sombra_20 = QGraphicsDropShadowEffect()
		self.sombra_20.setBlurRadius(22)
		self.boton_parent2.setGraphicsEffect(self.sombra_20)

		self.seno = QPushButton(self.frame_principal)
		self.seno.setGeometry(QRect(40,40,50,50))
		self.seno.setStyleSheet(botonStandar)
		self.seno.setFont(QtGui.QFont("Lobster", 14, QtGui.QFont.Bold))
		self.seno.setText("Sen")
		self.seno.move(390,160)
		self.sombra_21 = QGraphicsDropShadowEffect()
		self.sombra_21.setBlurRadius(22)
		self.seno.setGraphicsEffect(self.sombra_21)

		self.coseno = QPushButton(self.frame_principal)
		self.coseno.setGeometry(QRect(40,40,50,50))
		self.coseno.setStyleSheet(botonStandar)
		self.coseno.setFont(QtGui.QFont("Lobster", 14, QtGui.QFont.Bold))
		self.coseno.setText("Cos")
		self.coseno.move(450,160)
		self.sombra_22 = QGraphicsDropShadowEffect()
		self.sombra_22.setBlurRadius(22)
		self.coseno.setGraphicsEffect(self.sombra_22)

		self.tangente = QPushButton(self.frame_principal)
		self.tangente.setGeometry(QRect(40,40,50,50))
		self.tangente.setStyleSheet(botonStandar)
		self.tangente.setFont(QtGui.QFont("Lobster", 14, QtGui.QFont.Bold))
		self.tangente.setText("Tan")
		self.tangente.move(510,160)
		self.sombra_23 = QGraphicsDropShadowEffect()
		self.sombra_23.setBlurRadius(22)
		self.tangente.setGraphicsEffect(self.sombra_23)

		self.arcsen = QPushButton(self.frame_principal)
		self.arcsen.setGeometry(QRect(40,40,50,50))
		self.arcsen.setStyleSheet(botonStandar)
		self.arcsen.setFont(QtGui.QFont("Lobster", 12, QtGui.QFont.Bold))
		self.arcsen.setText("ArcSen")
		self.arcsen.move(390,220)
		self.sombra_24 = QGraphicsDropShadowEffect()
		self.sombra_24.setBlurRadius(22)
		self.arcsen.setGraphicsEffect(self.sombra_24)

		self.arccos = QPushButton(self.frame_principal)
		self.arccos.setGeometry(QRect(40,40,50,50))
		self.arccos.setStyleSheet(botonStandar)
		self.arccos.setFont(QtGui.QFont("Lobster", 12, QtGui.QFont.Bold))
		self.arccos.setText("ArcCos")
		self.arccos.move(450,220)
		self.sombra_25 = QGraphicsDropShadowEffect()
		self.sombra_25.setBlurRadius(22)
		self.arccos.setGraphicsEffect(self.sombra_25)

		self.arctang = QPushButton(self.frame_principal)
		self.arctang.setGeometry(QRect(40,40,50,50))
		self.arctang.setStyleSheet(botonStandar)
		self.arctang.setFont(QtGui.QFont("Lobster", 12, QtGui.QFont.Bold))
		self.arctang.setText("ArcTan")
		self.arctang.move(510,220)
		self.sombra_26 = QGraphicsDropShadowEffect()
		self.sombra_26.setBlurRadius(22)
		self.arctang.setGraphicsEffect(self.sombra_26)

		self.raiz = QPushButton(self.frame_principal)
		self.raiz.setGeometry(QRect(40,40,50,50))
		self.raiz.setStyleSheet(botonStandar)
		self.raiz.setText("ELpepe")
		self.raiz.move(390,280)
		self.sombra_27 = QGraphicsDropShadowEffect()
		self.sombra_27.setBlurRadius(22)
		self.raiz.setGraphicsEffect(self.sombra_27)

#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#

		
			
#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#
		# Eventos
		self.botonCerrar.clicked.connect(self.closeButton)
		self.botonMinimizar.clicked.connect(self.minimize)


	# Lógica#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#
	def closeButton(self):
		
		exit = QMessageBox(self)
		exit.setWindowTitle("¿Salir de VESOR?")
		exit.setIcon(QMessageBox.Question)
		exit.setText("¿Estás seguro que desea cerrar esta ventana?")
		buttonExit = exit.addButton("Salir", QMessageBox.YesRole)
		botonCancelar = exit.addButton("Cancelar", QMessageBox.NoRole)
            
		exit.exec_()
            
		if exit.clickedButton() == buttonExit:
			self.destroy()
		else:
			pass


	def minimize(self, event):
		self.setWindowState(Qt.WindowMinimized)

	def mousePressEvent(self, event):
		if event.button() == Qt.LeftButton:
			self.dragPosition = event.globalPos() - self.frameGeometry().topLeft()
			event.accept()

	def mouseMoveEvent(self, event):
		if event.buttons() == Qt.LeftButton:
			self.move(event.globalPos() - self.dragPosition)
			event.accept()


if __name__ == "__main__":
	app = QApplication(sys.argv)
	interface = Interface()
	interface.show()
	app.exec_()