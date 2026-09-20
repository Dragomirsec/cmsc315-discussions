

"""
====================================================
UNIT 6 DISCUSSION: Python Dictionaries as Hash Tables
====================================================

INSTRUCTIONS:
In this activity, you will work with Python dictionaries
to simulate the behavior of a hash table.

You will modify the provided starter code to demonstrate
common operations and explain key concepts.

Follow all TODO prompts in the code and ensure your output
clearly communicates what your program is doing at each step.

----------------------------------------------------
"""


def main():
    print("=== UNIT 6: DICTIONARIES AS HASH TABLES ===")

    # ===============================
    # TODO (Student): CREATE A HASH TABLE
    # ===============================
    #
    # Requirements:
    # 1. Create an empty dictionary.
    # 2. Add at least 5 key-value pairs.
    # 3. Add comments explaining how a dictionary
    #    behaves like a hash table.
    # 4. Display the contents of the dictionary.


    print("\n=== INSERT OPERATIONS ===")
    print("TODO: Create a dictionary and add multiple key-value pairs.")

    #Creating an emtpy deictionary of usernames and passwords 
    users ={ }
    # adding five users with hashed passwords 
    users["john"] = "password"
    users["cat"] = "meow"
    users["henry"] = "gatso"
    users["fernando"] = "fernando"
    users["Edward"] = "admin123"
    users["james"] = "default"

    #printing every key value Pairs 
    for key, value in users.items():
        print(f"{key}:{value}")

     # In python a dictionary is basically a simple hash table,
     # where the key value pairs are placed in hashed value of the key.
     # When we use .values() and .keys() python iterates over the dictionary
     # and converts it into a list to return the values.
     # For this reason one might thing that a dictionary is different form a hash table
     # when in reality they are the something 




    # ===============================
    # TODO (Student): LOOKUP OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Retrieve at least two existing keys.
    # 2. Clearly display the lookup results.
    # 3. Add meaningful comments to explain how the lookup works.

    print("\n=== LOOKUP OPERATIONS ===")
    print("TODO: Demonstrate successful key lookups.")

    # As we established earlier, a dictionary is a hash table!
    # following that logic, the dictionary runs a hash on the username 
    # which finds its location in memory, which then the value can be retrived 
    value0 = users.get("john")
    value1 = users.get("fernando")

    print(f"john:{value0}")
    print(f"fernando:{value1}")

    # ===============================
    # TODO (Student): UPDATE OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Update the value associated with an existing key.
    # 2. Display the dictionary before and after the update.
    # 3. Use comments to explain what happens when an existing key is assigned
    #    a new value.

    print("\n=== UPDATE OPERATIONS ===")
    print("TODO: Demonstrate updating an existing key.")

    print(f'Johns password before updating: {users["john"]}')
    # to update a single value in the dictionary we use the same 
    # method we used to insert a value. 
    users["john"] = "bad password"
    # when we updated the value of john the privous key was overwritten 
    # in other words the value was deleted and replaced 

    print(f'Johns password after updating: {users["john"]}')




    # ===============================
    # TODO (Student): DELETE OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Delete at least one key-value pair.
    # 2. Display the dictionary before and after deletion.
    # 3. Use comments to explain what happens when a key is removed.

    print("\n=== DELETE OPERATIONS ===")
    print("TODO: Demonstrate deleting a key-value pair.")

    print("the list of users before deleteing john")
    print(users.items())
    # deleteing john
    users.pop("john")

    print("\n the lsit of users after deleting john ")
    print(users.items())
    # when a key is reoved form  a dictionary, the key and value are remvoed
    # and are marked as removed. But all of the hash table logic is hidden behind the abstraction 
    # of the dictionay data type.






    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Lookup a missing key
    # - Delete a missing key safely
    # - Update a missing key
    # - Use an empty dictionary
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASES ===")
    print("TODO: Demonstrate and explain edge cases.")

    ## looking up a missing value will result in the program to stop and it will 
    ## throw an error keyerror becuase it coulnd find the key garry 
    print("LOOKING UP A MISSING KEY\n")
    print(f"the current dict is {users.items()}")
    print(f"looking up the missing key garry:{users["garry"]}")

    # updating a value for a missing key will simply add that key to the list 
    print("UPDATING A MISSING KEY")
    print(f"the current list is {users.items()} and we are updating garry ")
    users.update({"garry":"1232"})


if __name__ == "__main__":
    main()