"""
还差一个socket类
"""
import json
import threading
import socket
import pymysql


class Receive:
    """
    消息接收类
    """

    @staticmethod
    def receive(connect):
        """
        接收信息
        功能：按循环顺序接收消息，时间，消息发送者信息，群组名称和要添加的好友的id(应使用多线程)
        uid;time;information;gid;add_uid;flag;
        **优先判断flag为1则为添加群聊，为2则为删除群聊，为3则为创建群聊
        flag为4：添加好友请求
        flag为5：添加好友成功反馈
        flag为6：删除好友
        flag为0：聊天
        flag为-1：登录
        flag为-2：登出
        :return:
        """
        deal = DealInformation()
        log = Log()
        sent = SentInformation()
        global con
        while True:
            # print(connect)
            # 收东西
            recv_data = connect.recv(1024)
            print(threading.current_thread())
            print(connect)
            # print('what：%s' % recv_data.decode())
            print("进来了")
            user = json.loads(recv_data.decode())
            uid = user['uid']
            print(user)
            print("conn" + str(connect))
            if user['flag'] == '-500':
                c = [uid, connect]
                con = con + [c]
                continue
            print(con)
            if user['flag'] == '1' or user['flag'] == '2' or user['flag'] == '3':
                deal.deal_group(user)
            elif user['flag'] == '0':  # 聊天
                print("连上了聊天")
                deal.deal_information(user)
            elif user['flag'] == '4':  # 添加好友请求
                deal.deal_new_friend(user)
            elif user['flag'] == '5':  # 添加好友成功反馈
                deal.deal_friend_feedback(user)
            elif user['flag'] == '6':  # 删除好友
                deal.deal_del_friend(user)
            elif user['flag'] == '10':  # 一对一单聊
                deal.deal_talk(user)
            elif user['flag'] == '-1':  # 登录
                log.log_in(user)
            elif user['flag'] == '-2':  # 登出
                iddd = user['u2id']
                user['u2id'] = user['uid']
                user['uid'] = iddd
                for i in range(len(con)):
                    if user['uid'] == con[i][0]:
                        sent.sent_information(user,)
        # return


