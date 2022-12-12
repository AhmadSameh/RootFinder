import sys
sys.path.append('../frontend')
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
        self.ui.equation.setEnabled(False)
        self.ui.equation.setStyleSheet('background-color: white; color: black;')
        
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
        self.expr = self.expr[:-1]

    def find_roots(self):
        lower_bound = higher_bound = first_guess = second_guess = None
        method = ''
        
        if self.ui.Eps.text() == '':
            self.ui.Eps.setStyleSheet('border: 1px solid red')
        else:
            self.ui.Eps.setStyleSheet('')
            eps = float(self.ui.Eps.text())

        if self.ui.MaxItt.text() == '':
            self.ui.MaxItt.setStyleSheet('border: 1px solid red')
        else:
            self.ui.MaxItt.setStyleSheet('')
            it_num = int(self.ui.MaxItt.text())
            
        for radio_button in self.ui.methodGroup.buttons():
            if radio_button.isChecked() and (radio_button.text() == 'Bisection' or radio_button.text() == 'False Position'):
                if self.ui.LowBnd.text() == '':
                    self.ui.LowBnd.setStyleSheet('border: 1px solid red')
                else:
                    self.ui.LowBnd.setStyleSheet('')
                if self.ui.HiBnd.text() == '':
                    self.ui.HiBnd.setStyleSheet('border: 1px solid red')
                else:
                    self.ui.HiBnd.setStyleSheet('')
                if self.ui.LowBnd.text() != '' and self.ui.HiBnd.text() != '':
                    lower_bound = float(self.ui.LowBnd.text())
                    higher_bound = float(self.ui.HiBnd.text())
                    method = radio_button.text()

            if radio_button.isChecked():
                final_expr = sympify(self.expr)
                dlg = RootsDialog(self.expr, method, eps, it_num, lower_bound, higher_bound, first_guess, second_guess, self)
                dlg.exec()

        return
        
        

