"""
其余未加功能：查看群聊成员，如果有人添加和退出能否动态更新，需要服务器传下来一个信号可以是只有gid其余全是-1
接收反馈，改相应数据库
应考虑一下发出很多该怎么处理
接收到相应反馈刷新
"""
import sys
import threading
import socket
import pymysql
import time
import json
import login1
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication

import groupCon

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
my_name = socket.getfqdn(socket.gethostname())
# 获取本机ip
ip = socket.gethostbyname(my_name)
print(ip)
s = socket.socket()


class Register:
    """
    登录注册
    注册没想好怎么写
    """

    def sendUid(self):
        lo = login1.Login1_Dialog()
        a = lo.textEdit.toPlainText()
        print(a)

    @staticmethod
    def sign_in(uid, password):
        """
        登录
        功能：对比数据库中信息，判断登录成功与否，应有提示
            登录时连接服务器，将自己的ip等信息发送给服务器
            将flag设为-1
            并找到自己未接收的消息
            创建线程
        :param uid:
        :param password:
        :return:
        """
        global s
        global ip
        # s.connect(ip_port)
        s.connect(('62.234.14.145', 9999))
        receive = Receive()
        t1 = threading.Thread(target=receive.receive, args=())
        t1.start()
        # 数据库连接
        db = pymysql.connect(host='62.234.14.145', user='fxw', passwd="fxw666", db='chat', port=3306)
        cursor = db.cursor()
        cursor.execute("UPDATE `users` SET `ip`=ip,`addr`=80 WHERE id = " + str(uid))
        db.commit()
        db.close()

    @staticmethod
    def sign_out(uid):
        """
        登出
        功能：登出时将连接服务器，将自己的ip等信息发送给服务器
            将flag设为-2
            关掉线程
        :param uid:
        :return:
        """
        db = pymysql.connect(host='62.234.14.145', user='fxw', passwd="fxw666", db='test', port=3306)
        cursor = db.cursor()
        cursor.execute("UPDATE `users` SET `ip`=0 WHERE id = " + uid)
        db.commit()
        db.close()
        s.close()
        exit()


class UserGroup:
    """
    群聊类
    flag默认为0，添加群聊标记为1，退出标记为2，创建标记为3
    """

    @staticmethod
    def join(uid, gid):
        """
        进入群聊
        功能：将新用户信息写入群聊表
            将flag设为1
        :param gid:
        :param uid:
        :return:
        """
        user = {'uid': uid, 'gid': gid, 'information': uid, 'u2id': None, 'flag': '1', 'time': None}
        sent = SentInformation()
        sent.sent_information(user)
        return

    @staticmethod
    def create(uid, group_name):
        """
        创建群聊
        功能：在群聊名称表插入新群信息
            创建者用户信息写入群聊表
            群聊id从10开始自增
            将flag设为3
        :param uid:
        :param group_name:
        :return:
        """
        user = {'uid': uid, 'gid': None, 'information': group_name, 'u2id': None, 'flag': '3', 'time': None}
        sent = SentInformation()
        sent.sent_information(user)
        return

    @staticmethod
    def speak(uid, information, gid):
        """
        在群聊中发言
        功能：上传群聊信息和发言人信息到服务器
            服务器对在线的人，将信息，时间和发言人id进行广播，从数据库找到在线人ip并发送
                对不在线的把联系人id，时间和聊天内容存入数据库
            时间在发送时获取系统时间
            将flag设为0
        :param uid:
        :param information: 发言信息
        :param gid: 群聊id
        :return: 上传成功与否
        """
        now = time.strftime('%Y.%m.%d', time.localtime(time.time()))
        user = {'uid': uid, 'gid': gid, 'information': information, 'u2id': None, 'flag': '0', 'time': "'" + now + "'"}
        sent = SentInformation()
        sent.sent_information(user)
        return

    @staticmethod
    def leave(uid, gid):
        """
        退出群聊
        功能：将用户信息从群聊表中删除
            如果是唯一用户，从群聊名称表中删除相应信息
            只有uid和gid没有information判定为退出群聊
            将flag设为2
        :param gid:
        :param uid:
        :return:
        """
        user = {'uid': uid, 'gid': gid, 'information': None, 'u2id': None, 'flag': '2', 'time': None}
        sent = SentInformation()
        sent.sent_information(user)
        return


