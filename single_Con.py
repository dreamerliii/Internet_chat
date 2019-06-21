# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'single_Con.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QTableWidgetItem, QHeaderView, QDialog
from PyQt5.QtCore import Qt
import datetime
import main_Menu
import history

'''此一对一聊天窗口与群聊类似，可对比添加'''
class Infor:
    def set_uid(self, uid):
        self.uid = uid
    def get_uid(self):
        return self.uid
    def set_name(self, name):
        self.name = name
    def get_name(self):
        return self.name
    def set_infor(self, infor):
        self.infor = infor
    def get_infor(self):
        return self.infor

class SingleCon_Dialog(QDialog):

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(576, 559)
        self.dialog = Dialog
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(310, 500, 81, 51))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(400, 500, 71, 51))
        self.pushButton.setObjectName("pushButton")
        self.textEdit = QtWidgets.QTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(0, 420, 471, 71))
        self.textEdit.setObjectName("textEdit")
        self.pushButton_4 = QtWidgets.QPushButton(Dialog)
        self.pushButton_4.setGeometry(QtCore.QRect(0, 500, 81, 51))
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(1, 0, 571, 411))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.tableWidget = QtWidgets.QTableWidget(self.verticalLayoutWidget)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(1)
        #self.tableWidget.setRowCount(0)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.horizontalHeader().setVisible(False)
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableWidget.setShowGrid(False)
        self.verticalLayout.addWidget(self.tableWidget)

        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(480, 420, 86, 71))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_5 = QtWidgets.QPushButton(Dialog)
        self.pushButton_5.setGeometry(QtCore.QRect(90, 500, 81, 51))
        self.pushButton_5.setObjectName("pushButton_5")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "一对一"))
        self.pushButton_2.setText(_translate("Dialog", "表情"))
        self.pushButton_2.clicked.connect(self.emojiButtonClicked)
        self.pushButton.setText(_translate("Dialog", "历史记录"))
        self.pushButton.clicked.connect(self.historyButtonClicked)
        self.pushButton_4.setText(_translate("Dialog", "返回"))
        self.pushButton_4.clicked.connect(self.gobackButtonClicked)
        self.label.setText(_translate("Dialog", "TextLabel"))
        self.pushButton_3.setText(_translate("Dialog", "发送"))
        self.pushButton_3.clicked.connect(self.sendButtonClicked)
        self.pushButton_5.setText(_translate("Dialog", "删除"))
        self.pushButton_5.clicked.connect(self.deleteFriendButtonClicked)

    def emojiButtonClicked(self):
        '''查看表情'''

    def sendButtonClicked(self):
        '''发送信息功能'''
        if self.textEdit.toPlainText() != "":
            infor = Infor()
            infor.set_uid('111')
            infor.set_name('gg')
            user = {'Uid': infor.get_uid(), 'Name': infor.get_name()}
            utime = "%s %s" % (user['Name'], datetime.datetime.now())
            # QTableWidget.resizeColumnsToContents()
            # QTableWidget.resizeRowsToContents()
            row = self.tableWidget.rowCount()
            self.tableWidget.insertRow(row)
            item1 = QTableWidgetItem(utime)
            item1.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
            item1.setTextAlignment(Qt.AlignRight)
            self.tableWidget.setItem(row, 0, item1)
            row1 = self.tableWidget.rowCount()
            self.tableWidget.insertRow(row1)
            item2 = QTableWidgetItem(self.textEdit.toPlainText())
            item2.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
            item2.setTextAlignment(Qt.AlignRight)
            self.tableWidget.setItem(row1, 0, item2)

    def historyButtonClicked(self):
        '''查看聊天记录功能'''
        form3 = QtWidgets.QDialog()
        ui = history.History_Dialog()
        ui.setupUi(form3)
        form3.show()
        form3.exec_()

    def gobackButtonClicked(self):
        '''返回功能'''
        self.dialog.close()
        '''form2 = QtWidgets.QDialog()
        ui = main_Menu.MainMenu_Dialog()
        ui.setupUi(form2)
        form2.show()
        form2.exec_()'''

    def deleteFriendButtonClicked(self):
        '''删除好友功能'''

    def exit(self):
        self.dialog.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = QtWidgets.QDialog()
    sui = SingleCon_Dialog()
    sui.setupUi(widget)
    widget.show()
    sys.exit(app.exec_())