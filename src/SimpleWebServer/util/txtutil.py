
def getUsersAndPwds(filename="../user.txt"):
    with open(filename,encoding="utf-8") as f:
        data = f.readlines()
    return data
def checkUserAndPwd(username,pwd,filename="../user.txt"):
    flag = False
    alluerinfos = getUsersAndPwds(filename)
    for user in alluerinfos:
        if (username==user[0] and pwd==user[1]):
            flag = True
        else:
            pass    
    return flag
    