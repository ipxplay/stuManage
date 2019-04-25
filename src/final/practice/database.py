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

        
if __name__=="__main__":
#     saveData(jsondata=[{'test':'test'},{'admin':'admin'},{'wxit':'wxit'}])
    data= "wxit3,wxit3"
    saveData(data)
    print(getData())
