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
print("TODO: Create a Stack object, demonstrate LIFO behavior,")


# Creates a stack object named cool stack 
coolstack = Stack()

# Added four values the the stack object cool stack 
coolstack.push(10)
coolstack.push(11)
coolstack.push(12)
coolstack.push(13)

# Printing out an explenation of the stack
top_coolstack = coolstack.stack[1]
bottom_coolstack = coolstack.stack[0]
print("Created the stack object and pused four values to the stack")
print(f"The values in the stack are {coolstack.stack}, where {top_coolstack} is the top and {bottom_coolstack} is the bottom.")
print("Now we will pop all the values and see what happens when we pop when the stack is empty")
# first time poping the top value and printing the stack
coolstack.pop()

print(coolstack.stack)

# Second time poping the top value and printing the stack
coolstack.pop()

print(coolstack.stack)

# Third time poping the top value and printing the stack
coolstack.pop()

print(coolstack.stack)

# Fourth time poping the top value and printing the stack
coolstack.pop()

print(coolstack.stack)

#poping the empty stack 
coolstack.pop()

print("\n now we will try to peek at the emptystack and see the output:")
#peeking the empty stack. WIll print out that the stack is empty 
coolstack.peek()


print("Now we will test if a single-item stack becomes empty after removal.")
# Creating the stsck obejct
newstack = Stack()

# adding the value of 102 to the stack 
newstack.push(102)

# Removing 102 from the stack
print(newstack.stack)
newstack.pop()

#

# print a ture or false statemnt if the list is empty 
value1 = newstack.is_empty()

print(f"Is the single-item stack empty after removel:{value1}")



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
print("Create a Queue object, demonstrate FIFO behavior,")

#Creating a queue object
coolqueue = Queue()

# adding four values to the coolqueue
coolqueue.enqueue(101)
coolqueue.enqueue(102)
coolqueue.enqueue(103)
coolqueue.enqueue(104)

head = coolqueue.queue[0]
bottom = coolqueue.queue[-1]
print("Created the queue object and enqueued four values to queue")
print(f"The values in the queue are {coolqueue.queue}, where {head} is the top and {bottom} is the bottom.\n")
print("Now we will dequeue all the values and see what happens when we dequeue when the stack is empty")

#first time dequeueing and printing out the queue 
coolqueue.dequeue()
print(coolqueue.queue)

#Second time dequeueing and printing out the queue 
coolqueue.dequeue()
print(coolqueue.queue)

#Third time dequeueing and printing out the queue 
coolqueue.dequeue()
print(coolqueue.queue)

#Fourth time dequeueing and printing out the queue 
coolqueue.dequeue()
print(coolqueue.queue)

#deqeueing an empty queue
coolqueue.dequeue()

print("\n now we will try looking at the front of an empty queue:")

# tring to queue an empty queue
coolqueue.front()

print("Now we will test if a single-item queue becomes empty after removal.")

#creating a new queue object 
newqueue = Queue()

#adding a single value to the queue 
newqueue.enqueue(10)

#removing all values from the queue
print(newqueue.queue)
newqueue.dequeue()

# print a ture or false statemnt if the list is empty 
value2 =newqueue.is_empty()

print(f"Is the single-item queue empty after removel:{value2}")

if __name__ == "__main__":
    main()
