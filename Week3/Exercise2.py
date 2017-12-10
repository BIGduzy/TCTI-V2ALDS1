class ListNode:
    def __init__(self,data, next_node):
        self.data = data
        self.next = next_node

    def __repr__(self):
        return str(self.data)


class MyCircularLinkedList:
    def __init__(self):
        self.tail = None

    def __repr__(self):
        s = ''
        if not self.tail:
            return "empty list"

        current = self.tail.next

        if current:
            s = str(current)
            current = current.next

            while current is not None and current != self.tail.next:  # while not looped
                s += " -> " + str(current)
                current = current.next

        return s

    def append(self, e):
        if not self.tail:
            self.tail = ListNode(e, None)
            self.tail.next = self.tail
        else:
            self.tail.next = ListNode(e, self.tail.next)
            self.tail = self.tail.next

    def delete(self, e):
        if self.tail:
            if self.tail.data == e:
                if self.tail.next == self.tail:
                    self.tail = None
                else:
                    current = self.tail
                    while current.next is not self.tail:
                        current = current.next

                    current.next = self.tail.next
                    self.tail = current

            else:
                current = self.tail
                while current.next is not self.tail and current.next.data != e:
                    current = current.next

                if current.next.data == e:
                    current.next = current.next.next
                    self.tail = current


if __name__ == '__main__':
    my_list = MyCircularLinkedList()
    print(my_list)
    my_list.append(1)
    my_list.append(2)
    my_list.append(3)
    my_list.append(4)
    print(my_list)
    print('-------')

    my_list.delete(4)
    print(my_list)
    print('------- ^ 4 deleted')
    my_list.delete(1)
    print(my_list)
    print('------- ^ 1 deleted')
    my_list.delete(3)
    print(my_list)
    print('------- ^ 3 deleted')
    my_list.delete(2)
    print(my_list)
    print('------- ^ 2 deleted')

