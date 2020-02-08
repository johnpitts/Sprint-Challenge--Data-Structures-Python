from doubly_linked_list import DoublyLinkedList
from doubly_linked_list import ListNode


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.pointer = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        # Here we simply add until filling the RingBuffer
        print(f"{len(self.storage)}, {self.capacity}")
        if len(self.storage) < self.capacity:
            print("whoops")
            self.storage.add_to_tail(item)
            self.pointer = self.storage.head
        # Now we start replacing, instead of adding
        else:
            temp_tail = False
            # the "a" case (at head)
            if self.storage.head == self.pointer:
                self.storage.delete(self.storage.head)
                self.storage.add_to_head(item)
                self.pointer = self.storage.head.next
                print(f"headcase pointer is {self.pointer.value}")
            # the "c" case (at tail)
            elif self.pointer == self.storage.tail:
                # this isn't getting run, bc the middle case isn't doing the pointer right
                self.storage.delete(self.storage.tail)
                self.storage.add_to_tail(item)
                self.pointer = self.storage.head
                print(f"tailcase pointer is {self.pointer.value}")
            # the MIDDLE cases: i have a bug with the pointer here
            else:
                temp = self.pointer.next
                self.pointer.insert_after(item)
                self.storage.delete(self.pointer)
                self.pointer = temp
                print(f"middlecase pointer is {self.pointer.value}")
                self.storage.tail = temp
                self.storage.length += 1
                


    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        the_current_node = self.storage.head

        while the_current_node != None:
            list_buffer_contents.append(the_current_node.value)
            the_current_node = the_current_node.next
        print(f"here: {list_buffer_contents}")
        return list_buffer_contents


# John's Test of Ring Buffer...
# buffer = RingBuffer(3)
# buffer.get()
# buffer.append('a')
# buffer.append('b')
# buffer.append('c')
# buffer.get()
# buffer.append('d')
# buffer.get()
# buffer.append('e')
# buffer.get()
# buffer.append('f')
# buffer.get()
# buffer.append('g')
# buffer.get()
# buffer.append('h')
# buffer.get()


# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
