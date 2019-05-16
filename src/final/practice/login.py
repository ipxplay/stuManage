#coding:utf-8
from final.practice.database import getData,sqlite3GetData

def login(name,password):
    flag = False
    for user in sqlite3GetData():
        if name==user[0].strip() and password==user[1].strip():
            flag =True
    return flag
        