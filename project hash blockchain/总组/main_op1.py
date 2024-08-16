def addaccount(name1,re,sen,listi,card_number,money):#approved
    listi.append([])
    listi[-1].append(name1)
    listi[-1].append(re)
    listi[-1].append(sen)
    listi[-1].append(card_number)
    listi[-1].append(money)
def fp(cn,listi):
    for i in range(len(listi)):
        if cn==listi[i][3]:
            return i
def transformat(cn1,cn2,listi,money):
    if listi[fp(cn1,listi)][3]<money:
        return False
    listi[fp(cn1,listi)][3]-=money
    listi[fp(cn2,listi)][3]+=money
    return True
