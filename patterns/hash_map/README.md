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

