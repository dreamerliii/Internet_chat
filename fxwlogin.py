import pymysql

class Fxw:
    def fxwLogin(self, name1, pwd1):

        #import login1

        '''login = login1.Login1_Dialog()
        name = login.textEdit.toPlainText()
        pwd = login.textEdit_2.toPlainText()'''
        name = name1
        pwd = pwd1

        conn = pymysql.connect(host = '62.234.14.145', user = 'fxw', passwd = 'fxw666', db = 'chat', port = 3306)

        sql = "select password from users where id="+ name
        cus1 = conn.cursor()
        cus1.execute(sql)
        psw = cus1.fetchall()
        if psw == ():
            print("用户名错误")
            return 0
        elif psw[0][0] == pwd:
            print("登陆成功")
            return 1
        else:
            print("密码错误")
            return 2
        conn.commit()
        cus1.close()
        conn.close()



