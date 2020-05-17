class SLNode:
    def __init__(self, val):
        self.value = val
        self.next = None


class SList:
    def __init__(self):
        self.head = None

    def add_to_front(self, val):
        new_node = SLNode(val)  # create a instance of our class Node using the given value
        current_head = self.head  # save the current head in a variable
        new_node.next = current_head  # set the new node's 'next' to the list's current head
        self.head = new_node  # set list's head to the newly created node
        return self  # return self to allow for chaining

    def print_values(self):
        print('\nSL Values:')
        runner = self.head  # create a pointer to the list's first node
        while runner is not None:  # iterate through runners until end of list
            print(runner.value)  # print the current node's value
            runner = runner.next  # set runner to its neighbor (increment)
        return self

    def add_to_back(self, val):
        if self.head is None:  # if list is empty
            self.add_to_front(val)  # run add_to_front!
            return self     # and don't run the rest of the function

        new_node = SLNode(val)  # create an instance of our class Node using the given value
        runner = self.head  # set an iterator to start at the front of the list
        while (runner.next is not None):  # stop at last node (node with no neighbor)
            runner = runner.next  # increment runner to next node in list
        runner.next = new_node  # set new node as next value for list's last node
        return self

    def remove_from_front(self):
        if self.head is None:  # if list is empty
            return self  # skip the rest of the function!

        runner = self.head  # create an iterator and start at first node
        self.head = runner.next  # set head to equal next value in list
        runner = None  # delete the value
        return self

    def remove_from_back(self):
        if self.head is None:  # if list is empty
            return self  # skip the rest of the function!

        runner = self.head  # create an iterator to start at front of list
        while runner.next is not None:  # stop at last node
            prev_runner = runner  # store runner's current position before we increment
            runner = runner.next  # increment runner to next node in list
        prev_runner.next = None  # set next to None / "unlink" the last node
        runner = None  # delete the value
        return self  # skip the rest of the function!

    def remove_val(self, val):  # remove first node with the given value
        if self.head is None:  # check if list is empty
            return self  # skip the rest of the function!

        runner = self.head  # otherwise, start an iterator at the front of the list

        # if given val is first node:
        if runner.value is val:
            self.remove_from_front()  # run remove_from_front()
            return self  # skip the rest of the function

        # if given val is middle or last node
        prev_runner = runner  # store value of node before match is found at incrementation
        while runner:
            if runner.value is val:
                prev_runner.next = runner.next  # unlink the node and relink next value
                return self
            prev_runner = runner  # store value of node before match is found at incrementation
            runner = runner.next  # increment runner to next node in list
        return self


my_list = SList()
my_list.add_to_front("are").add_to_front("Linked lists").add_to_back("fun!").add_to_back("more").add_to_front("stuff").print_values()
# my_list.remove_from_front().remove_from_back().print_values()
my_list.remove_val("stuff").print_values()