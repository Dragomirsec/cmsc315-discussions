# Unit 6 Discussion: Dictionaries as Hash Tables

## Overview

This assignment uses Python dictionaries to demonstrate hash table behavior.

## Learning Objectives

- Insert key-value pairs
- Retrieve values efficiently
- Update existing values
- Remove entries
- Understand hashing concepts

## Requirements

1. Create and populate a dictionary.
2. Demonstrate lookup operations.
3. Demonstrate update operations.
4. Demonstrate delete operations.
5. Test edge cases.
6. Create a real-world scenario.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
	I feel that my main take away from this week text book and assignment was to deeper understanding of how hash tables work and how they affect efficiency. I was recently talking to a data scientist, and he commented one of the advantages humans still have against ai is taking complexity into account when designing a algorithm. 
2. What challenges did you encounter, and how did you overcome them?
	One of the main challenges i faced was understating exactly what was the difference between a dict and a hash map. But after some quick googling about what exactly are dictionaries i discovered, that they are hash maps!  
3. Explain how hash tables behave, what collisions are, and how hash tables can improve efficiency.
	Hash tables are basically large lists of key value pairs that are stored in a location indicated by the hash (a mathematical function ) of the key. Collisions are when two inputs produce the same output. Hash tables improve the efficiency over list, because it allows a more instant look up of values. While a linear search will have a complexity of O(N), the average search complexity of a hash table is O(1). 