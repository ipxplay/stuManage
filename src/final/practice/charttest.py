#coding:utf-8
 
import csv
import time
 
 
with open('u_ex181203.log','r') as f:
    data = f.readlines()
logdata = data[4:]
logdatalist = []
cs_uri_stem_list = []
c_ip_list = []
start = time.perf_counter()  
for linelog in logdata:
    linelog = linelog.split()
    if len(linelog)==15:
        logdatalist.append(linelog)
        cs_uri_stem_list.append(linelog[4])
        c_ip_list.append(linelog[8])
print(len(cs_uri_stem_list))        
cs_uri_stem_list_set = set(cs_uri_stem_list)
c_ip_list_set = set(c_ip_list)
cs_item_count_dict = {}
for cs_item in cs_uri_stem_list_set:
    cs_item_count_dict[cs_item] = cs_uri_stem_list.count(cs_item)
     
cs_max = max(cs_item_count_dict.values())
 
cs_item_count_dict_new = {v:k for k,v in cs_item_count_dict.items()}
end = time.perf_counter()  
print(cs_item_count_dict_new[cs_max])
print("ok")




