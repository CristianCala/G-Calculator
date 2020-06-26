import sys
from PyQt5 import QtGui
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

# Calculadora hecha por Cristian Cala


class Interface(QMainWindow):
	def __init__(self, parent=None):
		QMainWindow.__init__(self)
		self.setWindowIcon(QIcon(""))
		self.setWindowTitle("G-Calculator")
		self.setWindowFlags(Qt.WindowTitleHint | Qt.WindowCloseButtonHint | Qt.WindowMinimizeButtonHint)
		self.setFixedSize(750, 500)  
		self.setStyleSheet("QMainWindow{\n"
		"background-color: qlineargradient(spread:pad, x1:0.063, y1:0.346591, x2:0.982955, y2:0.477, stop:0 rgba(220,20,60,1), stop:1 rgba(102,0,0,1));\n"
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

		label_titulo = ("QLabel{\n"
				"color:rgb(24, 24, 24);\n"
				"}")

		self.sombra  = QGraphicsDropShadowEffect()        
		self.sombra.setBlurRadius(22)
#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#

		self.frame_principal = QFrame(self)
		self.frame_principal.setGeometry(QRect(30,120,690,410))
		self.frame_principal.setStyleSheet(frame)

		self.frame_titulo = QFrame(self)
		self.frame_titulo.setGeometry(QRect(30,30,135,50))
		self.frame_titulo.setStyleSheet(frame_2)
		self.frame_titulo.move(310,40)
		self.frame_titulo.setGraphicsEffect(self.sombra)


		self.Label = QLabel(self)
		self.Label.setGeometry(QRect(30,30,121,51))
		self.Label.setText("G-Calculator")
		self.Label.setStyleSheet(label_titulo)
		self.Label.setFont(QtGui.QFont("Lobster", 17, QtGui.QFont.Bold))
		self.Label.move(320, 40)

		self.Label.setGraphicsEffect(self.sombra)

if __name__ == "__main__":
	app = QApplication(sys.argv)
	interface = Interface()
	interface.show()
	app.exec_()