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
        # else a collision has occurred -> iterate over the list while node is not None
        # store the value of the previous node in list in 'prev' variable (initialised to the value of the node itself on first pass)
        prev = node
        while node is not None:
            # if the key of the previous node is the same as the one we're passing in, the linked pair already exists ->
            if prev.key == key:
                # overwrite the value of the linked pair
                prev.value = value 
            # else continue iterating over list
            # set the value of prev to the current node         
            prev = node
            # and set the value of the current node equal to the value of the next node   
            node = node.next
        # if the value of node is None (we have reached end of list and exited the while loop), add a new node 
        prev.next = LinkedPair(key, value)


    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        # generate the index for the element by hashing the key passed in to insert method
        index = self._hash_mod(key)
        # check if storage at new index is empty
        node = self.storage[index]

        # if the key of the node at the given index is equal to the key passed in, set the value of the node to None and return from function
        if node.key == key: 
            node.value = None
            return

        # else, while node is not None iterate over other nodes (ie LinkedPairs)
        while node is not None:
            # if the key of the current node == key passed in, break (we will need to set the value of node to None)
            if node.key == key:
                break
            # set the value of prev equal to the current node
            prev = node
            # set the value of the current node == current node.next to continue iterating
            node = node.next
        # if node is None (we've iterated over all LinkedPairs and not not found a node with the key we're looking for) just return None    
        if node is None:
            return None
        # else we have found the node we're looking for -> set the next node of the previous node equal to the next node of the current node   
        prev.next = node.next
        # set the current node = None
        node.value = None    



    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
       # generate the index to search for by hashing the key
        index = self._hash_mod(key)
       # iterate over linked list at given index
       # while the value of current node is not none and the key of the current node is not equal to the key we're looking for, we still have more elements to check
        node = self.storage[index]
        while node is not None and node.key != key:
            node = node.next
        # if we get to a point where node == None then we have reached the end of the list and the element has not been found -> return None
        if node is None:
            return None   
        # else we have reached a point in the list where the node is not None and the node.key == key -> return the value of the node
        return node.value    
     

    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        # set the capacity of hash table to be double what it currently is
        self.capacity *= 2
        # declare variable to hold everything from old storage
        old_storage = self.storage
        # set storage equal to array of Nones * new doubled capacity
        self.storage = [None] * self.capacity
        # iterate over old storage buckets
        for linked_pairs in old_storage:
            # if a list of linked pairs exists
            if linked_pairs is not None:
                # iterate over linked pairs
                node = linked_pairs
                while node is not None:
                    # insert into the hash table passing in the current nodes key and current nodes value
                    self.insert(node.key, node.value)
                    # set the val of current node = node.next to continue iteration
                    node = node.next



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
