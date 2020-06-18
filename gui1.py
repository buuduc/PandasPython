import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import uic
import CPU
import os
import json

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
        self.exit.clicked.connect(sys.exit)
        self.CheckPathJson()
    def CheckPathJson(self):
        if os.path.isfile('PathData.jsol'):
            print("ton tai")
            with open('PathData.jsol', 'r', encoding='utf-8') as file:
                data=json.load(file)
                print(data)
                self.EditDataSource.setText(data['DataSource'])
                self.EditFileName.setText(data['FileName'])
                self.daylable.setText(data['day'])

    def ClickBrowseDataSource(self):
        filename=QtWidgets.QFileDialog.getOpenFileName()
        self.EditDataSource.setText(filename[0])
    def ClickBrowseFileName(self):
        filename=QtWidgets.QFileDialog.getOpenFileName()
        self.EditFileName.setText(filename[0])
        print(self.EditDataSource.text())
        return 1
    def RunProgram(self):
        # print(self.daylable.text()=="08/05")
        # CPU.ConvertData(self.daylable.text(),self.EditDataSource.text(),self.EditFileName.text(),"Test1206")
        # filename=QtWidgets.QFileDialog.getSaveFileName()


        # dd = QtWidgets.QApplication(sys.argv)
        # error=QtWidgets.QErrorMessage()
        # error.showMessage("Dữ liệu nhập vào không đúng")
        # dd.exec_()

        fname = QtWidgets.QFileDialog.getSaveFileName(self, "Chọn vị trí lưu kết quả", 'Ngay' + self.daylable.text()[0:2] + '-' + self.daylable.text()[3:5], "All File (*) ;; Excel File (*.xlsx)")
        if fname[0]!='':
            data = {}
            data['DataSource']=self.EditDataSource.text()
            data['FileName']=self.EditFileName.text()
            data['day']=self.daylable.text()
            with open('PathData.jsol', 'w',encoding='utf-8') as f:
                json.dump(data, f,ensure_ascii= False)
            try:
                CPU.ConvertData(self.daylable.text(), self.EditDataSource.text(), self.EditFileName.text(), fname[0])

            except:
                print("loi roi")
                msg = QtWidgets.QMessageBox()
                msg.setText("Dữ liệu nhập vào không đúng")
                msg.setWindowTitle("Lỗi!")
                msg.setIcon(QtWidgets.QMessageBox.Critical)
                # msg.setWindowIcon(QtWidgets.QMessageBox.Critical)
                msg.show()
                msg.exec_()
            else:
                msg = QtWidgets.QMessageBox()
                msg.setText("Xuất file thành công !")
                msg.setWindowTitle("Thành công!")
                msg.setIcon(QtWidgets.QMessageBox.Information)
                # msg.setWindowIcon(QtWidgets.QMessageBox.Critical)
                msg.show()
                msg.exec_()


        # CPU.ConvertData('08/05', 'FileThongtinnhanvien.xlsx', 'Bang-cham-cong-[5-2020].xlsx',"CHecking")





app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()
