class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def display(self):
        """Displays the contents of the linked list."""
        current = self.head
        if not current:
            print("Linked List is empty.")
            return
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def insert_at_end(self, data):
        """Inserts a new node at the end of the list."""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def insert_at_position(self, data, position):
        """Inserts a new node at a specified position (0-based index)."""
        new_node = Node(data)
        if position == 0:
            new_node.next = self.head
            self.head = new_node
            return
        current = self.head
        count = 0
        while current and count < position - 1:
            current = current.next
            count += 1
        if not current:
            print("Position out of range.")
            return
        new_node.next = current.next
        current.next = new_node

    def delete_node(self, key):
        """Deletes the first node with the given value."""
        current = self.head

        if not current:
            print("List is empty.")
            return

        if current.data == key:
            self.head = current.next
            return

        prev = None
        while current and current.data != key:
            prev = current
            current = current.next

        if not current:
            print(f"Node with value {key} not found.")
            return

        prev.next = current.next


# Example usage
if __name__ == "__main__":
    ll = LinkedList()
    ll.insert_at_end(10)
    ll.insert_at_end(20)
    ll.insert_at_end(30)
    ll.insert_at_position(15, 1)
    ll.display()
    ll.delete_node(20)
    ll.display()
