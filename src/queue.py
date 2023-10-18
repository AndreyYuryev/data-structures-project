class Node:
    """Класс для узла очереди"""

    def __init__(self, data, next_node):
        """
        Конструктор класса Node

        :param data: данные, которые будут храниться в узле
        """
        self.data = data
        self.next_node = next_node


class Queue:
    """Класс для очереди"""

    def __init__(self):
        """Конструктор класса Queue"""
        self.head = None
        self.tail = None

    def enqueue(self, data):
        """
        Метод для добавления элемента в очередь

        :param data: данные, которые будут добавлены в очередь
        """
        if self.head is None:
            new_node = Node(data, None)
            self.head = new_node
            self.tail = new_node
        elif self.head == self.tail:
            self.tail = Node(data, None)
            self.head.next_node = self.tail
        else:
            new_node = Node(data, None)
            self.tail.next_node = new_node
            self.tail = new_node

    def dequeue(self):
        """
        Метод для удаления элемента из очереди. Возвращает данные удаленного элемента

        :return: данные удаленного элемента
        """
        data = ''
        if self.head is not None:
            if self.head == self.tail:
                data = self.head.data
                self.head = None
                self.tail = None
            elif self.head.next_node == self.tail:
                data = self.head.data
                self.head = self.tail
            else:
                data = self.head.data
                self.head = self.head.next_node
            return data
        return None

    def __str__(self):
        """Магический метод для строкового представления объекта"""
        node = self.head
        str_queue = ""
        if node is not None:
            str_queue += node.data
            node = node.next_node
            while node is not None:
                str_queue += '\n'
                str_queue += node.data
                node = node.next_node
        return str_queue
