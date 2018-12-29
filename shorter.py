from lzdb import *
from pprint import*
from random import *

Table.coding = "utf-8"

def table2set(t):
    s=set()
    for r in t:
        for i in range(1,5):
            block =r[i]
            if block is not None:
                s.update(block)
    return s

def name(m, rate = 0,time=1):
    s = ""
    q=rate
    for i in range(m):
        if len(s)>1 and q > random():
            sub =s[-1]
            time-=1
            q=0
        else:
            if i == 0:
                sub=choice(list(男生首字字典))
            else:
                sub = choice(list(男生后字字典))
            if time>0:
                q=rate
        s+=sub
    return s

def create_dict(t):
    d={}
    for row in t:

        sub=[]
        for i in [3,4,5,6]:
            if row[i] is not None:
                sub.append(row[i])
        d[row[2]]=sub
    return d

def z2e(s,d):
    s.replace("克斯","x")
    result=""
    for word in s:
        if word in d:
            result+=choice(d[word])
        else:
            result+=word
    result=result.capitalize() 
    return result

def rd(array):
    f,t=array
    return choice(list(range(f,t+1)))

###main###
男生首字字典=table2set(Table.read("男生首字字典(偏好)",[strof,strof,strof,strof,strof]))
男生后字字典=table2set(Table.read("男生后字字典(偏好)",[strof,strof,strof,strof,strof]))
女生首字字典=table2set(Table.read("女生首字字典(偏好)",[strof,strof,strof,strof,strof]))
女生后字字典=table2set(Table.read("女生后字字典(偏好)",[strof,strof,strof,strof,strof]))
中字字典=table2set(Table.read("中字字典",[strof,strof,strof,strof,strof]))
trans=Table.read("trans",[strof,strof,strof,strof,strof,strof,strof,strof])
edict = create_dict(trans)
t=Table([["engname","transname"]])
print()

def make(n,num,length):

    #n: 一共多少个名字
    for i in range(n):

        nums = rd(num)
        #length: 名字一共多少个部分
        fullname=[]
        efullname=[]
        for j in range(nums):
            lengths=rd(length)
            #m : 每个部分一共多少个音节
            part =name(lengths)
            epart=z2e(part,edict)
            fullname.append(part)
            efullname.append(epart)
        s="·".join(fullname)
        es="·".join(efullname)
        t.append([es,s])
        
        #print(es)
        #print(s)
        #print()
make(100,[1,1],[2,2])
make(100,[1,1],[3,3])
make(50,[1,1],[4,4])
make(100,[2,2],[1,3])
make(100,[2,2],[2,3])
make(100,[2,2],[2,4])
make(100,[2,2],[1,4])
make(100,[3,3],[2,3])
make(100,[3,3],[2,5])
make(100,[1,3],[2,3])
make(50,[1,3],[1,4])

#print(t)
for i in range(1,1000+1):
    row=t[i]
    s="{}: {}----{}".format(i,row[0],row[1])
    print(s)

#用表格来呈现
