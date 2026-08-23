"""
===========================================================
UNIT 2 DISCUSSION: STACKS AND QUEUES (PYTHON)
===========================================================

OVERVIEW:
This assignment introduces two fundamental data structures:
the Stack (LIFO) and the Queue (FIFO).

You will complete, modify, and extend the starter code while
explaining key concepts through comments and improved output.
"""

from collections import deque


class Stack:
    def __init__(self):
        # TODO (Student): Create the internal data structure for the stack.
        # Hint: A Python list can be used to store stack values.
        self.stack =  []


    def push(self, value):
        # TODO (Student): Add value to the stack.
        # Add a short comment explaining why this operation supports LIFO behavior.

        # this operation supports LIFO becuse it appends a value to the end of the list
        # the end of the list or the most right value of the list is the top of the stack 
        # this index wil be len(self.stack)-1 
        self.stack.append(value)

    def pop(self):
        # TODO (Student): Remove and return the most recently added value.
        # Improve or explain empty-stack handling.
        # What should happen if the stack is empty?

        # if the stack is empty print out to console that the stack is empty
        # it important to consider these edge cases,
        # so that the program has a graceful way to deal with it. insted of bracking the program
        
        if len(self.stack) == 0:
              print("Stack empty")
            
    

        
        else:
             popped = self.stack.pop(-1)
             print(f"Poped:{popped}")
             return popped
            

    def peek(self):
        # TODO (Student): Return the top value without removing it.
        # Add a comment explaining what peek does.

        # Peeking looks at the value at the top of the stack without affecting the stack 
        # if the length is 0 thow an error
        if len(self.stack) == 0:
            print("Stack empty")

        else:
            top_value = self.stack[-1]
            return top_value

    def is_empty(self):
        # TODO (Student): Return True if the stack has no values.

            return len(self.stack) ==0
        


class Queue:
    def __init__(self):
        # TODO (Student): Create the internal data structure for the queue.
        # Hint: collections.deque is useful for efficient queue operations.

        self.queue = deque()

    def enqueue(self, value):
        # TODO (Student): Add value to the back of the queue.
        # Add a short comment explaining why this operation supports FIFO behavior.

        #this operation supports FIFO becuse this adds a value to the back of the queue 
        self.queue.append(value)
        

        

    def dequeue(self):
        # TODO (Student): Remove and return the value from the front of the queue.
        # Explain or improve empty-queue handling.

        # We add and if statemnt to catch the edge case: when the queue is empty so the program has a gracefule way to handle it. 
        if len (self.queue) == 0:
            print("The queue is Empty!")
        
        else:
             dequeue1 =self.queue.popleft()
             print(f"Popped:{dequeue1}")
             return dequeue1
            
        

    def front(self):
        # TODO (Student): Return the front value without removing it.
        # Add a comment explaining what front returns.

        # the front method returns the value that is in the front of the queue without affecting the queue 

        if len (self.queue) == 0:
            print("The queue is Empty!")
        
        else:
            return self.queue[0]
        

    def is_empty(self):
        # TODO (Student): Return True if the queue has no values.
        return len (self.queue) == 0


def main():
    print("=== UNIT 2: STACKS AND QUEUES ===")

    # ===============================
    # TODO (Student): STACK DEMO
    # ===============================
    # Requirements:
    # 1. Create a Stack object.
    # 2. Add at least 4 values to the stack.
    # 3. Improve the print statements so they clearly explain what is happening.
    # 4. Demonstrate LIFO behavior.
    # 5. Show what happens when pop() is used on an empty stack.
    #
    # Edge Cases:
    # 6. Show what happens when peek() is used on an empty stack.
    # 7. Create a stack with only one item, remove it,
    #    and verify the stack is empty afterward.


print("\n=== STACK DEMO ===")
print("TODO: Create a Stack object, demonstrate LIFO behavior, senerio: dishses,")


# Creates a stack object named cool stack 
dishstack = Stack()

