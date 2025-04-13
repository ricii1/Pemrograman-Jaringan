# Struktur Data di Python - Contoh Implementasi

# 1. List
print("=== List ===")
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")
fruits.remove("banana")
print("List hasil:", fruits)
print("Elemen pertama:", fruits[0])

# 2. Tuple
print("\n=== Tuple ===")
coordinates = (10.0, 20.0)
print("Tuple:", coordinates)
print("Koordinat Y:", coordinates[1])

# 3. Set
print("\n=== Set ===")
numbers = {1, 2, 3}
numbers.add(4)
numbers.discard(2)
print("Set hasil:", numbers)
print("Apakah 3 ada di set?", 3 in numbers)

# 4. Dictionary
print("\n=== Dictionary ===")
person = {"name": "Alice", "age": 25}
person["city"] = "Jakarta"
print("Dictionary:", person)
print("Nama:", person["name"])

# 5. Deque
print("\n=== Deque ===")
from collections import deque
dq = deque()
dq.append("a")
dq.appendleft("b")
print("Deque setelah append:", dq)
dq.pop()
dq.popleft()
print("Deque setelah pop:", dq)

# 6. Stack (menggunakan list)
print("\n=== Stack ===")
stack = []
stack.append("a")
stack.append("b")
print("Stack sebelum pop:", stack)
print("Pop:", stack.pop())
print("Stack setelah pop:", stack)

# 7. Queue (menggunakan deque)
print("\n=== Queue ===")
queue = deque()
queue.append("a")
queue.append("b")
print("Queue sebelum dequeue:", queue)
print("Dequeue:", queue.popleft())
print("Queue setelah dequeue:", queue)

# 8. Priority Queue
print("\n=== Priority Queue ===")
import heapq
pq = []
heapq.heappush(pq, 3)
heapq.heappush(pq, 1)
heapq.heappush(pq, 2)
print("Isi priority queue (heap):", pq)
print("Pop elemen prioritas:", heapq.heappop(pq))

# 9. Array (modul array)
print("\n=== Array ===")
import array
arr = array.array('i', [1, 2, 3])
arr.append(4)
print("Array:", arr)
print("Elemen pertama array:", arr[0])

# 10. Circular Queue (Custom)
print("\n=== Circular Queue ===")

class CircularQueue:
    def __init__(self, size):
        self.queue = [None] * size
        self.head = self.tail = -1
        self.size = size

    def enqueue(self, data):
        if (self.tail + 1) % self.size == self.head:
            print("Queue is full!")
            return
        if self.head == -1:
            self.head = 0
        self.tail = (self.tail + 1) % self.size
        self.queue[self.tail] = data

    def dequeue(self):
        if self.head == -1:
            print("Queue is empty!")
            return
        value = self.queue[self.head]
        if self.head == self.tail:
            self.head = self.tail = -1
        else:
            self.head = (self.head + 1) % self.size
        return value

    def display(self):
        if self.head == -1:
            print("Queue is empty!")
        else:
            idx = self.head
            elements = []
            while True:
                elements.append(self.queue[idx])
                if idx == self.tail:
                    break
                idx = (idx + 1) % self.size
            print("Isi Circular Queue:", elements)

cq = CircularQueue(5)
cq.enqueue(10)
cq.enqueue(20)
cq.enqueue(30)
cq.display()
print("Dequeued:", cq.dequeue())
cq.display()
