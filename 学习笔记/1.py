#filename = "E:\Python project\1.bin"  
#lines = []
#coding:utf8
#-*- coding: UTF-8 -*- 
filename = raw_input('ÇëÊäÈëÎÄ¼þ')
try:  
    f = open(filename, 'rb')  
    #lines = f.readlines()
    print hello
except IOError as e:  
    print e  
#else:  
 #   for line in lines:  
  #      print line  
finally:  
    f.close() 

