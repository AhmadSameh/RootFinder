import sys
sys.path.append('../frontend')
from PyQt5.QtWidgets import QDialog, QTableWidgetItem
from frontend.roots_frontend import Ui_roots

class RootsDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_roots()    
        self.ui.setupUi(self)
        self.ui.IttTbl.setRowCount(1)
        self.ui.IttTbl.setItem(0, 0, QTableWidgetItem('0'))
        self.ui.IttTbl.setItem(0, 1, QTableWidgetItem('654'))
        self.ui.IttTbl.setItem(0, 2, QTableWidgetItem('789'))
