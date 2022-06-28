from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import QtGui
from PyQt5.QtCore import Qt
import sys
import webbrowser
import os
from LC3 import LC3

class MyWindow(QWidget):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setGeometry(200, 200, 800, 400)
        self.setMinimumSize(500, 300)
        self.setWindowTitle("LC3 Simulator")
        self.initUI()
        self.menuUI()
        print("LC3 Simulator")

    def menuUI(self):
        self.myQMenuBar = QMenuBar(self)
        self.myQMenuBar.setGeometry(0, 0, 120, 20)
        fileMenu = self.myQMenuBar.addMenu('File')
        editMenu = self.myQMenuBar.addMenu('Edit')
        helpMenu = self.myQMenuBar.addMenu('Help')

        #File menu
        self.saveAction = QAction(self)
        self.saveAction.setText("Save")
        self.saveAction.setShortcut("Ctrl+S")
        self.saveAction.triggered.connect(lambda: self.SaveFiles())
        fileMenu.addAction(self.saveAction)

        self.openAction = QAction(self)
        self.openAction.setText("Open")
        self.openAction.triggered.connect(lambda: self.OpenFile())
        fileMenu.addAction(self.openAction)

        #Edit menu
        self.runallAction = QAction(self)
        self.runallAction.setText("Run all")
        self.runallAction.setShortcut("Ctrl+R")
        self.runallAction.triggered.connect(lambda: self.RunAll())
        editMenu.addAction(self.runallAction)

        self.runstepAction = QAction(self)
        self.runstepAction.setText("Run step")
        self.runstepAction.setShortcut("Ctrl+E")
        self.runstepAction.triggered.connect(lambda: self.RunStep())
        editMenu.addAction(self.runstepAction)

        self.resetAction = QAction(self)
        self.resetAction.setText("Reset")
        self.resetAction.setShortcut("Ctrl+Z")
        self.resetAction.triggered.connect(lambda: self.Reset())
        editMenu.addAction(self.resetAction)

        #Help menu
        self.githubAction = QAction(self)
        self.githubAction.setText("GitHub")
        self.githubAction.triggered.connect(lambda: self.GitHubLink())
        helpMenu.addAction(self.githubAction)

        self.samplecodeAction = QAction(self)
        self.samplecodeAction.setText("Insert sample code")
        self.samplecodeAction.triggered.connect(lambda: self.InsertSampleCode())
        helpMenu.addAction(self.samplecodeAction)

    #window elements (button, label)
    def initUI(self):
        self.lc3 = LC3()
        font = "Bahnschrift"

        #Label For Sitting Background Color or Image
        self.bglabel = QtWidgets.QLabel(self)
        self.bglabel.setGeometry(0,0,1920,1080)
        self.bglabel.setStyleSheet("background-color:light gray")

        # User coding area
        self.code_area = QtWidgets.QTextEdit(self)
        self.code_area.setStyleSheet("border:2px solid black; color:black")
        self.code_area.setFont(QFont("Courier", 12))
        self.code_area.setText(".ORIG x0000\n;Sample code\nADD R1, R1, #1\nADD R2, R2, #2\n.END")

        # Print instructions
        self.instr_label = QtWidgets.QLabel(self)
        self.instr_label.setText("0| [.ORIG X0000]")
        self.instr_label.setFont(QFont("Courier", 8))
        self.instr_label.setAlignment(Qt.AlignTop)
        self.instr_label.setStyleSheet("border:2px solid black; color:black")
        self.instr_label.setWordWrap(True)

        # Print machine code
        self.binary_label = QtWidgets.QLabel(self)
        self.binary_label.setText(self.lc3.getMahcinecode())
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

        # Reset button
        self.reset_button = QtWidgets.QPushButton(self)
        self.reset_button.setText("Reset")
        self.reset_button.setFont(QFont(font, 12))
        self.reset_button.clicked.connect(self.Reset)

        #Window Layout

        sub_sub_layout = QHBoxLayout()
        sub_sub_layout.addWidget(self.reset_button, 0)
        sub_sub_layout.addWidget(self.runStep_button, 0)
        sub_sub_layout.addWidget(self.runAll_button, 0)

        sub_layout = QVBoxLayout()
        sub_layout.addWidget(self.code_area, 2)
        sub_layout.addLayout(sub_sub_layout)

        layout = QHBoxLayout()
        layout.setContentsMargins(10, 30, 10, 10)
        layout.addLayout(sub_layout, 2)
        layout.addWidget(self.instr_label, 0)
        layout.addWidget(self.binary_label, 0)
        layout.addWidget(self.reg_label, 0)
        self.setLayout(layout)

    def Reset(self):
        self.lc3.reset()
        self.reg_label.setText(self.lc3.getAllRegisters())
        self.instr_label.setText("0| [.ORIG X0000]")
        self.binary_label.setText(self.lc3.getMahcinecode())

    def RunAll(self):
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

    def SaveFiles(self):
        newpath = r'Save Files'
        if not os.path.exists(newpath):
            os.makedirs(newpath)

        f = open("Save Files\Save Code.asm", 'w')
        f.write(self.code_area.toPlainText())
        f.close()

        f = open("Save Files\Binary.txt", "w")
        f.write(self.lc3.getMahcinecode())
        f.close()

    def OpenFile(self):
        # TODO open assembly code from file
        return

    def GitHubLink(self):
        webbrowser.open('https://github.com/AnasMations/LC3-Simulator')
        return

    def InsertSampleCode(self):
        self.code_area.setText(".ORIG x0000\n;Sample code\nADD R1, R1, #1\nADD R2, R2, #2\n.END")

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
