class Node:
    """Класс для узла односвязного списка"""

    def __init__(self, data, next_node):
        self.data = data
        self.next_node = next_node


class LinkedList:
    """Класс для односвязного списка"""

    def __init__(self):
        ''' конструктор '''
        self.head = None

    def insert_beginning(self, data: dict) -> None:
        """Принимает данные (словарь) и добавляет узел с
        этими данными в начало связанного списка"""
        new_node = Node(data, None)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next_node = self.head
            self.head = new_node

    def insert_at_end(self, data: dict) -> None:
        """Принимает данные (словарь) и добавляет узел с
        этими данными в конец связанного списка"""
        new_node = Node(data, None)
        if self.head is None:
            self.head = new_node
        elif self.head.next_node is None:
            self.head.next_node = new_node
        else:
            node_from = self.head
            next_node = node_from.next_node
            while next_node is not None:
                node_from = next_node
                next_node = node_from.next_node
            node_from.next_node = new_node

    def __str__(self) -> str:
        """Вывод данных односвязного списка в строковом представлении"""
        node = self.head
        if node is None:
            return str(None)

        ll_string = ''
        while node:
            ll_string += f'{str(node.data)} -> '
            node = node.next_node

        ll_string += 'None'
        return ll_string

    def to_list(self):
        ''' вернуть список '''
        ll_list = []
        node = self.head
        if node is None:
            return None

        while node:
            ll_list.append(node.data)
            node = node.next_node
        return ll_list

    def get_data_by_id(self, id):
        ''' вернуть данные по id '''
        ll_list = self.to_list()
        for itm in ll_list:
            try:
                if not isinstance(itm, dict):
                    raise TypeError('Данные не являются словарем или в словаре нет id.')
                if itm['id'] == id:
                    return itm
            except TypeError as exp:
                print(exp)
