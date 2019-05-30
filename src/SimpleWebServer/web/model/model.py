import sqlite3
import pandas as pd

class Model:
    def __init__(self):
        pass
    
    def open(self):
        self.conn = sqlite3.connect("user.db")
        self.cursor = self.conn.cursor()
    
    def csvToDb(self):
        self.open()
        colunms = ["name","pwd"]
        df = pd.read_csv("userinfo.csv",names=colunms)
        df.to_sql("userinfo",self.conn)
        self.close()
    
    def getAllUserInfo(self):
        self.open()
        sql = "select * from userinfo"
        self.cursor.execute(sql)
        data = self.cursor.fetchall()        
        self.close()
        return data    
    def checkUserSAndpwd(self,username,pwd):
        flag = False
        userinfos =  self.getAllUserInfo()
        for user in userinfos:
            if (username==user[1] and pwd==user[2]):
                flag = True
            else:
                pass    
        return flag
            
        
        
    def close(self):
        self.cursor.close()
        self.conn.close()
        
if __name__=="__main__":
    model = Model()
    model.csvToDb()
    data = model.getAllUserInfo()
    print(data)