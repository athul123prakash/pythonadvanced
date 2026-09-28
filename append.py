#write a pgm to append the content from one file into another text file
# from os import write
# from pkgutil import read_code

# f=open("k.txt","r")
# s=f.read()
# f.close()
# q=open("total.txt","a")
# q.write(s)
# q.close()

#a+
# f=open("k.txt","a+")
# s=f.write('world')
# f.close()
# print(s)

#tell() #seek()

# f=open("k.txt","a+")
# print(f.tell())
# s=f.write('world')
# print(f.tell())
# print(f.seek(0))
# f.close()

#delete
# import os
# os.remove("k.txt")
# print("file is deleted")

#menu driven
# 1.file read
# 2.file write()
# 3.file append()
# 4.file search()
# 5.file delete()
# 6.exit

# while true:

[{"name": "Arun", "age": 23}, {"name": "Amal", "age": 24}]
import json
f=open('data.json','r')
content=json.load(f)
print(content)
f.close()

