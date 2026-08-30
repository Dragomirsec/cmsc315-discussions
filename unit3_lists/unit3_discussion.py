

"""
==================================================
Unit 3 DISCUSSION: List Operations (Insert, Delete, Search)
==================================================

INSTRUCTIONS:
This assignment focuses on understanding how lists behave when elements
are inserted, removed, and searched. You will analyze how Python lists
shift elements in memory and how different operations impact performance.
"""


def insert_at(lst, index, value):
    #Q:what happens to existing elements after an insertion occurs?
    #R:The pre existing items in the list will be shifed as if we where working with a java array, each index will increment by 1

    #Q:how insertion performance may vary depending on where the insertion occurs?
    #R: Depending where you insert the value, depends how many operations need to prefromed.
        #Example 1: If you insert a value at the end of a list the complexity will be O(1) which is the best senerio
        # - becuse only one operation is preformed.
        #Example 2: If you insert a value at the begining of the list the complexity grows for each item in the list O(N)
        # ,this is becuse you need to preform an operation for each subsiquent item, to increment its index.

    #Covers the edge case when the list is empty and when an oversized index is called
    if len(lst) == 0 or index >= len(lst):
       lst.append(value)
    #If we are inserting a value somewhare inside the list 
    else:
        lst.insert(index,value)




    """
    TODO (Student):
    Insert a value into the list at the specified index.

    Requirements:
    - Use a list operation to insert the value.
    - Add comments explaining what happens to existing elements
      after an insertion occurs.
    - Use comments to explain how insertion performance may vary depending on
      where the insertion occurs.
    """
    


def delete_at(lst, index):
    #Q:why index validation and safe deletion are important.
    #R: Index validation is important to deal de edge cases gracfuly and not cause an index error
    #R2: Safe deletion is imprtant becuase is for the same resoan, we dont want the program to try and delete an item at an 
    # an invaled index and cause an index error

    if 0 <= index < len(lst): 
        return lst.pop(index)
    return None
        


    """
    TODO (Student):
    Remove and return the value at the specified index.

    Requirements:
    - Validate that the index exists.
    - Return the removed value.
    - Return None if the index is invalid.
    - Add comments explaining why index validation and safe deletion are important.
    """
    


def search_value(lst, value):
   
    #Q: why this is a linear search and why it scans sequentially.
    #R:Python to find the first occurance of a specific value, prforms a comperason for each element in the list 
    # till it finds an occurance or it reaches the end of th list. This is liner becuase for each input(element of the list)
    # one operation is prefromed 
    #R2: It scans sequentially to find the first occurance, what could be at the begining, middle, or end.
    # so it starts at the begining and iterates till if findes the value or the list ends 

    for index, item in enumerate(lst):
        if item == value:
            return index
     
    return -1

 

"""
    TODO (Student):
    Search for a value within the list.

    Requirements:
    - Return the index if the value is found.
    - Return -1 if the value is not found.
    - Add comments explaining why this is a linear search and why it scans sequentially.
    """
    


def main():
    print("=== UNIT 3: LIST OPERATIONS ===")
    print("\n=== INSERTION TESTS ===")
    print("TODO: Create a list and demonstrate insertion.")

    # ===============================
    # TODO (Student): INSERTION TESTS
    # ===============================
    #
    # Requirements:
    # 1. Create a list containing several values.
    # 2. Display the original list.
    # 3. Test insertion at:
    #    - the beginning
    #    - the middle
    #    - the end
    # 4. Display the list after each insertion.
    # 5. Use comments to explain each step in the implementation.

    # Created an Attendance list of which students came to class. And printed out who had arrive so far
    Attendance = ["john","Anthony"]
    print(Attendance)

    # Adding a student to the begining of the list 
    #NOTE:THis has the worst complexity of O(N), becuase each item's index grows by 1 and then the value is assigned 
    insert_at(Attendance, 0 , "taylor")
    print(Attendance)

    # Adding a sutdent to the middle of the list 
    #NOTE: Has the same compexity as adding a studen in the beginging O(N)
    insert_at(Attendance, 1 , "edward")
    print(Attendance)

    # Adding a student to the end of the list
    # In terms of complexity this is the best case senerio of O(1). The value is just inserted at the end of list. 
    insert_at(Attendance, 4 , "jacob")
    print(Attendance)
    



    print("\n=== Deletion TESTS ===")
    print("TODO: Create a list and demonstrate Deletion.")
    # ===============================
    # TODO (Student): DELETION TESTS
    # ===============================
    #
    # Requirements:
    # 1. Delete an item from:
    #    - the beginning
    #    - the middle
    #    - the end
    # 2. Display the removed value.
    # 3. Display the updated list after each deletion.
    # 4. Use comments to clearly explain what is happening in the output.

    # prints a the current list of attendence 
    print(Attendance)

    # Deletes the first student on the attendance list
    #NOTE: All the elements of the attendence list, are iterated down by one 
    #NOTE: Has a complexity of O(N), where N are all the other elements in the list
    # if the list only had one value the complxity would be O(1)
    print(f"The student: {delete_at(Attendance,0)} was removed from the attendence list")
    print (Attendance)
    # Deletes the student in the middle of the attendence list 
    #NOTE: All the elements after the removed index are iterated down by one 
    #NOTE: Has a complexity of O(N), where N is all the lists element after the index
    print(f"The student: {delete_at(Attendance,2)} was removed from the attendence list")
    print (Attendance)
    # Deletes the student at the end fof the attence list 
    #NOTE: Only preforms the deletion operation, the rest of the list stayes the same 
    #NOTE: Has a complexity of O(1). Becuse only one Operation only affects one element 
    print(f"The student: {delete_at(Attendance,2)} was removed from the attendence list")
    print (Attendance)




    print("\n=== SEARCH TESTS ===")
    print("TODO: Demonstrate searching for values.")

    # ===============================
    # TODO (Student): SEARCH TESTS
    # ===============================
    #
    # Requirements:
    # 1. Search for a value that exists.
    # 2. Search for a value that does not exist.
    # 3. Display the search results with clear explanations.
    # 4. Use comments to explain each step.

    #Searching for a value that exsist
    #This will print out the index where john is located in the list
    print("---serching if john is in attendence index---")
    print(f"Results: {search_value(Attendance,'john')}")
    print(Attendance)

    #Serching for a student who is not in attendence 
    # Thiw will return an index of -1 indicating  taylor is not in attendnce
    print("---serching if taylor is in attendence index---")
    print(f"Restults {search_value(Attendance,'taylor')}")
    print(Attendance)





    print("\n=== EDGE TESTS ===")
    print("TODO: Demonstrate at least two edge cases.")

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Delete using an invalid index
    # - Search for a missing value
    # - Insert into an empty list
    # - Delete from an empty list
    # - Use comments to explain each edge case.

    print(f"\n-The current attendence is{Attendance}")
    #deleting at an invalid index
    print(f"\n-Deleting from attendence with invaled index. Result::{ delete_at(Attendance, 10)}")
    #Serching for a missing value
    print(f"\n-Serching for a missing value. Result: {search_value(Attendance,'random')}")

    #declareing an empty attendence list
    emptyattendence = []
    #Inserting into a empty list 
    insert_at(emptyattendence, 20, "benjamin")
    print(f"\n-Adding benjamin to attendence. Attendence: {emptyattendence}")

    #declareing an empty attendence list
    emptyattendence = []
    #Deleting from an empty list 
    print(f"\n-Value deleted from the list is: {delete_at(emptyattendence,10)}\n")
    


    



if __name__ == "__main__":
    main()