class DealInformation:
    """
    消息处理类
    """

    @staticmethod
    def deal_talk(message):
        """
        好友单聊
        :param message:
        :return:
        """
        global con
        for i in range(len(con)):
            if message['u2id'] == con[i]:
                sent = SentInformation()
                sent.sent_information(message, con[i][1])
                print(message)

    @staticmethod
    def deal_information(message):
        """
        处理群聊消息
        功能：根据gid从数据库找到群聊中包含的用户
            对在线的用户：调用发送函数进行发送
            对离线的用户：先存储到数据库中
        :param message:
        :return:
        """
        # 数据库操作
        global con
        db = pymysql.connect(host='62.234.14.145', user='fxw', passwd="fxw666", db='chat', port=3306)
        cursor = db.cursor()
        print(message)
        cursor.execute("INSERT INTO `information`(`gid`, `time`, `information`, `uid`) " +
                       "VALUES (" + str(message['gid']) + "," + message['time'] + ",'" + message['information']
                       + "','" + str(message['uid']) + "')")
        cursor.execute("SELECT max(id) FROM information")
        inf = cursor.fetchall()
        for ro in inf:
            information_id = ro[0]
        cursor.execute("SELECT uid FROM group_member WHERE group_member.gid = " + str(message['gid']))
        # cursor.execute("SELECT ip,addr,users.id FROM users,group_member WHERE group_member.uid = users.id and group_member.gid = " + str(message['gid']))
        result = cursor.fetchall()
        for row in result:
            if row[0] != message['uid']:
                p = 0
                for i in range(len(con)):
                    p += 1
                    print("12312321" + str(row[0]))
                    print("werwer" + str(con[i][0]))
                    if str(row[0]) == str(con[i][0]):
                        print("我有ip")
                        sent = SentInformation()
                        # ip = row[0]
                        # addr = int(row[1])
                        sent.sent_information(message, con[i][1])
                        break
                    else:
                        if p == 1:
                            print(row[0])
                            cursor.execute(
                                "INSERT INTO `unsend_people`(`infrom_id`, `uid`) VALUES (" + str(
                                    information_id) + "," + str(row[0]) + ")")
        db.commit()
        db.close()
        return

    @staticmethod
    def deal_new_friend(message):
        """
        处理好友请求
        功能：根据add_uid找到好友ip
            根据uid找到username
            发送username，remark，time
        :param message:
        :return:
        """
        db = pymysql.connect(host='62.234.14.145', user='fxw', passwd="fxw666", db='chat', port=3306)
        cursor = db.cursor()
        cursor.execute("INSERT INTO `friends`(`uid`, `friendid`) VALUES (" + str(message['uid']) + "," + str(
            message['u2id']) + ")")
        db.commit()
        db.close()
        return
        """
        db = pymysql.connect(host='62.234.14.145', user='fxw', passwd="fxw666", db='chat', port=3306)
        cursor = db.cursor()
        cursor.execute("SELECT * FROM `friends` WHERE (uid = " + str(message['uid']) + " AND friendid = "
                       + str(message['u2id']) + ") OR (uid = " + str(message['uid']) + " AND friendid = " + str(message[
                           'u2id']) + ")")
        if cursor.fetchall():
            sent = SentInformation()
            message['flag'] = '-100'
            sent.sent_information(message)
        else:
            cursor.execute("INSERT INTO `groups`(`id`) VALUES ( '" + str(message['uid']) + "000000" + str(message['u2id']) + "')")
            cursor.execute(
                "INSERT INTO `group_member`(`gid`, `uid`) VALUES (" + str(message['uid']) + "000000" + str(message['u2id'])+ "," + str(message['uid']) + ")")
            cursor.execute(
                "INSERT INTO `group_member`(`gid`, `uid`) VALUES (" + str(message['uid']) + "000000" + str(message['u2id']) + "," + str(message['u2id']) + ")")
            cursor.execute("INSERT INTO `information`(`gid`, `time`, `information`, `uid`) " +
                           "VALUES (" + str(message['uid']) + "000000" + str(message['u2id']) + "," + message['time'] + ",'" + message['information']
                           + "'," + str(message['uid']) + ")")
            cursor.execute("SELECT max(id) FROM information")
            information_id = cursor.fetchall()
            for ros in information_id:
                iid = ros[0]
            cursor.execute("SELECT ip,addr FROM users WHERE id=" + str(message['u2id']))
            result = cursor.fetchall()
            for row in result:
                if row[0] is not '0':
                    print("加好友：我有ip" + row[0])
                    sent = SentInformation()
                    ip = row[0]
                    addr = int(row[1])
                    sent.sent_information(message, ip, addr)
                else:
                    cursor.execute(
                        "INSERT INTO `unsend_people`(`infrom_id`, `uid`) VALUES (" + str(iid) + "," + row[
                            2] + ")")
        db.commit()
        db.close()
        return
        """

    @staticmethod
    def deal_friend_feedback(message):
        """
        处理添加好友反馈
        功能：在双方好友数据库中添加相应信息
            创建一uid-add_uid为名字的聊天室
            不用判断在线与否，即便不在线，在用户登录时也会自动刷新
        :param message: uid:add_uid:
        :return:
        """
        db = pymysql.connect(host='62.234.14.145', user='fxw', passwd="fxw666", db='chat', port=3306)
        cursor = db.cursor()
        cursor.execute(
            "INSERT INTO `friends`(`uid`, `friendid`) VALUES (" + str(message['uid']) + "," + str(
                message['u2id']) + ")")
        cursor.execute("SELECT ip,addr FROM users WHERE id=" + str(message['uid']) + " OR id = " + str(message['uid']))
        result = cursor.fetchall()
        for row in result:
            if row[0] is not '0':
                print("加好友反馈：我有ip" + row[0])
                sent = SentInformation()
                ip = row[0]
                addr = int(row[1])
                sent.sent_information(message, ip, addr)
        db.commit()
        db.close()
        return

    @staticmethod
    def deal_del_friend(message):
        """
        处理删除好友请求
        功能：将uid从双方好友数据库中删除
            删除一对一聊天室和所有聊天记录
        :param message: uid:add_uid:
        :return:
        """
        db = pymysql.connect(host='62.234.14.145', user='fxw', passwd="fxw666", db='chat', port=3306)
        cursor = db.cursor()
        cursor.execute(
            "DELETE FROM `friends` WHERE uid=" + str(message['uid']) + " OR friendid=" + str(message['u2id']))
        cursor.execute("SELECT ip,addr FROM users WHERE id=" + str(message['u2id']) + " OR id = " + str(message['uid']))
        result = cursor.fetchall()
        for row in result:
            if row[0] is not '0':
                print("加好友反馈：我有ip" + row[0])
                sent = SentInformation()
                ip = row[0]
                addr = int(row[1])
                sent.sent_information(message, ip, addr)
        db.commit()
        db.close()
        return

    @staticmethod
    def deal_group(message):
        """
        处理用户加入或退出群聊信息
        功能：将uid信息添加进/删除群聊用户数据库，并发送一个反馈至群聊所有成员，可以动态更新群聊成员
        :param message:
        :return:
        """
        global con
        db = pymysql.connect(host='62.234.14.145', user='fxw', passwd="fxw666", db='chat', port=3306)
        cursor = db.cursor()
        if message['flag'] is '3':  # 添加群聊或创建群聊
            cursor.execute("INSERT INTO `groups`(`name`) VALUES ( '" + message['information'] + "')")
            db.commit()
            cursor.execute("SELECT max(id) FROM groups")
            inf = cursor.fetchall()
            for ro in inf:
                idd = ro[0]
                message['gid'] = idd
            print(message['gid'])
            cursor.execute(
                "INSERT INTO `group_member`(`gid`, `uid`) VALUES (" + str(message['gid']) + "," + str(
                    message['uid']) + ")")
        elif message['flag'] is '1':
            cursor.execute(
                "INSERT INTO `group_member`(`gid`, `uid`) VALUES (" + str(message['gid']) + "," + str(
                    message['uid']) + ")")
        elif message['flag'] is '2':  # 删除群聊
            cursor.execute(
                "DELETE FROM `group_member` WHERE gid=" + str(message['gid']) + " AND uid=" + str(message['uid']))
        cursor.execute("SELECT uid FROM group_member WHERE group_member.gid = " + str(message['gid']))
        # cursor.execute("SELECT ip,addr,users.id FROM users,group_member WHERE group_member.uid = users.id and group_member.gid = " + str(message['gid']))
        db.commit()
        db.close()


