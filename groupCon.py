# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'conversation.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtWidgets import QApplication, QTableWidgetItem, QTableWidget, QHeaderView, QAbstractItemView, QDialog
import datetime
import addFriend1
import main_Menu
import history
import pymysql
import client

db = pymysql.connect(host='62.234.14.145',user='fxw', passwd="fxw666", db='test',port=3306)
cursor = db.cursor()
cursor.execute("select * from user")
result = cursor.fetchall()


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
    def set_time(self, time):
        self.time = time
    def get_time(self):
        return self.time

class GroupCon_Dialog(QDialog):
    # 自定义信号
    mySignal = pyqtSignal(str)

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(700, 555)
        self.dialog = Dialog
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(330, 500, 81, 51))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(420, 500, 81, 51))
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 501, 411))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.tableWidget = QtWidgets.QTableWidget(self.verticalLayoutWidget)
        self.tableWidget.move(20, 20)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(1)
        #self.tableWidget.setRowCount(2)
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidget.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.horizontalHeader().setVisible(False)
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableWidget.setShowGrid(False)
        #self.tableWidget.show(self.displayInfo(1,2))
        self.verticalLayout.addWidget(self.tableWidget)
        '''此处添加从服务器传来的消息,第一行显示成员名字，发送时间，第二行显示消息，全都居左显示'''
        i=0
        while i<3:
            '''a=info.get_name() + info.get_time()
            b=info.get_infor()'''
            a='aaa'
            b='bbbb'
            #调用显示信息函数
            self.displayInfo(a,b)
            i+=1


        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(560, 420, 81, 71))
        self.pushButton.setObjectName("pushButton")
        self.listWidget = QtWidgets.QListWidget(Dialog)
        self.listWidget.setGeometry(QtCore.QRect(510, 0, 181, 411))
        self.listWidget.setObjectName("listWidget")



        '''此处添加动态生成群聊成员代码'''
        db = pymysql.connect(host='62.234.14.145', user='fxw', passwd="fxw666", db='test', port=3306)
        cursor = db.cursor()
        cursor.execute("select * from user")
        result = cursor.fetchall()
        for row in result:
            a = row[1]
            self.listWidget.addItem(a)
            #print(a)
        db.close()
        self.listWidget.itemClicked.connect(self.itemClicked)

        self.mySignal.connect(self.add)

        self.textEdit = QtWidgets.QTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(0, 420, 501, 71))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        self.textEdit.setFont(font)
        self.textEdit.setObjectName("textEdit")
        self.pushButton_4 = QtWidgets.QPushButton(Dialog)
        self.pushButton_4.setGeometry(QtCore.QRect(0, 500, 75, 51))
        self.pushButton_4.setObjectName("pushButton_4")


        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "群聊"))
        self.pushButton_2.setText(_translate("Dialog", "表情"))
        self.pushButton_2.clicked.connect(self.emojiButtonClicked)
        self.pushButton_3.setText(_translate("Dialog", "历史记录"))
        self.pushButton_3.clicked.connect(self.historyButtonClicked)
        self.label.setText(_translate("Dialog", "TextLabel"))
        #print(self.label)
        self.pushButton.setText(_translate("Dialog", "发送"))
        self.pushButton.clicked.connect(self.sendButtonClicked)
        self.textEdit.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Agency FB\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.pushButton_4.setText(_translate("Dialog", "返回"))
        self.pushButton_4.clicked.connect(self.gobackButton)

    '''此处为点击群聊成员，弹出成员信息，若点击加好友按钮，可加好友'''
    def itemClicked(self):
        form1 = QtWidgets.QDialog()
        #ui = addFriend1.AddFriend_Dialog()
        self.dlg = addFriend1.AddFriend_Dialog()
        self.dlg.setupUi(form1)
        form1.show()
        self.listWidget.setSelectionMode(QAbstractItemView.ExtendedSelection)
        www = self.listWidget.selectedItems()
        text = [i.text() for i in list(www)]
        name = text[0]
        # print(name)
        self.mySignal.emit(name)
        form1.exec_()

    def add(self, name):
        print(name)
        self.dlg.textBrowser_2.setText(name)

    '''此函数是发送信息按钮，需添加存入数据库功能'''
    def sendButtonClicked(self):
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

    '''显示群成员发送的消息'''
    def displayInfo(self, a, b):
        usert = a
        infor = b
        row = self.tableWidget.rowCount()
        self.tableWidget.insertRow(row)
        item1 = QTableWidgetItem(usert)
        item1.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
        item1.setTextAlignment(Qt.AlignLeft)
        self.tableWidget.setItem(row, 0, item1)
        row1 = self.tableWidget.rowCount()
        self.tableWidget.insertRow(row1)
        item2 = QTableWidgetItem(infor)
        item2.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
        item2.setTextAlignment(Qt.AlignLeft)
        self.tableWidget.setItem(row1, 0, item2)


    '''以下都不需要修改'''
    def emojiButtonClicked(self):
        '''表情按钮，点击按钮显示村的所有表情'''

    def historyButtonClicked(self):
        '''查看聊天记录功能'''
        form3 = QtWidgets.QDialog()
        ui = history.History_Dialog()
        ui.setupUi(form3)
        form3.show()
        form3.exec_()

    def gobackButton(self):
        self.dialog.close()
        '''form2 = QtWidgets.QDialog()
        ui = main_Menu.MainMenu_Dialog()
        ui.setupUi(form2)
        form2.show()
        form2.exec_()
        #self.dialog.show()'''

    def exit(self):
        self.dialog.close()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = QtWidgets.QDialog()
    gui = GroupCon_Dialog()
    gui.setupUi(widget)
    widget.show()
    sys.exit(app.exec_())