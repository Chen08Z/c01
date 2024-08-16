from op1 import block
from op1 import BlockChain
def addop(li,a,b,dic):# need to be a line of all datas split by ' '
    try:
        f=[]
        f=li.split(' ')
        a.append(block(data=f,prev_hash=a[-1].hash))
        if int(f[1]) not in dic:
            dic[int(f[1])]=str(1000+int(f[2]))
        elif int(f[1]) in dic:
            dic[int(f[1])]=int(dic[int(f[1])])
            dic[int(f[1])]+=int(f[2])
            dic[int(f[1])]=str(dic[int(f[1])])
        if int(f[0]) not in dic:
            dic[int(f[0])]=str(1000-int(f[2]))
        elif int(f[0]) in dic:
            dic[int(f[0])]=int(dic[int(f[0])])
            dic[int(f[0])]-=int(f[2])
            dic[int(f[0])]=str(dic[int(f[0])])
        b.add_block(a[-1])
    except IndexError:
        print("error")
