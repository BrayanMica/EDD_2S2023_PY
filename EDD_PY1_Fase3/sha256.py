import hashlib

class Sha256():
    def __init__(self):
        pass
    
    def hash(self, message):
        return hashlib.sha256(message.encode('utf-8')).hexdigest()
    
    def compare(self, message, hash):
        return self.hash(message) == hash


# if __name__ == "__main__":
#     sha256 = Sha256()
#     print(sha256.hash("hola"))