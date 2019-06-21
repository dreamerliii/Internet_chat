# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'requestOfFriend.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication

'''此功能是你提出，自己应该会，拜~~'''
class RequestOfFriend_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(444, 310)
        self.dialog = Dialog
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(70, 210, 111, 41))
        self.pushButton.setObjectName("pushButton")
        self.formLayoutWidget = QtWidgets.QWidget(Dialog)
        self.formLayoutWidget.setGeometry(QtCore.QRect(70, 40, 311, 121))
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
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.formLayoutWidget)
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.textBrowser_2)
        self.textBrowser_3 = QtWidgets.QTextBrowser(self.formLayoutWidget)
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.textBrowser_3)
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(260, 210, 111, 41))
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "好友请求"))
        self.pushButton.setText(_translate("Dialog", "同意"))
        self.pushButton.clicked.connect(self.okButtonClicked)
        self.label.setText(_translate("Dialog", "账号："))
        self.label_2.setText(_translate("Dialog", "昵称："))
        self.label_3.setText(_translate("Dialog", "性别："))
        self.pushButton_2.setText(_translate("Dialog", "拒绝"))
        self.pushButton_2.clicked.connect(self.cancleButtonClicked)

    def okButtonClicked(self):
        '''点击同意按钮，将好友加入好友列表'''

    def cancleButtonClicked(self):
        '''拒绝好友请求功能'''
        self.dialog.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = QtWidgets.QDialog()
    aui = RequestOfFriend_Dialog()
    aui.setupUi(widget)
    widget.show()
    sys.exit(app.exec_())