# Added four values the the stack object cool stack 
dishstack.push("dish1")
dishstack.push("dish2")
dishstack.push("dish3")
dishstack.push("dish4")

# Printing out an explenation of the stack
top_dishstack = dishstack.stack[-1]
bottom_dishstack = dishstack.stack[0]
print("Created the dish stack object and added four dishes to the stack")
print(f"The dishes in the stack are {dishstack.stack}, where {top_dishstack} is the top dish and {bottom_dishstack} is the bottom dish.")
print("Now we will pop all the values and see what happens when we pop when the stack is empty")
# first time poping the top value and printing the stack
dishstack.pop()

print(dishstack.stack)

# Second time poping the top value and printing the stack
dishstack.pop()

print(dishstack.stack)

# Third time poping the top value and printing the stack
dishstack.pop()

print(dishstack.stack)

# Fourth time poping the top value and printing the stack
dishstack.pop()

print(dishstack.stack)

#poping the empty stack 
dishstack.pop()

print("\n now we will try to look at the name of the top dish when the stack is empty!")
#peeking the empty stack. WIll print out that the stack is empty 
dishstack.peek()


print("Now we will test if a single- dish stack becomes empty after removing a dish.")
# Creating the stsck obejct
newdishstack = Stack()

# adding the value of 102 to the stack 
newdishstack.push("cooldish")

# Removing 102 from the stack
print(newdishstack.stack)
newdishstack.pop()

#

# print a ture or false statemnt if the list is empty 
value1 = newdishstack.is_empty()

print(f"Is the single-item dish stack empty after removel:{value1}")



# ===============================
# TODO (Student): QUEUE DEMO
# ===============================
# Requirements:
# 1. Create a Queue object.
# 2. Add at least 4 values to the queue.
# 3. Improve the print statements so they clearly explain what is happening.
# 4. Demonstrate FIFO behavior.
# 5. Show what happens when dequeue() is used on an empty queue.
#
# Edge Cases:
# 6. Show what happens when front() is used on an empty queue.
# 7. Create a queue with only one item, remove it,
#    and verify the queue is empty afterward.

print("\n=== QUEUE DEMO ===")
print("Create a Queue object, demonstrate FIFO behavior, senerio:Register line")

#Creating a queue object
Registerqueue = Queue()

# adding four values to the Registerqueue
Registerqueue.enqueue("henry")
Registerqueue.enqueue("tony")
Registerqueue.enqueue("bob")
Registerqueue.enqueue("alice")

head = Registerqueue.queue[0]
bottom = Registerqueue.queue[-1]
print("Created the regester queue object and enqueued four people to queue")
print(f"The pepole in the queue are {Registerqueue.queue}, where {head} is the first in line and {bottom} is the last in line.\n")
print("Now we will remove all the people and see what happens when the queue is empty")

#first time dequeueing and printing out the queue 
Registerqueue.dequeue()
print(Registerqueue.queue)

#Second time dequeueing and printing out the queue 
Registerqueue.dequeue()
print(Registerqueue.queue)

#Third time dequeueing and printing out the queue 
Registerqueue.dequeue()
print(Registerqueue.queue)

#Fourth time dequeueing and printing out the queue 
Registerqueue.dequeue()
print(Registerqueue.queue)

#deqeueing an empty queue
Registerqueue.dequeue()

print("\n now we will try looking at the front of the empty regsister queue:")

# tring to queue an empty queue
Registerqueue.front()

print("Now we will check to see if the queue is empty after removeing a person.")

#creating a new queue object 
newqueue = Queue()

#adding a single value to the queue 
newqueue.enqueue("john")

#removing all values from the queue
print(newqueue.queue)
newqueue.dequeue()

# print a ture or false statemnt if the list is empty 
value2 =newqueue.is_empty()

print(f"Is the single-item queue empty after removel:{value2}")

if __name__ == "__main__":
    main()
