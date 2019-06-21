# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login1.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QApplication, QDialog
import main_Menu
import register1
import client
from fxwlogin import Fxw



class Login:
    def set_id(self, id):
        self.id = id
    def get_id(self):
        return self.id
    def set_pwd(self, pwd):
        self.pwd = pwd
    def get_pwd(self):
        return self.pwd

class Login1_Dialog(QDialog):
    #自定义uid信号
    uidSignal = pyqtSignal(str)



    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(448, 306)
        self.dialog = Dialog
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(180, 40, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(100, 230, 71, 41))
        self.pushButton.setObjectName("pushButton")

        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(270, 230, 71, 41))
        self.pushButton_2.setObjectName("pushButton_2")

        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(50, 100, 41, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(360, 150, 61, 31))
        self.pushButton_3.setObjectName("pushButton_3")

        self.textEdit_2 = QtWidgets.QTextEdit(Dialog)
        self.textEdit_2.setGeometry(QtCore.QRect(100, 150, 241, 31))
        self.textEdit_2.setObjectName("textEdit_2")
        self.textEdit = QtWidgets.QTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(100, 90, 241, 31))
        self.textEdit.setObjectName("textEdit")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(50, 160, 41, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        #fxw = fxwlogin.Fxw()
        #self.uidSignal.connect(fxw.fxwLogin)

        #login = Login()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "聊天群"))
        self.pushButton.setText(_translate("Dialog", "登录"))
        self.pushButton.clicked.connect(self.loginButtonClicked)

        self.pushButton_2.setText(_translate("Dialog", "注册"))
        self.pushButton_2.clicked.connect(self.registerButtonClicked)
        self.label_2.setText(_translate("Dialog", "账号："))
        self.pushButton_3.setText(_translate("Dialog", "忘记密码"))
        self.pushButton_3.clicked.connect(self.findButtonClicked)
        self.label_3.setText(_translate("Dialog", "密码："))

    def loginButtonClicked(self):
        '''登录验证，若验证成功，跳转到mainMenu界面；若验证失败，提示登录失败'''
        login = Login()
        login.set_id(self.textEdit.toPlainText())
        login.set_pwd(self.textEdit_2.toPlainText())
        flag = Fxw()
        f = flag.fxwLogin(login.get_id(), login.get_pwd())
        if f == 1:
            uid = main_Menu.Uid()
            uid.set_uid(login.get_id())
            self.dialog.close()
            form1 = QtWidgets.QDialog()
            ui = main_Menu.MainMenu_Dialog()
           # ui.set_uid(login.get_id())
            ui.setupUi(form1)
            form1.show()

            form1.exec_()
        elif f == 2:
            print("密码错误！！！！！")

        else:
            print("用户不存在")



    '''def sendUid(self,uid):
        print(uid)'''



        #self.dialog.show()

    def registerButtonClicked(self):
        '''跳转到register界面'''
        self.dialog.close()
        form2 = QtWidgets.QDialog()
        rui = register1.Register_Dialog()
        rui.setupUi(form2)
        form2.show()
        form2.exec_()
        #self.dialog.show()

    def findButtonClicked(self):
        '''跳转到找回密码界面'''
        '''self.form.hide()
        form1 = QtWidgets.QDialog()
        ui = MainMenu_Dialog()
        ui.setupUi(form1)
        form1.show()
        form1.exec_()
        self.form.show()'''

    def exit(self):
        self.dialog.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = QtWidgets.QDialog()
    log = Login1_Dialog()
    log.setupUi(widget)
    widget.show()
    sys.exit(app.exec_())
