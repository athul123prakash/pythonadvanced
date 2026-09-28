# name,age,place
# arun,23,ekm
# amal,24,tvm

#read
# import csv
# f=open("data.csv",'r')
# content=csv.reader(f)
# print(content)
# f.close()

#write
import csv
f=open("book.csv",'w')
content=[
    ['title','author','place'],
    ['book1','john','ekm'],
    ['book2','sam','tvm']
]
writer=csv.writer(f)
writer.writerows(content)
f.close()