class AddFriend:
    """
    添加好友类
    """

    @staticmethod
    def add_friend(remark, uid, add_uid):
        """
        主动添加朋友
        flag设为4
        :param remark:
        :param uid:
        :param add_uid:
        :return:
        """
        now = time.strftime('%Y.%m.%d', time.localtime(time.time()))
        user = {'uid': uid, 'gid': None, 'information': remark, 'u2id': add_uid, 'flag': '4', 'time': "'" + now + "'"}
        sent = SentInformation()
        sent.sent_information(user)
        return

    @staticmethod
    def added_friend(message):
        """
        是否同意添加好友
        :param message:
        :return:
        """
        answer = 0
        if answer == 1:  # 同意
            sent = SentInformation()
            message['flag'] = 5
            sent.sent_information(message)

    @staticmethod
    def del_friend(uid, del_uid):
        """
        删除朋友
        功能：将要自己的uid和要删除好友的uid均上传到服务器，之后双方数据库都删除
            flag设为6
        :param del_uid:
        :param uid:
        :return:
        """
        user = {'uid': uid, 'gid': None, 'information': None, 'u2id': del_uid, 'flag': '6', 'time': None}
        sent = SentInformation()
        sent.sent_information(user)
        return


class Chat:
    """
    一对一聊天类
    """

    @staticmethod
    def speak(uid, information, gid):
        """
        一对一聊天
        功能：同群聊speak函数功能
        :param uid:
        :param information:
        :param gid:聊天室id
        :return:发送是否成功
        """
        now = time.strftime('%Y.%m.%d', time.localtime(time.time()))
        user = {'uid': uid, 'gid': gid, 'information': information, 'u2id': None, 'flag': '0', 'time': "'" + now + "'"}
        sent = SentInformation()
        sent.sent_information(user)
        return


class Receive:
    """
    接收数据类
    调用类中函数时应先判断关键字gid的值，如果是0则调用ReceiveNewFriendInformation，非零则调用ReceiveInformation
    """

    @staticmethod
    def receive():
        """
        接收信息
        功能：按循环顺序接收消息，时间，消息发送者信息，群组名称和要添加的好友的id(应使用多线程)
        判断gid的值再选择不同函数
        uid;time;information;gid;add_uid;
        :return:
        """
        db = pymysql.connect(host='62.234.14.145', user='fxw', passwd="fxw666", db='chat', port=3306)
        cursor = db.cursor()

        soc = socket.socket()
        soc.bind(('127.0.0.1', 80))
        soc.listen()
        while True:
            conn, addr = soc.accept()
            while True:
                recv_data = conn.recv(1024)
                if recv_data:
                    print('what：%s' % recv_data.decode())
                    user = json.loads(recv_data.decode())
                    if user['flag'] is '4':  # 加好友请求
                        add_friend = AddFriend()
                        add_friend.added_friend(user)
                    elif user['flag'] is '5':  # 加好友成功反馈
                        cursor.execute("SELECT * FROM `friends` WHERE (uid = " + user['uid'] + " AND friendid = "
                                       + user['u2id'] + ") OR (uid = " + user['uid'] + " AND friendid = " +
                                       user['u2id'] + ")")
                        result = cursor.fetchall()
                        for row in result:
                            if row[0] is not '0':
                                print("刷新好友" + row[0])  # 用啥传啥
                                ######## 界面传
                        db.close()
                    elif user['flag'] is '2' or user['flag'] is '1':  # 创建删除群聊
                        cursor.execute("SELECT * FROM `group_member` WHERE uid=" + user['uid'])
                        result = cursor.fetchall()
                        for row in result:
                            if row[0] is not '0':
                                print("刷新好友" + row[0])  # 用啥传啥
                                ######## 界面传
                        db.close()
                    elif user['flag'] is '0':  # 发消息
                        deal = DealInformation()
                        deal.deal_information(user)


