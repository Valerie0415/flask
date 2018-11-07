#-*- coding: UTF-8 -*- 
# from __future__ import print_function

# import json
_dict = {}
f = open("E:\Python project\log.txt","r") 
lines = f.readlines()
for line in lines:
    r=line[11:-2]
    (key, value) = r.strip().split(':')
    _dict[key] = value
    print _dict 


# >>>new_list= [['key1','value1'],['key2','value2'],['key3','value3']]
# >>>new_dict = {}
# >>> for i in new_list:
# ...   new_dict[i[0]] = i[1]                #字典赋值，左边为key，右边为value
# ...
# >>> new_dict
# {'key3': 'value3', 'key2': 'value2', 'key1': 'value1'}



 #    d = {}
 #    for line in s.split():		
	# key, value = line.split(",")
	# d[key] = value
	# print (d)
    # d=dict()
    # d[s[0]] = s[1]
    # for i in s:
    # 	d[i[1]]=i[0] #字典赋值。左边为key，右边为value
    # 	print d
    # a=[121,122,123,124,128]

#分割列表两两一对
    # b = [s[i:i+2] for i in range(0,len(s),2)]
    # print b(s)


    #将其转换成字典形式
    
    # d = dict()
    # d[s[0]] = s[1]
    # d[s[2]] = s[3]  
    # d[s[4]] = s[5]  
    # d[s[6]] = s[7]  
    # d[s[8]] = s[9] 
    # print d[s[0]]
    # for x in d[s[0]]:
    # 	a.append(x)
    # print a
 #    s=d[s[0]]


# if x not in key:
	    # 	key.append(x)
	    # 	value.append('0')
	    # else:
	    # 	print key,value
	    	#print key,value


rows = len(f.readlines())
    print rows


# li=0
    # for lin in dictionary['121']:
    #     lin =dictionary['121'].strip()   #去除（字符串的）左边的和右边的（默认空格）
    #     li +=li
    #     print lin


arr=[]
    lin =dictionary['121'].replace("\n",'').split(',')
    arr.append(arr)
    print arr



list = ['1','2','3']
print ','.join(list)
print map(int,list)

1,2,3
[1, 2, 3]
>>>如何在Python里去掉列表的方括号和引号
