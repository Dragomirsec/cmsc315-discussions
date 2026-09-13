"""
=====================================================
UNIT 5 DISCUSSION: SEARCH ALGORITHMS (LINEAR vs BINARY)
=====================================================

INSTRUCTIONS:
In this assignment, you will implement and analyze two
fundamental search algorithms: linear search and binary search.

You will demonstrate your understanding by modifying the
provided code, running experiments on different dataset sizes,
and clearly explaining your results through code comments
and program output.
"""


def linear_search(lst, target):
    """
    TODO (Student):
    Implement a linear search algorithm.

    Requirements:
    - Search the list from beginning to end.
    - Return the index if the target is found.
    - Return -1 if the target is not found.
    - Add comments explaining why linear search
      has O(n) time complexity.
    """
# A liner search functions by itterating through tht whole list 
# and check to see if the value is equal to the target.
# This makes the time complexity of O(n) becuase for every value 
# in the list one operation is preformed.
# The best possible time complesity is O(1), if the target is the first value in the list 
# The worst possible time compelexity is O(n), if target is the last value in the list


    # Creating an interator that will loop through tht list
    for index, value in enumerate(lst):
        # check if the current value is equalt to the targt value 
        if value == target:
            # if the value is found then retuern the index of the value
            return index
     # if the value is not found return the value of -1 
    return -1 
        


def binary_search(lst, target):
    """
    TODO (Student):
    Implement a binary search algorithm.

    Requirements:
    - Assume the list is already sorted.
    - Repeatedly reduce the search space by half.
    - Return the index if the target is found.
    - Return -1 if the target is not found.
    - Add comments explaining how each iteration
      reduces the search space.
    """
    # A Binery serch works by taking a sorted list and checking the middle index value 
    # if that value is equal to the target then the serch is done if not we check if 
    # the middle value is greater or smaller then the target. Either way at this point 
    # if the target is smaller we discard the upper half of the list, if its larger we descard the lower
    # we keep following this proccess till we find the target! With each iteration of this, the list get cut in half.


    # Creating two veriables to hold the low and high index of the list
    # to control the search space of the list
    low = 0
    high = len(lst) - 1

    # this continues the loop until the target value is found or there is now 
    # where left to search in the list
    while high >= low:
        # Creating the mid veriable to hold the middle index of the list
        mid = (high + low) // 2
        # now we will check if the mid value is equal to the target
        # or if the mid value is less than or greater than the target

        # if the value is equal to the target 
        if lst[mid] == target:
            return mid 


        elif lst[mid]< target:
            # if the mid value is less the the target 
            low = mid + 1

        # if the mid value is greater the target value 
        elif lst[mid] > target:
            high = mid - 1

    # if the value is not found return -1 
    return -1



def main():
    print("=== UNIT 5: SEARCH ALGORITHMS ===")

    # ===============================
    # TODO (Student): SMALL DATASET
    # ===============================
    #
    # Requirements:
    # 1. Create a small sorted dataset.
    # 2. Test both linear search and binary search.
    # 3. Search for:
    #    - a value that exists
    #    - a value that does not exist
    # 4. Use comments to clearly explain the results.

    print("\n=== SMALL DATASET TEST ===")
    print("TODO: Create a small dataset and test both searches.")

    # created a small data set of multipes of ten
    ten_values = [10,20,30,40,50,60,70,80,90,100]

    print(f"the data set is {ten_values}")
    # ---- Liner search test --------
    print("\n---- linear search test -----")
    # The linear search function returns the index of the value found 
    #if no value is found -1 is return to indicate that the value is not in the list 

    print("\nserching for a value of 30")
    linear_output = linear_search(ten_values, 30)
    #the search will return the index of 20 from the list
    print(f"the output of the linear search is: {linear_output}")

    print("\nsearching for a non-exsistant value of 1")
    linear_output = linear_search(ten_values, 1)
    # when the function can not find the target value it returns -1
    print(f"the output of the linear search is {linear_output}\n")

    # ---- binery search list --- 
    print("\n---- binery search test -----")

    print("\nserching for a value of 20")
    linear_output = binary_search(ten_values, 20)
    #the search will return the index of 20 from the list
    print(f"the output of the binery search is: {linear_output}")

    print("\nsearching for a non-exsistant value of 1")
    linear_output = binary_search(ten_values, 1)
    # when the function can not find the target value it returns -1
    print(f"the output of the binery search is: {linear_output}")



    # ===============================
    # TODO (Student): LARGE DATASET
    # ===============================
    #
    # Requirements:
    # 1. Create a much larger sorted dataset.
    # 2. Test both search algorithms.
    # 3. Compare the results.
    # 4. Use comments to explain why binary search becomes more
    #    efficient as datasets grow larger.

    print("\n=== LARGE DATASET TEST ===")
    print("TODO: Create a larger dataset and compare results.")
    # Creating the large data set 
    large_data = list(range(100_000))
    print("the data set is a list from 0 to 100,000")

    print("------ linear search test -----")
    #A linear serch is less efficient with larger data sets becuse it iterates through each 
    # value in the list till if finds the target. This means as the input grows so does the time compelxity 
    large_linear_output = linear_search(large_data, 1000)

    print(f"the output of the linear search is: {large_linear_output}\n")

    print("\n------ binery search test -----")
    #A binery search becomes more efficent as the data set grows becuase every times it iterates 
    # it cuts the amount of values it needs to check in half, effectivly discarding half the list.
    large_binery_output = binary_search(large_data,1000)

    print(f"the out put of the binery search is: {large_binery_output}")

    # While in this case the time taken is not very comparable the amount of operation does by each is not
    # the linear search took 1000 opearations to find the index of 1000, while the binary search only took
    # around 17 operations to find the index 1000








    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Empty list
    # - Single-element list
    # - Value not present
    # - Value at the first position
    # - Value at the last position
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASE TESTS ===")
    print("--- empty list test --- .")
    print("linear search ")
    #Creating a empty list
    empty_list =[]
    #Seaching through an emptylist 
    empty_linear_search = linear_search(empty_list, 10)
    # when the function cant find the the target value it will return -1. 
    # when the list is empty, the function cant find the target and returns -1 
    print(f"results of searching an emtpy list for the value of 10: {empty_linear_search} ")
    print("\n binery search")
    empty_binery_search = binary_search(empty_list, 10)
    #The same occures in the binery search as in the linear search 
    print(f"Results of searching an emtpy list for the value of 10: {empty_binery_search}\n ")

    print("----Value at last position -----")
    # both searches will find the value, but depending on the size of the list the 
    # number of operations will differ 
    print("linear search")
    #When searching for the last value, a linear search will look through each value one by one giving it
    # the worst time complexity of O(n)
    last_value_list = [1,2,3,4,5]

    last_linear_search = linear_search(last_value_list,5)

    print(f"The index of the last value in (last_value_list) is:{last_linear_search}")

    print("\n binery search")
    # A binery search will be more effiecent becuse it dosnt half to look through all the elements of the list
    
    last_binery_search = binary_search(last_value_list, 5)

    print(f"The index of the last value in (last_value_list) is:{last_binery_search}")







if __name__ == "__main__":
    main()