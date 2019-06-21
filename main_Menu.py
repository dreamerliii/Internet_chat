# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_Menu.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

import sys

import pymysql
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QAbstractItemView, QDialog
from PyQt5.QtCore import Qt, pyqtSignal
import groupCon
import single_Con, create_Gruop, search_Group
import client


db = pymysql.connect(host='62.234.14.145',user='fxw', passwd="fxw666", db='test',port=3306)
cursor = db.cursor()
cursor.execute("select * from user")
result = cursor.fetchall()

class Uid:
    def set_uid(self, uid):
        #print(uid)
        self.uid = uid
        global id
        id = uid
    def get_uid(self):
        #print(self.uid)
        return self.uid


class MainMenu_Dialog(QDialog):
    # 自定义信号
    groupSignal = pyqtSignal(str)
    singleSignal = pyqtSignal(str)



    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(464, 585)
        self.dialog = Dialog
        self.gridLayoutWidget = QtWidgets.QWidget(Dialog)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, 461, 581))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")

        cli = client.DataBase()
        print("aaa")
        print("bbb")
        group = cli.find_group_name(id)

        #聊天列表
        self.listWidget = QtWidgets.QListWidget(self.gridLayoutWidget)
        self.listWidget.setObjectName("listWidget")
        self.gridLayout.addWidget(self.listWidget, 0, 0, 1, 1)
        for index, item in enumerate(group[0]):
            gid = str(group[0][index])
            gname = group[1][index]
            s = gname + "(" + gid + ")"
            self.listWidget.addItem(s)
            print("qqqq")

        self.listWidget.itemClicked.connect(self.conItemClicked)
        #self.listWidget.setContextMenuPolicy(Qt.CustomContextMenu)
        #self.listWidget.customContextMenuRequested[QtCore.QPoint].connect(self.listWidgetContext)
        self.groupSignal.connect(self.groupChat)

        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)

        #好友列表
        cli = client.DataBase()
        b = cli.find_friend(id)
        print(b)
        self.listWidget_2 = QtWidgets.QListWidget(self.gridLayoutWidget)
        self.listWidget_2.setObjectName("listWidget_2")
        self.gridLayout.addWidget(self.listWidget_2, 0, 1, 1, 1)
        for index, item in enumerate(b):
            print(item)
            c = cli.find_username(str(item))
            print(c)
            self.listWidget_2.addItem(c)
            print("qqqq")

        self.singleSignal.connect(self.singleChat)
        self.listWidget_2.itemClicked.connect(self.friendItemClicked)

        self.pushButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 2, 0, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 2, 1, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_2.setText(_translate("Dialog", "                                 好友"))
        self.label.setText(_translate("Dialog", "                                 信息"))
        self.pushButton.setText(_translate("Dialog", "加群"))
        self.pushButton.clicked.connect(self.joinGroupChat)
        self.pushButton_2.setText(_translate("Dialog", "建群"))
        self.pushButton_2.clicked.connect(self.createGroupChat)


    #跳转到groupCon界面
    def conItemClicked(self):
        #self.dialog.close()
        form1 = QtWidgets.QDialog()
        self.ui = groupCon.GroupCon_Dialog()
        self.ui.setupUi(form1)
        form1.show()
        self.listWidget.setSelectionMode(QAbstractItemView.ExtendedSelection)
        www = self.listWidget.selectedItems()
        text = [i.text() for i in list(www)]
        gname = text[0]
        print(gname)
        self.groupSignal.emit(gname)
        #form1.exec_()
        #self.dialog.show()

    def groupChat(self, gname):
        print(gname)
        self.ui.label.setText(gname)

    def friendItemClicked(self):
        #self.dialog.hide()
        form2 = QtWidgets.QDialog()
        self.sui = single_Con.SingleCon_Dialog()
        self.sui.setupUi(form2)
        form2.show()
        self.listWidget_2.setSelectionMode(QAbstractItemView.ExtendedSelection)
        www = self.listWidget_2.selectedItems()
        text = [i.text() for i in list(www)]
        sname = text[0]
        #print(dname)
        self.singleSignal.emit(sname)
        #form2.exec_()
        #self.dialog.show()

    def singleChat(self, sname):
        print(sname)
        self.sui.label.setText(sname)

    def listWidgetContext(self,item):
        item = self.listWidget.itemAt(5, 5)
        self.listWidget.removeItemWidget(self.listWidget.takeItem(self.listWidget.row(item)))
        '''popMenu = QtGui.QMenu()
        popMenu.addAction(QtGui.QAction(u'添加', self))
        popMenu.addAction(QtGui.QAction(u'删除', self))
        popMenu.addAction(QtGui.QAction(u'修改', self))

        popMenu.exec_(QtGui.QCursor.pos())'''

    def joinGroupChat(self):
        '''加入群聊功能'''
        form3 = QtWidgets.QDialog()
        self.sui = search_Group.SearchGroup_Dialog()
        self.sui.setupUi(form3)
        form3.show()
        form3.exec_()
        #self.dialog.show()

    def createGroupChat(self):
        '''创建群聊功能'''
        form4 = QtWidgets.QDialog()
        self.sui = create_Gruop.CreateGroup_Dialog()
        self.sui.setupUi(form4)
        form4.show()
        form4.exec_()

    def exit(self):
        self.dialog.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = QtWidgets.QDialog()
    gui = MainMenu_Dialog()
    gui.setupUi(widget)
    widget.show()
    sys.exit(app.exec_())