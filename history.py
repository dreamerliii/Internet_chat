# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'history.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication
import pymysql



class History_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(374, 554)
        self.listWidget = QtWidgets.QListWidget(Dialog)
        self.listWidget.setGeometry(QtCore.QRect(0, 0, 371, 551))
        self.listWidget.setObjectName("listWidget")

        '''此处是查看历史消息的功能，你可以单写函数，调用之，更加规范。群id从其他界面自己传'''
        db = pymysql.connect(host='62.234.14.145', user='fxw', passwd="fxw666", db='test', port=3306)
        cursor = db.cursor()
        cursor.execute("select * from user")
        result = cursor.fetchall()
        for row in result:
            a = row[1]
            b = row[2]
            self.listWidget.addItem(a)
            self.listWidget.addItem(b)
            print(a)
            print(b)
        db.close()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "聊天记录"))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = QtWidgets.QDialog()
    gui = History_Dialog()
    gui.setupUi(widget)
    widget.show()
    sys.exit(app.exec_())