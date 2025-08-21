import hashlib
import time

class Block:
    def __init__(self, index, timestamp, data, prev_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.prev_hash = prev_hash
        self.hash = self.calc_hash()

    def calc_hash(self):
        sha = hashlib.sha256()
       
        sha.update(str(self.index).encode('utf-8'))
        sha.update(str(self.timestamp).encode('utf-8'))
        sha.update(self.data.encode('utf-8'))
        return sha.hexdigest()

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block(0, time.time(), "Genesis Block", "0")

    def add_block(self, data):
        prev_block = self.chain[-1]
        new_block = Block(len(self.chain), time.time(), data, prev_block.hash)
        self.chain.append(new_block)



blockchain = Blockchain()
blockchain.add_block("First Block")
blockchain.add_block("Second Block")
blockchain.add_block("Third Block")

print("Blockchain:")
for block in blockchain.chain:
    print("Index:", block.index)
    print("Timestamp:", block.timestamp)
    print("Data:", block.data)
    print("Hash:", block.hash)
    print("Previous Hash:", block.prev_hash)
    print()
