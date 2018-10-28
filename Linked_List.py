class Linked_List:
    class __Node:

        def __init__(self, val): #initialize node
            self._val = val         #pass value to node
            self._next = None       #creates attribues next and previous
            self._prev = None


    def __init__(self):
        self._length = 0                    #create attribute for length
        self._header = self.__Node(None)        #create header and trailer nodes
        self._trailer = self.__Node(None)
        self._header._next = self._trailer      #links header and trailer nodes
        self._trailer._next = None
        self._trailer._prev = self._header      #outer bounds of the list are None
        self._header._prev = None


    def __len__(self):
        return self._length     #returns the length of the list, changed when nodes added/removed


    def append_element(self, val):
        new_node = self.__Node(val)     #creates a new node and passes the value
        new_node._prev = self._trailer._prev        #links the new node to previvous node of trailer
        self._trailer._prev = new_node              #makes new node the previous to trailer
        new_node._prev._next = new_node             #links the node behind the new node to new node
        new_node._next = self._trailer              #links new node to trailer
        self._length = self._length + 1             #increments size


    def insert_element_at(self, val, index):
        if index >= len(self) or index < 0:     #tests if valid index
            raise IndexError
        new_node = self.__Node(val)         #creates new node and passes value
        if int(len(self)/2) > index:        #tests to see if inserting in front or back half of list to save time
            current = self._header   #creates temp pointer to walk through list
            current_index = -1      #index of temp pointer
            while current_index < index - 1:    #walks pointer through list until in correct location
                current = current._next         #moves pointer to next
                current_index = current_index + 1   #increments pointer index
            current._next._prev = new_node      #inserts node
            new_node._prev = current
            new_node._next = current._next
            current._next = new_node
        else:                               #triggers when the index in in back half of list
            current = self._trailer             #same process as above but walks backward
            current_index = len(self)
            while current_index > index - 1:
                current = current._prev
                current_index = current_index - 1
            current._next._prev = new_node
            new_node._prev = current
            new_node._next = current._next
            current._next = new_node
        self._length = self._length + 1        #increments length to reflect new node


    def remove_element_at(self, index):
        if index >= len(self) or index < 0:     #tests if valid index
            raise IndexError
        if int(len(self)/2) > index:        #tests for first half of list
            current = self._header          #temp walking pointer
            current_index = -1
            while current_index < index:    #walks pointer through list
                current = current._next
                current_index = current_index + 1
            return_val = current._val       #stores value of node to return before it is removed
            current._next._prev = current._prev
            current._prev._next = current._next  #patches hole where the node previously was
            self._length = self._length - 1   #decrements length to refelct removed node
            return return_val       #returns value of removed node
        else:
            current = self._trailer     #same as above but for walking backwards
            current_index = len(self)
            while current_index > index:
                current = current._prev
                current_index = current_index - 1
            return_val = current._val
            current._next._prev = current._prev
            current._prev._next = current._next
            self._length = self._length - 1
            return return_val


    def get_element_at(self, index):
        if index >= len(self) or index < 0: #checks for valid index
            raise IndexError
        if int(len(self)/2) > index:    #creates walking pointer for first half of list
            current = self._header
            current_index = -1
            while current_index < index: #walks pointer to desited node
                current = current._next
                current_index = current_index + 1
            return current._val     #returns node value
        else:
            current = self._trailer #same as above but for backwards walking
            current_index = len(self)
            while current_index > index:
                current = current._prev
                current_index = current_index - 1
            return current._val


    def rotate_left(self):
        if len(self) == 0:
            return
        temp_value = self._header._next._val    #temp storage of the value of the moving node
        self._header._next._next._prev = self._header   #Makes the previously second node in list the first one
        self._header._next = self._header._next._next
        self._length = self._length - 1     #decrements list to reflect the dropped node
        self.append_element(temp_value)     #appends a new node to the end of list using the stored value


    def __str__(self):
        to_return = '[ '     #creates string and opening bracket
        current = self._header._next    #puts the waling pointer on the first node
        while current._next is not None:    #walks to the end of the list, breaks on trailer node or when the break condition is met
            to_return += str(current._val)     #adds string of current node value to return string
            if current._next._next == None:     #checks node two ahead of current to see when last term will be reached
                break                           #breaks loop when second to last node is reached, prevents trailer and last comma from printing
            to_return += ", "                   #adds comma and space between nodes in the list
            current = current._next             #increments node through list
        if len(self)==0:
            to_return += ']'
        else:
            to_return += ' ]'     #adds closing bracket
        return to_return    #returns final created string


    def __iter__(self):
        self._iter = self._header._next #creates iteration pointer on first node containing a value
        return self     #returns the iteration


    def __next__(self):
        if self._iter._next is not None:        #runs until the trailer node is reached
            node_value = self._iter._val        #stores node value
            self._iter = self._iter._next       #iterates to next node
            return node_value                   #returns node value
        else:
            raise StopIteration                 #stops iteration when the If statement is broken (end of list)


if __name__ == '__main__':
    ll = Linked_List()
    try:
        ll.insert_element_at(0,0)
    except IndexError:
        print("Cannot insert to empty List")
    print("currentrent length: ", len(ll))
    print(ll,'1')
    try:
        print(ll.get_element_at(0))
    except IndexError:
        print("Invalid Index, no value to read")
    try:
        ll.rotate_left()
    except IndexError:
        print("Cannot rotate empty list")
    try:
        ll.remove_element_at(0)
    except IndexError:
        print("Cannot remove from empty list")


    ll.append_element(0)
    print("New length: ", len(ll))
    print(ll,'2')
    try:
        ll.insert_element_at(1,1)
    except IndexError:
        print("Cannot append 1 to end of list")
    print(ll,'3')
    try:
        print(ll.get_element_at(0))
    except IndexError:
        print("Invalid Index, no value to read")
    try:
        ll.rotate_left()
    except IndexError:
        print("Cannot rotate empty list")
    print(ll,'4')
    try:
        ll.remove_element_at(0)
    except IndexError:
        print("Cannot rotate empty list")
    print(ll,'5')



    ll.append_element(0)
    ll.append_element(1)
    print(ll)
    try:
        ll.insert_element_at(2,0)
        print("insert 2 at position 0")
    except IndexError:
        print("Cannot append to end of list")
    print("New length: ", len(ll))
    print(ll)
    try:
        ll.remove_element_at(30)
    except IndexError:
        print("Cannot remove from this Index (30)")
    try:
        print("Remove element at pos 1")
        ll.remove_element_at(1)
    except IndexError:
        print("Cannot remove from this Index (1)")
    print("New length: ", len(ll))
    print(ll)
    ll.append_element('Data')
    print("New length: ", len(ll))
    print(ll)
    print("iteration over the list:")
    for element in ll:
        print(element)
