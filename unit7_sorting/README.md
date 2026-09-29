# Unit 7 Discussion: Sorting Algorithms

## Overview

This assignment compares Bubble Sort and Merge Sort.

## Learning Objectives

- Implement Bubble Sort
- Implement Merge Sort
- Understand divide-and-conquer
- Compare algorithm efficiency

## Requirements

1. Test Bubble Sort and Merge Sort.
2. Use multiple datasets.
3. Demonstrate edge cases.
4. Analyze performance.
5. Create a real-world sorting example.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Compare and constrast each sorting algorithm based on efficiency differences, tradeoffs made, and when to each.

While completing this assignment, I acquired a deep understanding behind the logic and complexity of merge sort and bubble sort. Bubble sort compares every new element against all previous elements until it finds one smaller than it. This gives bubble sort a time complexity of O(N²). On the other hand, merge sort recursively divides the list in half and merges those halves back together while keeping it sorted. This gives merge sort an average complexity of O(N log N). Honestly, in a real-world scenario, I wouldn't use bubble sort because it's just inefficient compared to other sorting algorithms like merge sort.

The main challenge I faced in this assignment was that I had used (startIndex - endIndex) // 2 in the merge sort algorithm, and this was causing it in some cases to return 0 and infinitely recurse, causing a recursion error. I fixed this by implementing len(lst) // 2, making sure it never returns 0. Also, because of this, I removed the start and end indices and replaced the if statement with 1 < len(lst) as a cleaner version.