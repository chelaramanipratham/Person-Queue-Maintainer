MAX = 10
queue_array = [None] * MAX
rear = -1
front = -1

def queue_insert():
    global rear, front
    if rear == MAX - 1:
        print("Queue Overflow")
    else:
        if front == -1:
            front = 0
        add_item = input("Insert the element in queue: ")
        rear += 1
        queue_array[rear] = add_item
        print("\nElement inserted!")

def queue_delete():
    global front, rear
    if front == -1 or front > rear:
        print("Queue Underflow")
        return
    else:
        print("Element deleted from queue is:", queue_array[front])
        front += 1
        if front == rear + 1:
            front = -1
            rear = -1

def display():
    print("The queue is:", end=" ")
    for i in range(front, rear + 1):
        print(queue_array[i], end=" ")
    print("\n")

def queue_search():
    person = input("Enter name of person you want to search: ")
    print()
    for i in range(front, rear + 1):
        if queue_array[i] == person:
            print("Person is waiting at position:", i + 1)
            return
    print("Person is not in the queue")

def main():
    while True:
        print("1. Add person to queue")
        print("2. Delete person from queue")
        print("3. Display all person in queue")
        print("4. Search for a person in queue")
        print("5. Quit")
        choice = int(input("Enter your choice: "))
        print("\n")
        if choice == 1:
            queue_insert()
        elif choice == 2:
            queue_delete()
        elif choice == 3:
            display()
        elif choice == 4:
            queue_search()
        elif choice == 5:
            break
        else:
            print("Wrong choice")

if __name__ == "__main__":
    main()