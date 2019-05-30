import re
from bs4 import BeautifulSoup

with open("time.html",'r') as f:
    data = f.read()
# pattern = r'<h3>.*?([\u4e00-\u9fa5]+).*?</h3>'
pattern = r'<p class="point">(.*?)</p>'
print(re.findall(pattern, data))  
