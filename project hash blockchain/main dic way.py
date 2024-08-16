l={}
import hashlib as ha
def adac(n,dic,cn,m):
    dic[cn]=[n,m]
def transform(cn1,cn2,dic,m):
    if dic[cn1][1]<m:
        return False
    dic[cn1][1]-=m
    dic[cn2][1]+=m
    return True
def has(dic,cn):
    a=dic[cn]
    print(a)
    b=ha.sha256()
    for i in range(len(a)):
        if str(i).isdigit():
            b.update(int(a[i]))
        else:
            b.update(a[i].encode())
    dic[cn].append(b)
adac('chen',l,627876545678,8268)
adac('hsiuh',l,572789929,84793287)
adac('yfdysgghs',l,65467882,76567)
adac("hgdgfa",l,5845455449643,25865452)
adac("jdsgj",l,58547747479689,985655)
has(l,627876545678)
has(l,572789929)
has(l,65467882)
print(l)
print(transform(65467882,627876545678,l,5689))
print(transform(65467882,627876545678,l,578987678))
print(l)

