import logging
import os




def weblog(weblogstr,ip,path):
    logging.basicConfig(format='%(message)s - %(asctime)s',level="DEBUG")
    msg = ip + " "+path
    logging.info(msg)
    
# weblog("10.10.10.10", "/check")

  
# weblog("10.35.10.10","/check")
    
