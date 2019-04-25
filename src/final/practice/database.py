#coding:utf-8
import json
import final.practice.config as config

def saveData(data,filename=config.txtfile):
    with open(filename,mode="a",encoding="UTF-8") as f:
        f.write(data+"\n")
        
def getData(filename=config.txtfile):
    str=[]
    try:
        with open(filename,encoding="UTF-8") as f:
            str = f.readlines()
    except:
        pass            
    return str
import sqlite3

def sqlite3Connect(dbfile=config.dbfile):
    conn = sqlite3.connect(dbfile)
    return conn

def sqlite3CreateTable():
    conn = sqlite3Connect()
    cursor = conn.cursor()
    cursor.execute("create table userinfo (username varchar(20),passwd varchar(20)) ")
    cursor.close()
    conn.close()
    
def sqlite3SaveData(username="admin",passwd="admin"):
    conn = sqlite3Connect()
    cursor = conn.cursor()
    sql = "insert into userinfo (username,passwd) values (\"admin\",\"admin\")"
#     sql = sql.format(username,passwd)
    cursor.execute(sql)
    cursor.close()
    conn.close()
    
def sqlite3GetData():
    conn = sqlite3Connect()
    cursor = conn.cursor()
    cursor.execute("select * from userinfo")
    data = cursor.fetchall()
    cursor.close()
    conn.close()
    return data
    
    
    
    
        
if __name__=="__main__":
#     saveData(jsondata=[{'test':'test'},{'admin':'admin'},{'wxit':'wxit'}])
#     data= "wxit3,wxit3"
#     saveData(data)
#     print(getData())
#     sqlite3CreateTable()
    sqlite3SaveData()
    print(sqlite3GetData())
