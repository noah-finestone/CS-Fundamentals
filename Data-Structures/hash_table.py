# Hash Tables are used to index and retrieve large amounts of data efficiently. Each key's address is calculated using the key itself.
# Collisions can occur when two keys have the same hash value. This is resolved with open or closed addressing.
# Open addressing is a method of resolving collisions by finding a different address than the calculated one. Linear probing, Plus 3 rehash, Quadratic probing, and Double hashing are all methods of open addressing.
# Closed addressing is a method of resolving collisions by chaining items that have collided in a linked list.
# Load factor = # of items stored / size of array
# Best case time complexity is O(1), and worst case time complexity is O(N).
# Open addressing with linear probing can work reasonably well as long as the load factor is reasonably low.
# The objectives of hash functions are to minimize collisions, ensure a uniform distribution of hash values, make it easy to calculate, and resolve any collisions.
# Insertion, deletion, and retrieval of data can be performed in constant time using hash tables.

# Future improvements: add a load factor function and a resize function based on a cetain percentage of how full the hash table gets

class HashTable: 

    def __init__(self, size):
        self.size = size
        self.hash_table = [[] for _ in range(self.size)] # array of lists 

    def isEmpty(self):
        sum = 0 
        for i in range(self.size):
            sum += len(self.hash_table[i])
        if sum == 0:
            return True
        return False

    def hashFunction(self, key):
        hash_value = sum(list(ord(char) for char in str(key)))
        # modulus is applied to ensure hash value falls within range of bucket indices
        return hash_value % self.size 

    def insertItem(self, key, value): 
        hash_value = self.hashFunction(key)
        bucket = self.hash_table[hash_value]

        # insert key value pair using seperate chaining (using an array)
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                print("Key '{}' exists. Value replaced with '{}'.".format(key, value))
                return 
        bucket.append((key, value))

    def removeItem(self, key):
        hash_value = self.hashFunction(key)
        bucket = self.hash_table[hash_value]

        # search for the key and delete it 
        for i, (k, v) in enumerate(bucket):
            if k == key:
                del bucket[i]
                print("('{}', '{}') has been deleted.".format(k, v))
                return
        # raise KeyError("Key '{}' not found".format(key))
        print("[WANRING] '{}' not found".format(key))

    def getItem(self, key):
        hash_value = self.hashFunction(key)
        bucket = self.hash_table[hash_value]

        # search for the key in the bucket
        bucket = self.hash_table[hash_value]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                return v 
        # raise KeyError("'{}' not found".format(key))
        print("[WANRING] '{}' not found".format(key))

    def printTable(self):
        # Print the key-value pairs in each bucket
        for i, bucket in enumerate(self.hash_table):
            print("Bucket '{}': '{}'".format(i, bucket)) 

if __name__ == '__main__':
    hashTable = HashTable(10)
    print("Is hash table empty: " + str(hashTable.isEmpty()))
    hashTable.insertItem('Noah', 22)
    hashTable.insertItem('Alex', 20)
    hashTable.insertItem('Drew', 29)
    hashTable.insertItem('Camille', 26)
    hashTable.insertItem('Paul', 34)

    # print table
    hashTable.printTable()
    
    print(hashTable.getItem('Noah')) # output should be 22
    print(hashTable.getItem('Lea'))
    hashTable.removeItem('Alex')
    hashTable.insertItem('Noah', 23)

    # print updated table
    hashTable.printTable()
    print("Is hash table empty: " + str(hashTable.isEmpty()))