class DealInformation:
    """
    消息处理类
    """

    @staticmethod
    def deal_information(user):
        """
        处理聊天信息
        功能：将消息，时间，消息发送者信息，群组名称存储到本地数据库以便可以查看历史消息

        gid:uid: 发送者id;time: 时间;nformation:消息;information:聊天室id
        :param user:
        备注：为什么要不能一个uid确定gid，因为两个好友可能有不同群聊
            同样只有gid不知道是谁发的消息
        :return:
        """
        uid = user['uid']
        db = pymysql.connect(host = '62.234.14.145', user = 'fxw', passwd = 'fxw666', db = 'chat', port = 3306)
        cursor = db.cursor()
        cursor.execute("select name from users where id = " + user['uid'] + ",name='"+user['name']+"'")
        result = cursor.fetchall()
        db.close()
        time = user['time']
        info = user['information']

        '''group = groupCon.Infor()
        group.set_name(result)
        group.set_uid(uid)
        group.set_infor(info)
        group.set_time(time)'''

        print("界面")
        return

    @staticmethod
    def deal_new_friend_information(user):
        """
        接收添加好友请求
        功能：接收好友请求
            同意则双方数据库添加，自动建立一对一聊天室，该聊天室id命名以u1id-u2id方式命名主动添加的人认定为u1id
            返回时flag设为5
            拒绝则直接退出
        uid;remark;time;add_uid
        :return:
        """
        user['flag'] = '5'
        sent = SentInformation()
        sent.sent_information(user)
        return


class SentInformation:
    """
    发送消息类
    """

    @staticmethod
    def sent_information(message):
        """
        发送消息
        功能：上传消息到服务器
            获取系统时间yyyy-mm-dd hh:mm
        :param message: 接收整个数据字典
        :return:
        'uid': None, 'gid': None, 'information': None, 'u2id': None, 'flag': None, 'time': None,
        备注：不用写接收方id是因为可以通过gid找到想要的目标id
        """
        global s
        json_string = json.dumps(message)
        s.send(bytes(json_string, encoding='utf-8'))
        return


class DataBase:
    @staticmethod
    def find_username(uid):
        db = pymysql.connect(host='62.234.14.145', user='fxw', passwd="fxw666", db='chat', port=3306)
        cursor = db.cursor()
        cursor.execute("select name from users WHERE id = '" + uid + "'")
        result = cursor.fetchall()
        for row in result:
            print(row[0])
        db.close()
        return row[0]

    @staticmethod
    def find_group_member(gid):
        db = pymysql.connect(host='62.234.14.145', user='fxw', passwd="fxw666", db='chat', port=3306)
        cursor = db.cursor()
        cursor.execute(
            "SELECT name,users.id FROM group_member, users WHERE group_member.uid = users.id AND group_member.gid = '" + gid + "'")
        result = cursor.fetchall()
        for row in result:
            print(row[1])
        db.close()
        return result

    @staticmethod
    def find_friend(uid):
        print(uid)
        db = pymysql.connect(host='62.234.14.145', user='fxw', passwd="fxw666", db='chat', port=3306)
        cursor = db.cursor()
        cursor.execute("SELECT friendid FROM `friends` WHERE uid =  '" + uid + "'")
        result = cursor.fetchall()
        cursor.execute("SELECT uid FROM `friends` WHERE friendid ='" + uid + "'")
        result1 = cursor.fetchall()
        result = result + result1
        a = []
        for row in result:
            print(row[0])
            a.append(row[0])
        db.close()
        #print(a)
        return a

    @staticmethod
    def change_ip(uid):
        db = pymysql.connect(host='62.234.14.145', user='fxw', passwd="fxw666", db='chat', port=3306)
        cursor = db.cursor()
        cursor.execute("UPDATE `users` SET `ip`=ip,`addr`=80 WHERE id = '" + uid + "'")
        db.commit()
        db.close()

    @staticmethod
    def find_group_name(uid):
        db = pymysql.connect(host='62.234.14.145', user='fxw', passwd="fxw666", db='chat', port=3306)
        cursor = db.cursor()
        cursor.execute(
            "SELECT groups.id,groups.name FROM group_member,groups WHERE group_member.gid = groups.id AND group_member.uid = " + str(
                uid))
        result = cursor.fetchall()
        g_id = []
        gname = []
        for row in result:
            g_id.append(row[0])
            gname.append(row[1])
        db.close()
        answer = [g_id, gname]
        return answer


if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = QtWidgets.QDialog()
    log = login1.Login1_Dialog()
    log.setupUi(widget)
    widget.show()
    sys.exit(app.exec_())