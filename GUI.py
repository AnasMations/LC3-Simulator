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
        self.setGeometry(200, 200, 700, 300)
        self.setWindowTitle("LC3 Simulator")
        self.initUI()

    #window elements (button, label)
    def initUI(self):

        font = "Bahnschrift"

        # User coding area
        self.code_area = QtWidgets.QTextEdit(self)
        self.code_area.setStyleSheet("border:2px solid black; color:black")
        self.code_area.setFont(QFont("Courier", 12))
        self.code_area.setText(";Sample code\nADD R5, R5, #1\n.END")
        self.code_area.setGeometry(150, 0, 300, 400)

        # Print register values
        self.reg_label = QtWidgets.QLabel(self)
        self.reg_label.setText("Result")
        self.reg_label.setFont(QFont(font, 14))
        self.reg_label.setAlignment(Qt.AlignTop)
        self.reg_label.setStyleSheet("border:2px solid black; color:black")
        self.reg_label.setWordWrap(True)

        self.runAll_button = QtWidgets.QPushButton(self)
        self.runAll_button.setText("Run all")
        self.runAll_button.clicked.connect(self.RunAll)

        self.runStep_button = QtWidgets.QPushButton(self)
        self.runStep_button.setText("Run step")
        #self.runStep_button.move(0, 200)
        self.runStep_button.clicked.connect(self.RunAll)

        #Window Layout

        sub_sub_layout = QHBoxLayout()
        sub_sub_layout.addWidget(self.runStep_button, 0)
        sub_sub_layout.addWidget(self.runAll_button, 0)

        sub_layout = QVBoxLayout()
        sub_layout.addWidget(self.code_area, 2)
        sub_layout.addLayout(sub_sub_layout)

        layout = QHBoxLayout()
        layout.addLayout(sub_layout, 2)
        layout.addWidget(self.reg_label, 0)
        self.setLayout(layout)

    def RunAll(self):
        # create object from our class LC3 and test on it
        test = LC3()
        #print(test.openFileToList("testing.txt"))
        #print(test.readStringToList("add r1, r1, #2\nadd r2, r0, r1\n.END"))
        print(test.readStringToList(self.code_area.toPlainText()))

        try:
            test.simulateAll()
            self.reg_label.setText( test.getAllRegisters() )
            self.reg_label.adjustSize()
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
