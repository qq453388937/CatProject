# -*- coding:utf-8 -*-
# import redis
import MysqlHelper
from hashlib import sha1


def main():
    try:
        user_name = raw_input("请输入用户名?")
        user_pwd = raw_input("请输入密码")
        sha1_model = sha1()
        sha1_model.update(user_pwd.encode())
        sha_pwd = sha1_model.hexdigest()  # 返回sha1加密结果
        r = MysqlHelper.RedisHelper()
        retpwd = r.get(user_name)  # redis nil python 表示空

        if retpwd:
            print(str(retpwd))
            if retpwd == sha_pwd:  # windows下需要retpwd.decode()
                print("登录成功 from redis")
            else:
                print("登录失败 from redis")

        else:  # redis 没有存用户名:密码 key/value对 数据库查询
            mysql_model = MysqlHelper.MysqlHelper()
            sql = """select pwd from my_1 where name = %s"""
            res = mysql_model.fetchone(sql, [user_name])  # 拿不到结果返回 none
            if not res:
                print("mysql查询用户名不存在")
            else:
                mysql_pwd = res[0]  # 查询到结果取出密码
                r.set(user_name, mysql_pwd)  # 这个需求是只要查询到有该用户就存储用户名和密码到redis下次就不会从数据库中查询直接通过redis查询用户名密码
                if mysql_pwd == sha_pwd:
                    # r.set(user_name, mysql_pwd)  # 这个需求是登陆成功存储到redis中下次查询速度更快无需查数据库
                    print("mysql登录成功并且写入redis")
                else:
                    print("mysql登录失败用户名密码错误!!")

    except Exception as e:
        print(e)


if __name__ == '__main__':
    while True:
        main()