class SentInformation:
    """
    发送消息至群聊
    只管发送，调用数据库应在其他函数进行
    消息，好友请求，好友添加成功反馈，群聊成员变动反馈, 发送失败反馈（已经是好友）
    """

    @staticmethod
    def sent_information(message, connect):
        """
        发送群聊消息
        功能：发送群聊消息给相应在线用户，修改conn信息为相应用户的conn即可
            应先发一个-1让客户收到为接收信号
        from_name:information:time:gid:
        :param message:
        :return:
        """
        # soc = socket.socket()
        # con = (ip, addr)
        # print(con)
        # soc.connect(con)
        """
        co=message['time']
        conn = json.loads(co)
        
        socket
        """
        print("sdfsf")
        json_string = json.dumps(message)
        connect.send(bytes(json_string, encoding='utf-8'))


class Log:
    """
    登录登出
    """

    def log_in(self, iip):
        """
        接收登录时客户端传过来的ip并写入数据库
        :param iip:
        :return:
        """

    def log_out(self, iip):
        """
        用户登出，接收传过来的id，从数据库中删除相应ip
        :param iip:
        :return:
        """


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip_port = ('127.0.0.1', 9999)
s = socket.socket()
s.bind(ip_port)
s.listen(5)
t = []
con = []
while True:
    conn, addr = s.accept()
    """
    if len(con) > 1:
        user = {'uid': 1, 'gid': 1, 'information': 'qweqe', 'u2id': None, 'flag': '0', 'time': 123}
        json_string = json.dumps(user)
        conn.send(json_string.encode(encoding="utf-8"))
    """
    t = t + [threading.Thread(target=Receive.receive, args=(conn,))]
    t[len(t) - 1].start()
