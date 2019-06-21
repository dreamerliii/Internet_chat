import pymysql

class Fsd:
    def fsdRegister(self, name1, tele1, password1, male1, rp_pwd1):
        while True:
            name = name1
            tele = tele1
            rp_pwd = rp_pwd1
            print(rp_pwd)
            password = password1
            print(password)
            male = male1
            print(type(male))
            if (password == rp_pwd):
                #print("qqq")
                break;
            else:
                #print("输错了！重新输入！")
                return 0

        try:
            conn = pymysql.connect(host='62.234.14.145', user='fxw', passwd='fxw666', db='chat', port=3306)
            cus1 = conn.cursor()
            res = [name, tele, password, male]
            sql = "insert into users(name,tele,password,male,addr) values ('"+ name +"','"+ tele +"','"+ password +"','"+ male +"','"+ "123" +"')"
            print(sql)
            print(res)
            cus1.execute(sql)
            conn.commit()
            cus1.close()
            conn.close()
        except Exception as e:
            print(e)
        else:
            print("新用户创建成功")

        return 1

