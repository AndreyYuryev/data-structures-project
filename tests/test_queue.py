"""Здесь надо написать тесты с использованием unittest для модуля queue."""
import unittest
from src.queue import Node, Queue


class TestCls(unittest.TestCase):
    ''' Тестовые ситуации '''

    def test_node(self):
        ''' проверить Node '''
        node1 = Node(5, None)
        node2 = Node('test', node1)
        self.assertEqual(node1.data, 5)
        self.assertEqual(node2.data, 'test')
        self.assertEqual(node1.next_node, None)
        self.assertEqual(node2.next_node, node1)

    def test_str_queue(self):
        queue = Queue()
        # Магический метод __str__ возвращает пустую строку
        assert str(Queue()) == ""
        # Добавляем данных в очередь
        queue.enqueue('data1')
        queue.enqueue('data2')
        queue.enqueue('data3')
        # Проверяем магический метод __str__
        assert str(queue) == "data1\ndata2\ndata3"

    def test_order_queue(self):
        queue = Queue()
        queue.enqueue('data1')
        queue.enqueue('data2')
        queue.enqueue('data3')

        # Проверяем очередность хранения данных
        assert queue.head.data == 'data1'
        assert queue.head.next_node.data == 'data2'
        assert queue.tail.data == 'data3'
        assert queue.tail.next_node is None
        with self.assertRaises(AttributeError):
            print(queue.tail.next_node.data)
        # AttributeError: 'NoneType' object has no attribute 'data'
