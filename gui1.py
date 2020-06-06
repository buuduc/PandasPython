import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import uic
import CPU

class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        uic.loadUi("mainwindow.ui", self)
        self.setFixedSize(320, 220)
        self.load_form()
    def load_form(self):
        self.BrowseDataSource_btn = self.findChild(QtWidgets.QPushButton, 'pushButton')
        self.BrowseDataSource_btn.clicked.connect(self.ClickBrowseDataSource)

        self.BrowseFileName_btn = self.findChild(QtWidgets.QPushButton, 'pushButton_2')
        self.BrowseFileName_btn.clicked.connect(self.ClickBrowseFileName)

        self.EditDataSource=self.findChild(QtWidgets.QLineEdit,"lineEdit_2")
        self.daylable = self.findChild(QtWidgets.QLineEdit, "lineEdit_3")

        self.EditFileName=self.findChild(QtWidgets.QLineEdit,"lineEdit")

        self.RUN=self.findChild(QtWidgets.QPushButton,'pushButton_3')
        self.RUN.clicked.connect(self.RunProgram)

        self.exit = self.findChild(QtWidgets.QPushButton, 'pushButton_4')
        self.exit.clicked.connect(sys.exit)s


    def ClickBrowseDataSource(self):
        filename=QtWidgets.QFileDialog.getOpenFileName()
        self.EditDataSource.setText(filename[0])
    def ClickBrowseFileName(self):
        filename=QtWidgets.QFileDialog.getOpenFileName()
        self.EditFileName.setText(filename[0])
        print(self.EditDataSource.text())
        return 1
    def RunProgram(self):
        print(self.daylable.text()=="08/05")
        CPU.ConvertData(self.daylable.text(),self.EditDataSource.text(),self.EditFileName.text(),"sadasdasd")
        # CPU.ConvertData('08/05', 'FileThongtinnhanvien.xlsx', 'Bang-cham-cong-[5-2020].xlsx',"CHecking")





app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()
