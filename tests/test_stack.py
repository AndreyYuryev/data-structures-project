"""Здесь надо написать тесты с использованием unittest для модуля stack."""
import unittest
from src.stack import Node, Stack


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

    def test_stack_push(self):
        ''' Проверить Stack Push  '''
        stack = Stack()
        stack.push('test1')
        stack.push('test2')
        stack.push('test3')
        self.assertEqual(stack.top.data, 'test3')  # data3
        self.assertEqual(stack.top.next_node.data, 'test2')  # data2
        self.assertEqual(stack.top.next_node.next_node.data, 'test1')  # data1
        self.assertEqual(stack.top.next_node.next_node.next_node, None)  # None
        with self.assertRaises(AttributeError):
            self.assertEqual(stack.top.next_node.next_node.next_node.data, 'test1')
            # AttributeError: 'NoneType' object has no attribute 'data'

    def test_stack_pop(self):
        ''' Проверить Stack Pop '''
        stack = Stack()
        stack.push('test1')
        stack.push('test2')
        top_data = stack.pop()
        self.assertEqual(top_data, 'test2')
        next_data = stack.pop()
        self.assertEqual(next_data, 'test1')
        self.assertEqual(stack.next_node, None)

    def test_str(self):
        ''' Проверить вызов str '''
        stack = Stack()
        self.assertEqual(str(stack), 'None -> None')
        stack.push('Test1')
        self.assertEqual(str(stack), "'Test1' -> None")
        stack.push('Test2')
        stack.push('Test4')
        self.assertEqual(str(stack), "'Test4' -> 'Test2'")
