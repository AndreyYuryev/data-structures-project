"""Здесь надо написать тесты с использованием unittest для модуля linked_list."""
import unittest
from src.linked_list import Node, LinkedList


class TestCls(unittest.TestCase):
    ''' Тестовые ситуации '''
    def test_linked_list(self):
        # Создаем пустой односвязный список
        ll = LinkedList()

        # Добавляем данные
        ll.insert_beginning({'id': 1})
        ll.insert_at_end({'id': 2})
        ll.insert_at_end({'id': 3})
        ll.insert_beginning({'id': 0})

        # Проверяем данные
        assert str(ll) == "{'id': 0} -> {'id': 1} -> {'id': 2} -> {'id': 3} -> None"