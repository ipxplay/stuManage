from urllib import request
import re
import time

url= 'http://www.wxit.edu.cn'
datahandler = request.urlopen(url)
data = datahandler.read()
data = data.decode()
pattern = r'<img src="(/.*?)" .*?/>'
photospath = re.findall(pattern, data)

name = 1

for photopath in photospath:
    fileext = photopath.split('.')[-1]
    url1 = url + photopath
    print(url1)
    picname = str(name) + "."+fileext
    request.urlretrieve(url1, picname)
    name = name + 1
    time.sleep(0.5)