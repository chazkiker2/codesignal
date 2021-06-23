class Stack:
    # This stack is a FIFO data structure
    # implemented with a List
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, value):
        # add to end of list
        self.items.append(value)

    def pop(self):
        # remove from end of list
        return self.items.pop()


# queues represent LIFO data structures
def queue_on_stacks(requests):
    # prev is our permanent storage
    # each time an element is inserted, it will go on top of prev stack
    # BOTTOM of prev stack = FIRST IN
    # TOP of prev stack = LAST IN
    left = Stack()

    # next is our temporary storage
    # every time we remove an element from our queue_on_stacks storage,
    # we are looking to remove and return the element at the BOTTOM
    # of the LEFT STACK
    #
    # each time an element is removed, prev will move each element over
    # one by one from the top of the prev stack to the top of the next stack
    # until prev stack is empty.
    #
    # then make a copy of TOP of next stack
    right = Stack()

    def insert(x):
        left.push(x)

    def remove():
        while not left.isEmpty():
            right.push(left.pop())

        to_return = right.pop()


    ans = []
    for request in requests:
        req = request.split(" ")
        if req[0] == "push":
            insert(int(req[1]))
        else:
            ans.append(remove())
    return ans
