from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import QtGui
from PyQt5.QtCore import Qt
import sys
from LC3 import LC3

class MyWindow(QWidget):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setGeometry(200, 200, 800, 400)
        self.setMinimumSize(500, 300)
        self.setWindowTitle("LC3 Simulator")
        self.initUI()

    #window elements (button, label)
    def initUI(self):
        self.lc3 = LC3()
        font = "Bahnschrift"

        # User coding area
        self.code_area = QtWidgets.QTextEdit(self)
        self.code_area.setStyleSheet("border:2px solid black; color:black")
        self.code_area.setFont(QFont("Courier", 12))
        self.code_area.setText(".ORIG x0000\n;Sample code\nADD R1, R1, #1\nADD R2, R2, #2\n.END")

        # Print instructions
        self.instr_label = QtWidgets.QLabel(self)
        self.instr_label.setFont(QFont("Courier", 8))
        self.instr_label.setAlignment(Qt.AlignTop)
        self.instr_label.setStyleSheet("border:2px solid black; color:black")
        self.instr_label.setWordWrap(True)

        # Print machine code
        self.binary_label = QtWidgets.QLabel(self)
        self.binary_label.setFont(QFont("Courier", 8))
        self.binary_label.setAlignment(Qt.AlignTop)
        self.binary_label.setStyleSheet("border:2px solid black; color:black")
        self.binary_label.setWordWrap(True)

        # Print register values
        self.reg_label = QtWidgets.QLabel(self)
        self.reg_label.setText(self.lc3.getAllRegisters())
        self.reg_label.setFont(QFont(font, 14))
        self.reg_label.setAlignment(Qt.AlignTop)
        self.reg_label.setStyleSheet("border:2px solid black; color:black")
        self.reg_label.setWordWrap(True)

        # Run buttons
        self.runAll_button = QtWidgets.QPushButton(self)
        self.runAll_button.setText("Run all")
        self.runAll_button.setFont(QFont(font, 12))
        self.runAll_button.clicked.connect(self.RunAll)

        self.runStep_button = QtWidgets.QPushButton(self)
        self.runStep_button.setText("Run step")
        self.runStep_button.setFont(QFont(font, 12))
        self.runStep_button.clicked.connect(self.RunStep)

        #Window Layout

        sub_sub_layout = QHBoxLayout()
        sub_sub_layout.addWidget(self.runStep_button, 0)
        sub_sub_layout.addWidget(self.runAll_button, 0)

        sub_layout = QVBoxLayout()
        sub_layout.addWidget(self.code_area, 2)
        sub_layout.addLayout(sub_sub_layout)

        layout = QHBoxLayout()
        layout.addLayout(sub_layout, 2)
        layout.addWidget(self.instr_label, 0)
        layout.addWidget(self.binary_label, 0)
        layout.addWidget(self.reg_label, 0)
        self.setLayout(layout)

    def RunAll(self):
        self.lc3.reset()
        self.lc3.readStringToList(self.code_area.toPlainText())

        try:
            self.lc3.simulateAll()
            self.reg_label.setText( self.lc3.getAllRegisters() )
            self.instr_label.setText( self.lc3.getInstructions() )
            self.binary_label.setText( self.lc3.getMahcinecode() )
        except:
            self.error_message()

    def RunStep(self):
        self.lc3.readStringToList(self.code_area.toPlainText())
        try:
            self.lc3.simulate()
            self.reg_label.setText( self.lc3.getAllRegisters() )
            self.instr_label.setText(self.lc3.getInstructions())
            self.binary_label.setText(self.lc3.getMahcinecode())
        except:
            self.error_message()

    def error_message(self):
        msg = QMessageBox()
        msg.setText("Synatx Error!")
        msg.setIcon(QMessageBox.Warning)

        x = msg.exec_()


def window():
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())

window()
