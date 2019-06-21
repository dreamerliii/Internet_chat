# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'register1.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication

import login1
from fxwregister import Fsd

class Register:
    def set_name(self, name):
        self.name = name
    def get_name(self):
        return self.name
    def set_tel(self, tel):
        self.tel = tel
    def get_tel(self):
        return self.tel
    def set_pwd(self, pwd):
        self.pwd = pwd
    def get_pwd(self):
        return self.pwd
    def set_repwd(self, repwd):
        self.repwd = repwd
    def get_repwd(self):
        return self.repwd
    def set_sex(self, sex):
        self.sex = sex
    def get_sex(self):
        return self.sex

class Register_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(419, 391)
        self.dialog = Dialog
        self.horizontalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(70, 240, 271, 101))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.formLayoutWidget = QtWidgets.QWidget(Dialog)
        self.formLayoutWidget.setGeometry(QtCore.QRect(30, 60, 361, 181))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.label_4 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(11)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.label_5 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(11)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.textEdit = QtWidgets.QTextEdit(self.formLayoutWidget)
        self.textEdit.setObjectName("textEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.textEdit)
        self.textEdit_2 = QtWidgets.QTextEdit(self.formLayoutWidget)
        self.textEdit_2.setObjectName("textEdit_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.textEdit_2)
        self.textEdit_3 = QtWidgets.QTextEdit(self.formLayoutWidget)
        self.textEdit_3.setObjectName("textEdit_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.textEdit_3)
        self.textEdit_4 = QtWidgets.QTextEdit(self.formLayoutWidget)
        self.textEdit_4.setObjectName("textEdit_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.textEdit_4)
        self.textEdit_5 = QtWidgets.QTextEdit(self.formLayoutWidget)
        self.textEdit_5.setObjectName("textEdit_5")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.textEdit_5)
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(200, 10, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(24)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", "注册"))
        self.pushButton.clicked.connect(self.registerButtonClicked)
        self.pushButton_2.setText(_translate("Dialog", "返回"))
        self.pushButton_2.clicked.connect(self.gobackButtonClicked)
        self.label.setText(_translate("Dialog", "姓名："))
        self.label_2.setText(_translate("Dialog", "手机号："))
        self.label_3.setText(_translate("Dialog", "密码："))
        self.label_4.setText(_translate("Dialog", "重复密码："))
        self.label_5.setText(_translate("Dialog", "性别："))
        self.label_6.setText(_translate("Dialog", "注册"))


    def registerButtonClicked(self):
        '''实现注册功能，若注册成功/失败，提示注册成功/失败。跳转到mainMenu界面'''
        register = Register()
        register.set_name(self.textEdit.toPlainText())
        register.set_tel(self.textEdit_2.toPlainText())
        register.set_pwd(self.textEdit_3.toPlainText())
        register.set_repwd(self.textEdit_4.toPlainText())
        register.set_sex(self.textEdit_5.toPlainText())
        '''print(register.get_name())
        print(register.get_tel())
        print(register.get_pwd())
        print(register.get_repwd())
        print(register.get_sex())'''
        '''注册函数调用此方法，此函数接收注册函数发来的值，若注册成功，跳转到mainMenu界面，若失败提示注册失败并留在register界面'''
        flag = Fsd()
        r = flag.fsdRegister(register.get_name(), register.get_tel(),register.get_pwd(),register.get_sex(), register.get_repwd())
        print(r)
        if r == 1:
            self.dialog.close()
            form1 = QtWidgets.QDialog()
            ui = login1.Login1_Dialog()
            ui.setupUi(form1)
            form1.show()
            form1.exec_()
            # self.dialog.show()
        else:
            print("密码不一致")


    def gobackButtonClicked(self):
        #self.dialog.close()
        self.dialog.close()
        form2 = QtWidgets.QDialog()
        gui = login1.Login1_Dialog()
        gui.setupUi(form2)
        form2.show()
        form2.exec_()
        #self.dialog.show()

    '''def exit(self):
        self.dialog.close()'''

if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = QtWidgets.QDialog()
    register = Register_Dialog()
    register.setupUi(widget)
    widget.show()
    sys.exit(app.exec_())