import sys
sys.path.append('../frontend')
sys.path.append('../backend')
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow
from frontend.main_frontend import Ui_RootFinder
from backend.roots_backend import RootsDialog
from sympy import * 

class RootFinder(QMainWindow):
    def __init__(self):
        super().__init__()
        self.expr = ''
        self.ui = Ui_RootFinder()
        self.ui.setupUi(self)
        for button in self.ui.buttonGroup.buttons():
            button.clicked.connect(self.add_value)
        self.ui.dltBtn.clicked.connect(self.backspace)
        self.ui.FndBtn.clicked.connect(self.find_roots)
        
    def add_value(self):
        self.ui.equation.setText(self.ui.equation.text() + self.sender().text())
        if self.sender().text() == '^':
            self.expr += '**'
        else:
            self.expr += self.sender().text()
        if self.sender().text() == 'sin' or self.sender().text() == 'cos':
            self.ui.equation.setText(self.ui.equation.text() + '(')
            self.expr += '('
        if self.sender().text() == 'e':
            self.ui.equation.setText(self.ui.equation.text() + '^')
            self.expr += '**'

    def backspace(self):
        self.ui.equation.setText(self.ui.equation.text()[:-1])

    def find_roots(self):
        print(self.expr) 
        dlg = RootsDialog(self)
        dlg.exec()
        
        

