# Unit 3 Discussion: List Operations

## Overview

This assignment examines insertion, deletion, and searching in Python lists.

## Learning Objectives

- Insert values into a list
- Delete values from a list
- Search for values in a list
- Analyze list behavior and performance

## Requirements

1. Test insertion at the beginning, middle, and end.
2. Test deletion at the beginning, middle, and end.
3. Search for existing and missing values.
4. Demonstrate edge cases.
5. Create a real-world scenario.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. How do list operations impact performance in real-world applications?

Reflections

In this assignment, I had to create functions that insert, delete, and search for values in a list. I grasped how the different operations impact performance. Additionally, I had to design tests to verify the functionality of said functions.

Difficulties

The main difficulty I faced was designing the insert_at() function to cover the edge cases when the list is empty and when you insert at an index larger than the list. I wasn't sure of an elegant solution for this! At first, I thought of adding an elif statement, but I found it redundant because it would perform the same action as when the list was empty. So, I decided to combine the two using an or statement.

Another difficulty I faced was that I forgot about the existence of the enumerate function, and because of this, I was using a bulky for loop when enumerate would be cleaner and more efficient.

List Operations

List operations impact real-world computer systems, as some operations are more resource-intensive than others, just from the sheer amount of sub-operations needed to finish the operations. For example, to insert a value at the beginning of a list, you need to shift all the other values in the list, and each value shifted is a sub-operation. The number of sub-operations only grows as the list grows. This is the difference between counting one pack of M&Ms versus a jar of M&Ms. It's quick and easy when there's just a few, while it's long and hard when there's a lot.