# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addFriend1.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QApplication
import groupCon


class Add:
    def set_id(self, id):
        self.id = id
    def get_id(self):
        return self.id
    def set_name(self, name):
        self.name = name
    def get_name(self):
        return self.name
    def set_sex(self, sex):
        self.id = id
    def get_sex(self):
        return self.sex

class AddFriend_Dialog(object):
    # 自定义信号
    #mySignal = pyqtSignal(str)

    def setupUi(self, Dialog):
        add = Add()
        '''从group1传来id，通过id从服务器中查找姓名和性别，并赋值给add.set_id(),add.set_name(),add.set_sex()'''

        Dialog.setObjectName("Dialog")
        Dialog.resize(404, 284)
        self.dialog = Dialog
        self.formLayoutWidget = QtWidgets.QWidget(Dialog)
        self.formLayoutWidget.setGeometry(QtCore.QRect(50, 70, 311, 101))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.textBrowser = QtWidgets.QTextBrowser(self.formLayoutWidget)
        self.textBrowser.setObjectName("textBrowser")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.textBrowser)
        # 从groupCon传来的账号（id）显示在textBrowser中
        #self.textBrowser.setText(add.get_id())

        self.textBrowser_2 = QtWidgets.QTextBrowser(self.formLayoutWidget)
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.textBrowser_2)
        #self.my = groupCon.GroupCon_Dialog()
        #self.my.mySignal.connect(self.add)
        # 在textBrowser_2中显示昵称（name）
        #self.textBrowser_2.setText(add.get_name())

        self.textBrowser_3 = QtWidgets.QTextBrowser(self.formLayoutWidget)
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.textBrowser_3)
        # 在textBrowser_3中显示性别（sex）
        #self.textBrowser_3.setText(add.get_sex())

        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(140, 200, 111, 41))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "账号："))
        self.label_2.setText(_translate("Dialog", "昵称："))
        self.label_3.setText(_translate("Dialog", "性别："))
        self.pushButton.setText(_translate("Dialog", "添加好友"))
        self.pushButton.clicked.connect(self.addFriendButton)

    '''def setName(self, name):
        self.textBrowser_2.clear()
        self.textBrowser_2.setText(name)'''

    '''def add(self,name):
        print(name)
        self.textBrowser_2.setText(name)'''

    '''def getDialogSignal(self, connect):
        self.textBrowser_2.setText(connect)
        print(self.textBrowser_2.toPlainText())'''

    def addFriendButton(self):
        '''添加好友功能'''

    def exit(self):
        self.dialog.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = QtWidgets.QDialog()
    aui = AddFriend_Dialog()
    aui.setupUi(widget)
    widget.show()
    sys.exit(app.exec_())