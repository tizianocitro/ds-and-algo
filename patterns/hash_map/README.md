# Hash Map

Imagine you have a huge bookshelf (like, Hogwarts library size). You've got a new book and need to find a spot for it and later on, search it quickly every time you need it. Instead of scanning the whole shelf, you use a magical spell that tells you exactly where to place or find it. This magical spell takes the book's title and gives you a specific location, like "4th shelf, 10th spot". But remember! Even if you slightly change the book's title, the spell gives a completely different spot.

Now, let's map this to computer science:

**Hashing**: It's a technique that takes an input (or 'message') and returns a fixed-size string, which looks random. The output, known as the hash value, is unique (mostly) to the given input.

**Hash Function**: This is our "magical spell" that converts the input data (like our book title) into a fixed-length value.

However, no magic is perfect. If two different inputs give the same hash, that's called a **collision**. It's like our spell accidentally pointing to the same spot for two different books. Good hash functions make these super rare. We will discuss this in detail later on.

## Why hashing?

Hashing is a great tool to quickly access, protect, and verify data. Here are a few of the common use cases of hashing:

1. **Quick Data Retrieval**: Hashing helps in accessing data super fast. With it, systems can quickly find a data piece without searching the whole database or list.

2. **Data Integrity Checks**: When downloading a file from the web, the site may provide you with a hash value for that file. If even a tiny portion of that file changes during the download, its hash will differ. By comparing the provided hash with the hash of the downloaded file, you can determine whether the file is exactly as the original, or if it was tampered with during the transfer.

3. **Password Security**: Instead of storing actual passwords, systems store their hash. It's like locking the real magical item away and just keeping a hologram on display.

4. **Hash Tables**: Hashing is used in programming for efficient data structures like hash tables. It’s like having organized shelves for our books where each item has its designated spot.

5. **Cryptography**: Some hash functions are used in cryptography to ensure data confidentiality and integrity. It's like a spell that only allows certain wizards to read a message.

6. **Data Deduplication**: If you're saving data, and you don’t want duplicates, you can just compare their hashes. Same hash? It’s the same data. It ensures you're not wasting space with repeated magical items.

7. **Load Balancing**: In big systems serving many users, hashes can be used to decide which server should handle a particular request. It's like deciding which magical portal to send a wizard based on their wand.

Hashing has numerous applications in several practical domains.

## Introduction to Hash Tables

A Hash Table (also known as Hash Map), at its core, is a data structure that allows us to store and retrieve data efficiently. If we think about a real-life analogy, it's like a library where each book (data) has a unique identifier (key) like ISBN, and all books are organized in a specific way to allow the librarian (hash function) to find and retrieve them quickly.

In other words, a Hash Table implements an associative array abstract data type (or Dictionary ADT), mapping keys to values. A Hash Table uses a hash function to compute an index into an array of buckets or slots where the desired value is stored.

There are four main elements to any Hash Table: Keys, Values, the Hash Function, and Buckets.

