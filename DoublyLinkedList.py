class Node:
    def __init__(self, data, next_node=None, prev_node=None):
        self.data = data
        self.next = next_node
        self.prev = prev_node


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def append(self, data):
        new_node = Node(data)

        if self.is_empty():
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next

            current.next = new_node
            new_node.prev = current

    def prepend(self, data):
        new_node = Node(data)

        if self.is_empty():
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def insert_after(self, prev_node, data):
        if prev_node is None:
            return

        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node
        new_node.prev = prev_node

        if new_node.next.prev:
            new_node.next.prev = new_node

    def insert_at_index(self, index, data):
        if index < 0:
            print("Invalid index!")
            return

        new_node = Node(data)

        if index == 0:
            self.prepend(data)
        else:
            current = self.head
            current_index = 0

            while current and current_index < index - 1:
                current = current.next
                current_index += 1

            if not current:
                print("Index out of range!")
                return

            new_node.next = current.next
            new_node.prev = current
            current.next = new_node

            if new_node.next:
                new_node.next.prev = new_node

    def delete(self, data):
        current = self.head

        while current:
            if current.data == data:
                if current.prev:
                    current.prev.next = current.next
                else:
                    self.head = current.next

                if current.next:
                    current.next.prev = current.prev

                return

            current = current.next

    def display(self):
        current = self.head

        while current:
            print(current.data, end=" ")
            current = current.next

        print()


dll = DoublyLinkedList()

# Append elements
dll.append(10)
dll.append(20)
dll.append(30)

# Prepend an element
dll.prepend(5)

# Insert after a specific node
node = dll.head.next  # Second node with data 20
dll.insert_after(node, 25)

# Display the list
dll.display()

# Delete an element
dll.delete(20)

# Display the updated list
dll.display()

# Insert at index
dll.insert_at_index(1, 15)

# Display the list
dll.display()
