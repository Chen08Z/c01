import hashlib
from datetime import datetime
def mine(b):
    nonce=0
    while True:
        b_d=f"{b.prev_hash}{nonce}".encode()
        hash_v=hashlib.sha256(b_d)
        for i in b.data:
            hash_v.update(str(i).encode('utf-8'))
        h=hash_v.hexdigest()
        if hashlib.sha256(h.encode('utf-8')).hexdigest()[:4]=='0000':
            return nonce
        nonce+=1
class block:
    def __init__(self,data,prev_hash):
        self.prev_hash = prev_hash
        self.data = data
        self.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        message = hashlib.sha256()
        message.update(str(self.prev_hash).encode('utf-8'))
        self.n=mine(self)
        message.update(str(self.n).encode('utf-8'))
        for i in data:
            message.update(str(i).encode('utf-8'))
        self.hash = hashlib.sha256(message.hexdigest().encode('utf-8')).hexdigest()
class BlockChain:
    def __init__(self):
        self.blocks = []
    def add_block(self, block):
        self.blocks.append(block)   
#sha1:0.0;sha256:0.0;sha512:0.0;sha3-256:0.0;sha3-512:0.0
