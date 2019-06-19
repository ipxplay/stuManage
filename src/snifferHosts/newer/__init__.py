#coding:gbk
import os
import logging
import subprocess
import threading
import queue
import tkinter

def getLanHosts():
    hosts = []
    host = "10.35.53.{}"
    for ip_ex in range(1,15,6):
        hosts.append(host.format(str(ip_ex)))
    return hosts
def sniffer(t1):
    hosts = getLanHosts()
    alivekey = "字节=32"
    aliveHosts = []
    logging.basicConfig(filename="../logs/host.log",format="%(asctime)s - %(message)s - %(filename)s",level="DEBUG")
    for host in hosts:
        command = "ping {}".format(host)
        t1.insert(tkinter.END,command+"\r\n")
#         q_text.insert(command)
    #     ress = os.popen(command).readlines()[2:5]
    #     msg = host+" - "+ress[0]
        process = subprocess.Popen(command,stdout=subprocess.PIPE)
        result = process.communicate()
        msg = host+" - "+result[0].decode("gbk")
        print(msg)      
        logging.info(msg)
    #     for res in result[0].decode("gbk").split('\n\r'):
    #         print(res)
        if alivekey in result[0].decode("gbk"):
            t1.insert(tkinter.END,"{} is alive.".format(host)+"\r\n")
            print("{} is alive.".format(host))
            if host not in aliveHosts:
                aliveHosts.append(host)
        else:
            t1.insert(tkinter.END,"{} is dead.".format(host)+"\r\n")
    print(aliveHosts)
    
def sniffer_thread(t1):
#     q_text = text.get()
    s_thread = threading.Thread(target=lambda:sniffer(t1))
    s_thread.setDaemon(True)
    s_thread.start()
    
    
                
if __name__=="__main__":
    sniffer()            
              
        
    
# command = "ping 10.35.254.254"
# res = os.popen(command).readlines()[2:5]
# print(res)