1. **Keys**: In our library analogy, think of keys as the unique identifiers for each book. Keys are the inputs we feed into our hash function. They can be any data type - numbers, strings, or even objects. The crucial characteristic of keys is that they should be unique. If two pieces of data share the same key, it might lead to complications, like collisions (we'll discuss this in detail later).

2. **Values**: Values are the actual data that we store in our Hash Table. They could be anything from a single number to a complex object or even a function. Using the key, we can quickly retrieve the corresponding value from the Hash Table.

3. **Hash Function - H(x)**: We've touched on this before, but it's worth emphasizing the importance of the hash function. This is the engine that drives a Hash Table. It's responsible for transforming keys into hash values, which dictate where we store our data in the table.

4. **Buckets**: Once the hash function processes our key, it produces a hash value. This value corresponds to a specific location or 'bucket' within the Hash Table. Think of buckets as shelves in our library, each one designated to store a specific book (or piece of data).

Here are the three basic operations that are performed on Hash Tables:

1. **Insert(key, value)** operation: Calculates the hash index `H(key)` and stores the key-value pair in the slot at that index.

2. **Search(key)** operation: Computes `H(key)` to find the slot and returns the value associated with the key, or `null` if not present.

3. **Delete(key)** operation: Removes the key-value pair stored at index `H(key)`.

### A naive Hash Table implementation

Imagine once again a major public library that needs to store basic information, such as Key (ISBN), Title, and Placement Info, for all available books. This system is heavily used, with librarians frequently searching for books. This results in many retrieval requests.

The frequent retrievals require an efficient solution that can quickly perform the search operation (ideally, in constant time). Therefore, the Hash table data structure perfectly suits the scenario.

Let's start by discussing our data model. We will use a dynamic array of the `Record` type to store the books' information. Here is what our `Record` class looks like:

```python
class Record:
    def __init__(self, key=-1, title="", placement_info=""):
        self.Key = key
        self.Title = title
        self.PlacementInfo = placement_info
```

Now, let's look at the `HashTable ADT` class definition. The `HashTable` class has an `HT_array` pointer to store the address of the dynamically allocated array of records. The `max_length` property is the maximum number of records the hash table can hold. The `length` represents the current number of records in the Hash table. It increments and decrements with insertions and deletions, respectively.

```python
class HashTable:
    def __init__(self, size):
        """
        Initializes a HashTable instance.

        Args:
            size (int): The maximum number of elements the HashTable can store.
        """
        self._max_length = size
        self._length = 0
        self._HT_array = [Record() for _ in range(size)]

    def __del__(self):
        """Destroys the HashTable instance and releases the memory."""
        del self._HT_array
        
    def H(self, key):
        """
        The Hash function.

        Args:
            key (int): The key for which the hash value is calculated.

        Returns:
            int: The calculated hash value.
        """
        # Implement your hash function logic here
        

    def Insert(self, item):
        """
        Inserts a record into the HashTable.

        Args:
            item (Record): The record to be inserted.

        Returns:
            bool: True if the record was inserted successfully, False otherwise.
        """
        # Implement the Insert method logic here
        return False

    def Search(self, key):
        """
        Searches for a record in the HashTable based on the given key.

        Args:
            key (int): The key to search for.

        Returns:
            Record or None: The record with the given key if found, None otherwise.
        """
        # Implement the Search method logic here
        return None

    def Delete(self, key):
        """
        Deletes a record from the HashTable based on the given key.

        Args:
            key (int): The key of the record to delete.

        Returns:
            bool: True if the record was deleted successfully, False otherwise.
        """
        # Implement the Delete method logic here
        return False
```
Let's define our Hash method `H()` for this naive implementation. We will use the simplest modular Hashing for this scenario:

```python
def H(self, key):
    return key % self.max_length
```

The above Hash function ensures we always get an index value in the range `[0, max_length -1]`. Let's move on to see how the simplified/naive `Insert()` method works.

The `Insert()` method takes a new record as a parameter and checks if the maximum capacity of the `HT_array` is not reached. If the table still can have more records, the method calculates a proper index/hash key for placing this item. After that, it puts the item at the computed index.

```python
def Insert(self, item):
    if self.length == self.max_length:
        print("Hash table is full. Cannot insert the key-value pair.")
        return False

    index = self.H(item.Key)
    self.HT_array[index] = item
    self.length += 1
    return True
```

*Point to ponder*: What happens if two different keys map to the same array index? This implementation overwrites it. Indeed, it is a flaw we will address in the Solving Collisions section.


Now, let's explore how and why the `Search()` method will retrieve records in `O(1)` for us. Here is a naive implementation:

```python
def Search(self, key, returnedItem):
    index = self.H(key)
    if self.HT_array[index].Key == -1:
        return False # Item not found
    returnedItem.Key = self.HT_array[index].Key
    returnedItem.Title = self.HT_array[index].Title
    returnedItem.PlacementInfo = self.HT_array[index].PlacementInfo
    return True # Return true to indicate the record was found
```

The `Search()` method applies the hash function `H()` on the passed key and checks if the hash table slot is empty or not. If this slot has a valid record, the `Search()` method assigns the record at this slot to the reference parameter. Also, it returns a true flag to indicate the operation's success.

The above implementation of `Search()` clearly takes constant time (i.e., `O(1)`) time to retrieve/ search any record regardless of the size our table may grow. This is evident by the fact that you only have to apply the hash function only constant number of times to calculate the position of the searched item.

*Note*: This naive implementation for the search doesn't cover all aspects. We will discuss a more sophisticated method in the next lesson.

Like the search operation, this deletion operation first locates the item requiring a delete. Afterward, the deletion operation simply places a null or default object at the table slot.

Here is what the naive implementation looks like:

```python
def Delete(self, key):
    index = self.H(key)
    if self.HT_array[index].Key == key:
        self.HT_array[index].Key = -1 # Mark the slot as empty
        self.length -= 1
        return True
    return False # The slot is already empty or there is a different item at the slot s
```

Again, like the search operation, deletion also takes a constant time to locate and delete an item from the table. But, it is important to note that this naive implementation is just to get an overall idea of how the hash table works. However, it doesn't cater to many exceptional cases; we will discuss those in the subsequent sections.

Here is the complete code for the naive hash table implementation with a sample driver code:

```python
class Record:
    def __init__(self, key=-1, title="", placement_info=""):
        self.Key = key
        self.Title = title
        self.PlacementInfo = placement_info

class HashTable:
    def __init__(self, size):
        # Pointer to store address of dynamically allocated array
        self.HT_array = [Record() for _ in range(size)]
        # To store maximum number of elements a Hash table can store
        self.max_length = size
        # To keep track of total records present in the hash table
        self.length = 0

    def __del__(self):
        # Cleanup the dynamically allocated array
        del self.HT_array

    # The Hash function
    def H(self, key):
        return key % self.max_length

    # Defining naive insertion
    def Insert(self, item):
        if self.length == self.max_length:
            print("Hash table is full. Cannot insert the key-value pair.")
            return False

        index = self.H(item.Key)
        self.HT_array[index] = item
        self.length += 1
        return True

    # Defining naive search
    def Search(self, key, returnedItem):
        index = self.H(key)
        if self.HT_array[index].Key == -1:
            # Record not found
            return False
        returnedItem.Key = self.HT_array[index].Key
        returnedItem.Title = self.HT_array[index].Title
        returnedItem.PlacementInfo = self.HT_array[index].PlacementInfo
        # Return true to indicate the record was found
        return True

    # Defining naive deletion
    def Delete(self, key):
        index = self.H(key)
        if self.HT_array[index].Key == key:
            # Mark the slot as empty
            self.HT_array[index].Key = -1
            self.length -= 1
            return True
        # The slot is already empty or there is a different item at the slot
        return False

# The driver code
if __name__ == "__main__":
    hashTable = HashTable(10)

    # Insert book information
    hashTable.Insert(Record(1001, "Introduction to Programming", "A2 Shelf"))
    hashTable.Insert(Record(1002, "Data Structures and Algorithms", "B1 Shelf"))
    hashTable.Insert(Record(1003, "Database Management Systems", "C3 Shelf"))

    # Retrieve book information
    book = Record()
    if hashTable.Search(1001, book):
        print("Book Information for Key", book.Key, ":")
        print("Title:", book.Title)
        print("Placement Info:", book.PlacementInfo)
    else:
        print("No book information found for Key 1001")

    # Delete a book information
    hashTable.Delete(1001)

    # Retrieve the book status after deletion
    if hashTable.Search(1001, book):
        print("Book Information for Key", book.Key, ":")
        print("Title:", book.Title)
        print("Placement Info:", book.PlacementInfo)
    else:
        print("No book information found for Key 1001")
```

### Hash Table Implementation in DIfferent Languages

Here is how different languages implement Hash Tables:

| Language | API |
| --------- | ------- |
| Python | dict |
| JavaScript | Object or Map |
| Java | java.util.Map Or java.util.HashMap |
| C++ | std::unordered_map |

## Issues with Hash Tables

Our Hash Table implementation is naive. By that, we mean that the code doesn't cater to some frequently occurring issues. Let's see what these issues really are.

### Collisions

A collision in a Hash Table occurs when an insert operation tries to insert an item at a table slot already occupied by another item. How can this happen? Let's find out.


#### Collision example

Reconsider our earlier example of the Hash Table for the public library book information storage. Assume, for the sake of simplicity, the Hash Table has the `max_length` equal to `10`. Further, you need to insert the following book records in it:

![Book records example](/assets/hashmap_1.png "Book records example")

Here is the hash value calculation for the first four entries:

![Key for the book records example](/assets/hashmap_2.png "Key for the book records example")

So the hash table array would look something like this:

![Hash map array](/assets/hashmap_3.png "Hash map array")

Now, what happens if we try inserting the record with the `Key` `1021`? The hash value for `1021` is the same as occupied by the book with the `Key` `1011` because `1021 % 10 = 1`. In this scenario, we say that a collision has occurred.

Collisions occur frequently in hash tables when two different keys hash to the same bucket. Without proper collision handling, lookup performance degrades from `O(1)` to `O(n)` linear search time. Managing collisions is crucial to efficient hash table implementation.

### Overflows

Overflow in a hash table occurs when the number of elements inserted exceeds the fixed capacity allocated for the underlying bucket array. For example, if you already have inserted information of ten books in the earlier discussed hash table, inserting the eleventh one will cause an overflow.

One important point to note here is that as the underlying bucket array starts filling towards its maximum capacity, the expectation of collisions starts increasing. Thereby the overall efficiency of hash table operations starts decreasing.

An ideal hash table implementation must resolve collisions effectively and must act to avoid any overflow early. In the next section, we will explore different strategies for handling collisions.

### Resolving Collisions

Remember that our naive hash table implementation directly overwrote existing records when collisions occurred. This is inaccurate as it loses data on insertion. This section describes how we can avoid such data losses with the help of collision resolution techniques.

Based on how we resolve the collisions, the collision resolution techniques are classified into two types:

- Open addressing/Closed hashing
- Chaining/Open hashing

#### Open Addressing (Closed Hashing):

Open addressing techniques resolve hash collisions by probing for the next available slot within the hash table itself. This approach is called open addressing since it opens up the entire hash table for finding an empty slot during insertion.

It is also known as closed hashing because the insertion is restricted to existing slots within the table without using any external data structures.

Depending on how you jump or probe to find the next empty slot, the closed hashing is further divided into multiple types. Here are the main collision resolution schemes used in the open-addressing scheme:

1. **Linear probing**: Linear probing is the simplest way to handle collisions by linearly searching consecutive slots for the next empty location.
2. **Quadratic probing**: When a collision occurs, the quadratic probing attempts to find an alternative empty slot for the key by using a quadratic function to probe the successive possible positions.
3. **Double hashing**: It uses two hash functions to determine the next probing location in case of a successive collision.
4. **Random probing**: Random probing uses a pseudo-random number generator (PRNG) to compute the step size or increment value for probes in case of collisions.

Implementation of insertion, search, and deletion operations is slightly different for each type of the operations.

#### Separate Chaining (Open Hashing):

Selecting the right closed hashing technique for resolving collisions can be tough. You need to keep the pros and cons of different strategies in mind and then have to make a decision.

Separate chaining offers a rather simpler chaining mechanism to resolve collisions. Each slot in the hash table points to a separate data structure, such as a linked-list. This linked-list or chain stores multiple elements that share the same hash index. When a collision occurs, new elements are simply appended to the existing list in the corresponding slot.

Separate chaining is an "open hashing" technique because the hash table is "open" to accommodate multiple elements within a single bucket (usually using a chain) to handle collisions. Here is the generalized conceptual diagram for the chaining method:

![Open hashing](/assets/open_hashing.png "Open hashing")

*Example*: Recall our earlier example of the hash table for storing books' information. Assume you have a hash table (with open hashing) of size `11` and have the following situation:

![Open hashing example](/assets/open_hashing_1.png "Open hashing example")

Now, here is what the hash table would look like after inserting a new book record `(1724, "Compilers Theory", "E4 Shelf")`:

![Open hashing example](/assets/open_hashing_2.png "Open hashing example")

The key `1724` hashes on `08`. Therefore, the item with this key is appended at the end of the chain, pointed by table slot `08`.

Let's now move on to implementing the hash table with separate chaining.

### A complete implementation

