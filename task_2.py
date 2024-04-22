import collections


class CircularBufferList:
    """циклический буфер FIFO реализованный с помощью списка"""
    def __init__(self, capacity):
        self.capacity = capacity
        self.buffer = [None] * capacity
        self.size = 0
        self.front = 0
        self.rear = -1

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == self.capacity

    def enqueue(self, item):
        if self.is_full():
            raise Exception("Buffer is full")
        self.rear = (self.rear + 1) % self.capacity
        self.buffer[self.rear] = item
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            raise Exception("Buffer is empty")
        item = self.buffer[self.front]
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return item

"""Плюсы реализации через список:

Операции доступа по индексу выполняются за O(1).
Не требует импорта дополнительных модулей.

Минусы реализации через список:

При удалении элементов может возникнуть "разрыв" в буфере из-за того, что элементы могут быть удалены из начала буфера.
При добавлении новых элементов в буфер могут возникать переаллокации памяти, что может привести к увеличению времени
выполнения операций."""


class CircularBufferDeque:
    """циклический буфер FIFO реализованный с помощью двусторонней очереди"""
    def __init__(self, capacity):
        self.capacity = capacity
        self.buffer = collections.deque(maxlen=capacity)

    def is_empty(self):
        return len(self.buffer) == 0

    def is_full(self):
        return len(self.buffer) == self.capacity

    def enqueue(self, item):
        if self.is_full():
            raise Exception("Buffer is full")
        self.buffer.append(item)

    def dequeue(self):
        if self.is_empty():
            raise Exception("Buffer is empty")
        return self.buffer.popleft()

"""Плюсы реализации с помощью двусторонней очереди:

Использует специализированную структуру данных, которая сама по себе реализует циклическую природу буфера.
Предоставляет методы append() и popleft(), которые выполняются за константное время, что делает операции добавления
и удаления эффективными.
Не требует реализации логики циклического перемещения индексов.

Минусы реализации с помощью двусторонней очереди:

Требует импорта модуля collections.
Могут возникнуть некоторые проблемы с производительностью при работе с очень большими буферами из-за внутренней реализации двусторонней очереди.
В случае, если необходима дополнительная логика обработки данных, придется реализовывать её самостоятельно."""