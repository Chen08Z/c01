from op1 import BlockChain
from op1 import block
from opb import addop
blockChain = BlockChain()
a=[]
dic={999999999:'999999999999999999999999999999999999'}
def main():
    while True:
        try:
            t=int(input("choices:1:addoperation;2:checkbalance;other:exit"))
            if t==1:#ok
                b=input('your data list in format of s r m,split by using space/" "')
                addop(b,a,blockChain,dic)
                printf(blockChain)
                dic[999999999]='999999999999999999999999999999999999'
            elif t==2:#not ok
                b=input('card number(should be all integer)')
                try:
                    print(dic[int(b)])
                except:
                    print("disapproved")
            else:
                break
        except EOFError:
            break
        except ValueError:
            break
f=open('account.txt')
txt=[]
for i in f:
    c=i.strip()
    b=[]
    b=c.split(' ')
    txt.append(b)
f.close()
for i in range(len(txt)):
    if i!=0:
        a.append(block(data=txt[i],prev_hash=a[-1].hash))
        blockChain.add_block(a[-1])
    else:
        a.append(block(data=txt[i],prev_hash=''))
        blockChain.add_block(a[-1])
    if int(txt[i][1]) not in dic:
        dic[int(txt[i][1])]=str(1000+int(txt[i][2]))
    elif int(txt[i][1]) in dic:
        dic[txt[i][1]]=int(dic[txt[i][1]])
        dic[int(txt[i][1])]+=int(txt[i][2])
        dic[txt[i][1]]=str(dic[txt[i][1]])
    if int(txt[i][0]) not in dic:
        dic[int(txt[i][0])]=str(1000-int(txt[i][2]))
    elif int(txt[i][0]) in dic:
        dic[txt[i][0]]=int(dic[txt[i][0]])
        dic[int(txt[i][0])]-=int(txt[i][2])
        dic[txt[i][0]]=str(dic[txt[i][0]])
def printf(q):
    print("现在区块链包含区块个数为：%d\n" % len(q.blocks))
    blockHeight = 0
    for block in q.blocks:
        print(f"本区块高度为：{blockHeight}")
        print(f"父区块哈希：{block.prev_hash}")
        print(f"区块内容：{block.data}")
        print(f"区块哈希：{block.hash}")
        print(f"区块随机值：{block.n}")
        print()
        blockHeight += 1
printf(blockChain)
main()
