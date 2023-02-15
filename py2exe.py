import sys
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *
from ui_py2exe import Ui_MainWindow
import os
import PyInstaller.__main__


class py2exe(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setup()
        self.show()
        self.file1=None
        self.file2=None
        self.file3=None
    def reset(self):
        self.file1=None
        self.file2=None
        self.file3=None
        self.lb_1.setText(QCoreApplication.translate("MainWindow", u"file 1", None))
        self.lb_2.setText(QCoreApplication.translate("MainWindow", u"file 2(if have)", None))
        self.lb_3.setText(QCoreApplication.translate("MainWindow", u"not available", None))
        self.pbth_4.setText(QCoreApplication.translate("MainWindow", u"convert(make sure all file are in the same folder!)", None))

    def setup(self):
        self.pbtn_1.clicked.connect(self.select_file)
        self.pbtn_2.clicked.connect(self.select_file)
        self.pbtn_3.clicked.connect(self.error)
        self.pbth_4.clicked.connect(self.convert)
    def select_file(self):
        if self.file1 == None:
            self.file1 = QFileDialog.getOpenFileName(caption='choose file', filter='(*.py)')
            if self.file1[0]:
                self.lb_1.setText("file 1: {}".format(self.file1[0]))
            else:
                QMessageBox.warning(self, 'caution', 'please choose a file')
        elif self.file2==None:
            self.file2 = QFileDialog.getOpenFileName(caption='choose file', filter='(*.py)')
            if self.file2[0]:
                self.lb_2.setText("file 2: {}".format(self.file2[0]))
            else:
                QMessageBox.warning(self, 'caution', 'please choose a file')
        # elif self.file3==None:
        #     self.file3 = QFileDialog.getOpenFileName(caption='choose file', filter='(*.py)')
        #     if self.file3[0]:
        #         self.lb_3.setText("file 3: {}".format(self.file3[0]))
        #     else:
        #         QMessageBox.warning(self, 'caution', 'please choose a file')
        else:
            QMessageBox.warning(self, 'caution', 'you can only choose 3 files maximun')
    def convert(self):
        self.pbth_4.setText(QCoreApplication.translate("MainWindow", u"converting, please wait", None))
        conv_file=[]
        if self.file1:
            conv_file.append(self.file1[0])
        if self.file2:
            conv_file.append(self.file2[0])
        #if self.file3:
            #conv_file.append(self.file3[0])
        options = [
        '--onefile',
        ]
        os.chdir(os.path.dirname(conv_file[0]))
        PyInstaller.__main__.run(conv_file + options)
        QMessageBox.information(self, 'info', 'finished! Your file is in C:/Users/user/dist')
        self.reset()
    def error(self):
        QMessageBox.information(self, 'info', 'not available')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = py2exe()
    sys.exit(app.exec_())
