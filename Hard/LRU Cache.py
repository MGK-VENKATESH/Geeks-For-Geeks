Description:
Design a data structure that works like a LRU Cache. Here cap denotes the capacity of the cache and Q denotes the number of queries. Query can be of two types:

PUT x y: sets the value of the key x with value y
GET x: gets the key of x if present else returns -1.
The LRUCache class has two methods get() and put() which are defined as follows.

get(key): returns the value of the key if it already exists in the cache otherwise returns -1.
put(key, value): if the key is already present, update its value. If not present, add the key-value pair to the cache. If the cache reaches its capacity it should remove the least recently used item before inserting the new item.
In the constructor of the class the capacity of the cache should be initialized.
Examples:

Input: cap = 2, Q = 2, Queries = [["PUT", 1, 2], ["GET", 1]]
Output: [2]
Explanation: Cache Size = 2
["PUT", 1, 2] will insert the key-value pair (1, 2) in the cache,
["GET", 1] will print the value corresponding to Key 1, ie 2.
Input: cap = 2, Q = 8, Queries = [["PUT", 1, 2], ["PUT", 2, 3], ["PUT", 1, 5], ["PUT", 4, 5], ["PUT", 6, 7], ["GET", 4], ["PUT", 1, 2], ["GET", 3]]
Output: [5, -1]
Explanation: Cache Size = 2
["PUT", 1, 2] will insert the pair (1,2) in the cache.
["PUT", 2, 3] will insert the pair (2,3) in the cache: 1->2, 2->3(the most recently used one is kept at the rightmost position) 
["PUT", 1, 5] will replace the value of 1 from 2 to 5 : 2 -> 3, 1 -> 5
["PUT", 4, 5] : 1 -> 5, 4 -> 5 (Cache size is 2, hence we delete the least recently used key-value pair)
["PUT", 6, 7] : 4 -> 5, 6 -> 7 
["GET", 4] : Prints 5 (The cache now looks like 6 -> 7, 4->5)
["PUT", 1, 2] : 4 -> 5, 1 -> 2  (Cache size is 2, hence we delete the least recently used key-value pair)
["GET", 3] : No key value pair having key = 3. Hence, -1 is printed.
Constraints:
1 <= cap <= 103
1 <= Q <= 105
1 <= x, y <= 104

Python3:
#User function Template for python3

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, cap):
        """
        Initialize the LRUCache with a given capacity.
        """
        self.capacity = cap
        self.cache = {}  # Hashmap to store key-node pairs
        self.head = Node(0, 0)  # Dummy head node
        self.tail = Node(0, 0)  # Dummy tail node
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node):
        """
        Remove a node from the doubly linked list.
        """
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def _add(self, node):
        """
        Add a node right after the head.
        """
        next_node = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = next_node
        next_node.prev = node

    def get(self, key):
        """
        Return the value of the key if it exists in the cache; otherwise, return -1.
        """
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)  # Move the accessed node to the head (most recently used)
            self._add(node)
            return node.value
        return -1

    def put(self, key, value):
        """
        Add a key-value pair to the cache. If the cache exceeds capacity,
        remove the least recently used item.
        """
        if key in self.cache:
            # If the key exists, remove the old node
            self._remove(self.cache[key])
        elif len(self.cache) == self.capacity:
            # If at capacity, remove the least recently used item (tail's previous node)
            lru_node = self.tail.prev
            self._remove(lru_node)
            del self.cache[lru_node.key]

        # Add the new node to the cache and the linked list
        new_node = Node(key, value)
        self.cache[key] = new_node
        self._add(new_node)


