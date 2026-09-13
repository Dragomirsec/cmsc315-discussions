# Unit 5 Discussion: Search Algorithms

## Overview

This assignment compares linear search and binary search.

## Learning Objectives

- Implement linear search
- Implement binary search
- Compare performance
- Analyze algorithm efficiency

## Requirements

1. Test both algorithms on a small dataset.
2. Test both algorithms on a large dataset.
3. Demonstrate edge cases.
4. Analyze performance.
5. Create a real-world search scenario.


## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
   I gained a deep understanding of the logic of diffrent search algorithems and how they affect the time compelxity of our programs. For example: a linear search looks through each value one by one till it finds the value giving it a worst time complexty of O(N), While binery search with every iteration cuts the list in half making its time complexity Olog(n)
2. What challenges did you encounter, and how did you overcome them?
   The main challenge that i faced wat that i accediently put the return -1 inside the while loop, making all the searches come out as if the value was not insdie the list. I overcame this quickly by looking at the loop and going through each process in my head while reading the code 
3. Explain when to use linear versus binary search, including tradeoffs in real-world scenarios.
   I feel the main benifit of linear search over binery search is that the list doesn't need to be sorted! That being said, it is much more in efficeint then a binary search. If i was every implamenting a seach algorithm i would look at if it need to sorted and if sorting the list would be more or less efficient the just using a linear search.