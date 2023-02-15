# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'py2exe.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(573, 314)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.pbth_4 = QPushButton(self.centralwidget)
        self.pbth_4.setObjectName(u"pbth_4")
        self.pbth_4.setGeometry(QRect(42, 230, 491, 28))
        self.pbtn_1 = QPushButton(self.centralwidget)
        self.pbtn_1.setObjectName(u"pbtn_1")
        self.pbtn_1.setGeometry(QRect(30, 50, 141, 28))
        self.pbtn_2 = QPushButton(self.centralwidget)
        self.pbtn_2.setObjectName(u"pbtn_2")
        self.pbtn_2.setGeometry(QRect(30, 110, 141, 28))
        self.pbtn_3 = QPushButton(self.centralwidget)
        self.pbtn_3.setObjectName(u"pbtn_3")
        self.pbtn_3.setGeometry(QRect(30, 170, 141, 28))
        self.lb_1 = QLabel(self.centralwidget)
        self.lb_1.setObjectName(u"lb_1")
        self.lb_1.setGeometry(QRect(190, 60, 361, 16))
        self.lb_2 = QLabel(self.centralwidget)
        self.lb_2.setObjectName(u"lb_2")
        self.lb_2.setGeometry(QRect(190, 120, 361, 16))
        self.lb_3 = QLabel(self.centralwidget)
        self.lb_3.setObjectName(u"lb_3")
        self.lb_3.setGeometry(QRect(190, 180, 361, 16))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"py2exe", None))
        self.pbth_4.setText(QCoreApplication.translate("MainWindow", u"convert(make sure all file are in the same folder!)", None))
        self.pbtn_1.setText(QCoreApplication.translate("MainWindow", u"choose", None))
        self.pbtn_2.setText(QCoreApplication.translate("MainWindow", u"choose", None))
        self.pbtn_3.setText(QCoreApplication.translate("MainWindow", u"not available", None))
        self.lb_1.setText(QCoreApplication.translate("MainWindow", u"file 1", None))
        self.lb_2.setText(QCoreApplication.translate("MainWindow", u"file 2(if have)", None))
        self.lb_3.setText(QCoreApplication.translate("MainWindow", u"not available", None))
    # retranslateUi

