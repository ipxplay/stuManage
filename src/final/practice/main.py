#coding:utf-8
from final.practice.msgPrint import MsgPrint
from final.practice.login import login
from final.practice.student import Student
from final.practice.database import saveData,getData
import os
if __name__=="__main__":
#     测试
#     printtest = MsgPrint(key=[{"name":"张三","no":1234567890,"major":"物联网","grade":"一年级","score":90},{"name":"张三","no":1234567890,"major":"物联网","grade":"一年级","score":90}])
#     printtest.mainMenu()
#     基本流程

# 登陆
#     print(getData())

    flag = 0
    while True:
        print("please input usename and password to login the system.")
        name = input("username:")
        password = input("password:")
        if (login(name, password)):
            mainmenu = MsgPrint()
            stu = Student()
            while True:
                mainmenu.mainMenu()                        
                cmd = input("mainmenu,please input your choice:")            
                if cmd=="1":
                    mainmenu.studentManageMenu()
                    mancmd = input("ManageMenu,please input your choice:")
                    if mancmd =="1":
                        mainmenu.studentAddMenu()
                        stuinfo = input("AddMenu,please input student infos:").split(",")
                        stu.add(stuinfo[0], stuinfo[1], stuinfo[2], stuinfo[3], stuinfo[4])
                        print(stu.select())
                    elif mancmd=="2":
                        mainmenu.studentDelMenu()
                        stuno = input("DelMenu,please input student no:")
                        stu.delete(stuno)
                        print(stu.select())
#                 学生查找
                elif cmd=="2":
                    pass
#                 成绩管理
                elif cmd=="3":
                    pass
            
                

# 成功登陆主菜单
# 选择编号进入相应子菜单
    