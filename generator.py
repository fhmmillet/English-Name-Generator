import sys
sys.path.append('..')
from lazy import *
from pprint import*
#######################

"""
ascii
utf-8          万国语
utf-16         万国语
big5           繁体中文
big5hkscs      繁体中文
gb2312         简体中文
gbk            繁简混合
gb18030        繁简混合
"""
Table.coding = "utf-8"

def table2set(t):
    s=set()
    for r in t:
        for i in range(1,5):
            block =r[i]
            if block is not None:
                s.update(block)
    return s


男生首字字典=table2set(Table.read("男生首字字典(偏好)",[strof,strof,strof,strof,strof]))
男生后字字典=table2set(Table.read("男生后字字典(偏好)",[strof,strof,strof,strof,strof]))
女生首字字典=table2set(Table.read("女生首字字典(偏好)",[strof,strof,strof,strof,strof]))
女生后字字典=table2set(Table.read("女生后字字典(偏好)",[strof,strof,strof,strof,strof]))
中字字典=table2set(Table.read("中字字典",[strof,strof,strof,strof,strof]))
字典=table2set(Table.read("字典",[strof,strof,strof,strof,strof]))

from random import *

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

trans=Table.read("trans",[strof,strof,strof,strof,strof,strof,strof,strof])

def create_dict(t):
    d={}
    for row in t:

        sub=[]
        for i in [3,4,5,6]:
            if row[i] is not None:
                sub.append(row[i])
        d[row[2]]=sub
    return d

edict = create_dict(trans)


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


def rd(f,t):
    return choice(list(range(f,t+1)))

#对于字的长段概率调整，23，最为常见，45不是很常见
t=Table([["engname","transname"]])


n=10
#n: 一共多少个名字
for i in range(n):

    length = rd(2,3)
    #length: 名字一共多少个部分
    fullname=[]
    efullname=[]
    for j in range(length):
        m=rd(2,5)
        #m : 每个部分一共多少个音节
        part =name(m)
        epart=z2e(part,edict)
        fullname.append(part)
        efullname.append(epart)
    s="·".join(fullname)
    es="·".join(efullname)
    #t.append([es,s])
    #print(t)
    #上面2行 uncomment 表示用表格来呈现
    print()
    print(es)
    print(s)
    
    



