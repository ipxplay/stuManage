import configparser

def getPort():
    cf = configparser.ConfigParser()
    cfgpath = r"E:\stuManage\src\SimpleWebServer\configarure\web.ini"
    cf.read(cfgpath, encoding="utf-8")
    return cf.get("host", "port")

def getLogfile():
    cf = configparser.ConfigParser()
    cfgpath = r"E:\stuManage\src\SimpleWebServer\configarure\web.ini"
    cf.read(cfgpath, encoding="utf-8")
    return cf.get("log", "logfile ")

if __name__ == "__main__":
    print(getPort())