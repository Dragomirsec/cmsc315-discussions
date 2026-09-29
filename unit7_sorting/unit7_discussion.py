"""
===========================================================
UNIT 7 DISCUSSION: SORTING ALGORITHMS (BUBBLE SORT VS MERGE SORT)
===========================================================

STUDENT INSTRUCTIONS:

This project explores two fundamental sorting algorithms:
- Bubble Sort (iterative, comparison-based)
- Merge Sort (recursive, divide-and-conquer)

Your goal is to demonstrate both your coding ability and your
understanding of algorithm efficiency and behavior.
"""


def bubble_sort(lst):
    """
    TODO (Student):
    Implement Bubble Sort.

    Requirements:
    - Create a copy of the original list.
    - Compare adjacent elements.
    - Swap elements when they are out of order.
    - Continue until the list is sorted.
    - Return the sorted list.
    - Add meaningful comments.

    """
    # Copy of the original list that will be sorted 
    copy_lst = list(lst)
    
    i = 0
    while i < len(copy_lst) -1:
        j = 0 
        while j < len(copy_lst) -i -1:
            # is element j bigger the element j + 1,
            # if true swap them 
            if copy_lst[j] > copy_lst[j + 1]:
                # creating a temp veriable to save j
                temp = copy_lst[j]
                # replacing j with j + 1
                copy_lst[j] = copy_lst[j+1]
                # adding j back, into j +1 position 
                copy_lst[j+1] = temp
            j += 1
        i += 1
    return copy_lst



def merge_sort(lst):
    """
    TODO (Student):
    Implement Merge Sort.

    Requirements:
    - Use recursion.
    - Divide the list into smaller halves.
    - Sort each half recursively.
    - Merge the sorted halves together.
    - Return the sorted list.
    - Add meaningful comments.

    """
    #Creating a copy of lst to sort 
    copySortList = list(lst)
    # defineing the bounds of the list
    
    if 1 < len(lst):
        # Finding the middle of the list 
        mid  = len(lst) // 2

        #Sperating into to lst int two seperate lists 
        left = copySortList[:mid] 
        right = copySortList[mid:]

        # Recursivly Sorting the left and right lists 
        left = merge_sort(left)
        right = merge_sort(right)

        # Merging the sorted left and right lists 
        return merge(left, right)
    return copySortList


def merge(left, right):
    """
    TODO (Student):
    Implement the merge step used by Merge Sort.

    Requirements:
    - Compare values from the left and right lists.
    - Build a new sorted result list.
    - Append any remaining values.
    - Return the merged sorted list.
    - Add meaningful comments.
    """
    #Creating a merged numers lst 
    mergedNumbers =[]
    # Defining the positions theat we will compare in each sorted list 
    leftPos = 0 
    rightPos = 0 

    # This while loop will contiue checking comparing values till one list is empty 
    while leftPos < len(left) and rightPos < len(right):
        # checking whether the value whether leftPos or rightPos is smaller and appending to the merged list
        # is Leftpos smaller?
        if left[leftPos] < right[rightPos]:
            # append the value of leftpos to mergedNumbers 
            mergedNumbers.append(left[leftPos])
            # increment the position of leftpos
            leftPos += 1
        # the value or right post is smaller
        else:
            # append the value of rightpos to mergedNumbers
            mergedNumbers.append(right[rightPos])
            # Increment the position of rightpos 
            rightPos += 1
    # Iterates if the right list is empty 
    while leftPos < len(left):
        # appends leftpos to mergedNumbers
        mergedNumbers. append(left[leftPos])
        # Increments the position of leftpos
        leftPos += 1
    # Iterates if the left list is empty 
    while rightPos <len(right):
        # appends right pos to merged Numbers 
        mergedNumbers.append(right[rightPos])
        # Incremetns the position of rightpos
        rightPos += 1
    return mergedNumbers


def main():
    print("=== UNIT 7: SORTING ALGORITHMS ===")

    # ===============================
    # TODO (Student): DATASET #1
    # ===============================
    #
    # Requirements:
    # 1. Create an unsorted list containing at least 7 values.
    # 2. Display the original list.
    # 3. Sort the list using Bubble Sort.
    # 4. Sort the same list using Merge Sort.
    # 5. Clearly label and display all results.

    print("\n=== DATASET #1 ===")
    print("TODO: Create an unsorted dataset and test both sorting algorithms.")

    # Creaiting an unsorted list of ids 
    ids = [1,3,53,7,34,4,57,43,4634,64,634]

    # displying the original list 
    print(f"THe original ID list is {ids}")

    # sorting using bubble 
    print(f"The list of IDs sorted using bubble sort: {bubble_sort(ids)}")

    # sorting  using merge sort 
    print(f"The list of IDs sorted using merge sort: {merge_sort(ids)}")




    # ===============================
    # TODO (Student): DATASET #2
    # ===============================
    #
    # Requirements:
    # 1. Create a second dataset.
    # 2. Use different values than Dataset #1.
    # 3. Sort using both algorithms.
    # 4. Compare the results.

    print("\n=== DATASET #2 ===")
    print("TODO: Create a second dataset and compare sorting results.")

    #creating a second data set with string values insted of ints 
    studentNames = ["john","cat","henry","bob","amy","george","jacob"]

    # print the current list of student names 
    print(f"the students enrolled in python are: {studentNames}")
    
    # Sorting the students names with bubble sort 
    print(f"The sorted (bubble sort) list of students for roll call is: {bubble_sort(studentNames)} ")

    # Sorting the students names with merge sort 
    print(f"The sorted (merge sort) list of students for roll call is: {merge_sort(studentNames)} ")





    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Empty list
    # - Already sorted list
    # - Reverse-sorted list
    # - List with duplicate values
    # - Single-element list
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASE TESTS ===")
    print("TODO: Demonstrate and explain edge cases.")

    # Testing the edge case emtpy list 
    print("Edge Case: Empty List")

    # Creating the empty list 
    emptyList = []

    # Displaying the empty list 
    print(f"the contents of the list: {emptyList}")

    #Testing bubble sort on an empty list 
    # Bubble sort wil just return the empty list, becuse there is nothing to iterate on.
    print(f"the output of bubble sorting a emptiy list is:{bubble_sort(emptyList)}")

    #Testing merge sort on an empty list 
    # Becuse there is only one element in the list, the loop inside the function dont run and just return the list 

    print(f"the output of merge sorting a emptiy list is:{merge_sort(emptyList)}")

    #----------------------------------------------------------------------------------------
    # Testing the edge case of an single element list 
    print("Edge Case: One element list")
    # Creating the one element list 
    oneList = [1]

    # displaying the one element list 
    print(f"Displaing the list: {oneList}")

    # Testing bubble sort one the one element list 
    # Becuse there is only one element in the list, the loop inside the function dont run and just return the list 
    print(f"The output of bubble sorting a one element list {bubble_sort(oneList)}")

    #Testing merge sort on the one element list 
    # Becuse there is only one element in the list, the loop inside the function dont run and just return the list 
    print(f"The output of merge sorting a one element list: {merge_sort(oneList)}")


if __name__ == "__main__":
    main()