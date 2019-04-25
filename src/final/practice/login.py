#coding:utf-8
from final.practice.database import getData

def login(name,password):
    flag = False
    for user in getData():
        if name==user.split(",")[0].strip() and password==user.split(",")[1].strip():
            flag =True
    return flag
        