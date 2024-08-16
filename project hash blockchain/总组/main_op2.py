import hashlib as h
def ha(li,pre_hash):
    m=h.sha256()
    for i in li:
        m.update(str(i).encode('utf-8'))
    li.append(m.hexdigest())
