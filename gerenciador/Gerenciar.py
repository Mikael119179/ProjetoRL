import heapq

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Task:
    def __init__(self, title, description, priority):
        self.title = title
        self.description = description
        self.priority = priority

    def __lt__(self, other):
        return self.priority < other.priority

class PriorityQueue:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        heapq.heappush(self.tasks, (task.priority, task))

    def remove_task(self):
        if self.tasks:
            return heapq.heappop(self.tasks)[1]
        else:
            return None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            self.tail.next = new_node
        self.tail = new_node

    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" -> ")
            current_node = current_node.next
        print("None")

    def add_task(self, data):
        self.append(data)

    def remove_task(self, data):
        current_node = self.head
        previous_node = None
        while current_node:
            if current_node.data == data:
                if previous_node:
                    previous_node.next = current_node.next
                else:
                    self.head = current_node.next
                if current_node == self.tail:
                    self.tail = previous_node
                return
            previous_node = current_node
            current_node = current_node.next