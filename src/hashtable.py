# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''
    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity


    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return hash(key)


    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        pass


    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity


    def insert(self, key, value):
        '''
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Fill this in.
        '''

        # generate the index for the element by hashing the key passed in to insert method
        index = self._hash_mod(key)
        # check if storage at new index is empty
        node = self.storage[index]
        # if node is none, then storage at given index is empty ->
        if node is None:
            # set the value in storage at given index equal to new LinkedPair with key and value and return from function
            self.storage[index] = LinkedPair(key, value)
            return
        # else a collision has occurred -> iterate to the end of the list
        prev = node
        while node is not None:
            if prev.key == key:
                prev.value = value        
            prev = node
            node = node.next
        # once at the end of the list add the new LinkedPair    
        prev.next = LinkedPair(key, value)


    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        pass


    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
       # generate the index to search for by hashing the key
        index = self._hash_mod(key)
       # iterate over linked list at given index
       # while the next value of current node is not none and the key of the current node is not equal to the key we're looking for, we still have more elements to check
        node = self.storage[index]
        while node is not None:
            if node.key == key:
                return node.value
            else:    
                node = node.next
        # if we get to a point where node == None then we have reached the end of the list and the element has not been found -> return None
        return None    
     


    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        pass



if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")
