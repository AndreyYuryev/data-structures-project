class Node:
    '''
    Класс для узла стека
    '''

    def __init__(self, data, next_node=None):
        """
        Конструктор класса Node

        :param data: данные, которые будут храниться в узле
        """
        self.data = data
        self.next_node = next_node


class Stack:
    """Класс для стека"""

    def __init__(self):
        """Конструктор класса Stack"""
        self.top = None
        self.next_node = None

    def push(self, data):
        """
        Метод для добавления элемента на вершину стека

        :param data: данные, которые будут добавлены на вершину стека
        """
        if self.top is None and self.next_node is None:
            new_node = Node(data, None)
            self.top = new_node
        elif self.top is not None and self.next_node is None:
            new_node = Node(data, self.top)
            self.next_node = self.top
            self.top = new_node
        else:
            new_node = Node(data, self.top)
            self.next_node = self.top
            self.top = new_node

    def pop(self):
        """
        Метод для удаления элемента с вершины стека и его возвращения

        :return: данные удаленного элемента
        """
        if self.top is None:
            return None
        pop_data = self.top
        next_data = self.next_node
        self.top = self.next_node
        if next_data is not None:
            self.next_node = next_data.next_node
        return pop_data.data

    def __str__(self):
        ''' Представление '''
        if self.top is not None and self.next_node is not None:
            return f"'{self.top.data}' -> '{self.next_node.data}'"
        elif self.top is not None and self.next_node is None:
            return f"'{self.top.data}' -> None"
        else:
            return 'None -> None'
