f=open('account.txt')
txt=[]
for i in f:
    a=i.strip()
    b=[]
    b=a.split(' ')
    txt.append(b)
f.close()
from main_op2 import ha
for i in range(len(txt)):#add hash
    if i==0:
        ha(txt[0],[0])
    else:
        ha(txt[i],txt[i-1][-1])
print(txt)
