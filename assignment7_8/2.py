class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)
        print(f"Enqueued: {item}")

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty, cannot dequeue.")
        else:
            removed_item = self.queue.pop(0)
            print(f"Dequeued: {removed_item}")
            return removed_item
        
    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)

    def peek(self):
        if self.is_empty():
            print("Queue is empty.")
        else:
            print(f"Front element: {self.queue[0]}")
            return self.queue[0]
        
queue = Queue()

while True:
    print("\nQueue Operations Menu:")
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Peek")
    print("4. Check if Queue is Empty")
    print("5. Get Queue Size")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == '1':
        item = input("Enter an element to enqueue: ")
        queue.enqueue(item)

    elif choice == '2':
        queue.dequeue()

    elif choice == '3':
        queue.peek()

    elif choice == '4':
        if queue.is_empty():
            print("Queue is empty.")
        else:
            print("Queue is not empty.")

    elif choice == '5':
        print(f"Queue size: {queue.size()}")

    elif choice == '6':
        print("Exiting the program.")
        break

    else:
        print("Invalid choice, please try again.")