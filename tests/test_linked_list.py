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

    def test_to_list(self):
        # Создаем и наполняем односвязный список
        ll = LinkedList()

        ll.insert_beginning({'id': 1, 'username': 'lazzy508509'})
        ll.insert_at_end({'id': 2, 'username': 'mik.roz'})
        ll.insert_at_end({'id': 3, 'username': 'mosh_s'})
        ll.insert_beginning({'id': 0, 'username': 'serebro'})

        # метод to_list()
        lst = ll.to_list()
        # for item in lst: print(item)
        assert lst[0] == {'id': 0, 'username': 'serebro'}
        assert lst[1] == {'id': 1, 'username': 'lazzy508509'}
        assert lst[2] == {'id': 2, 'username': 'mik.roz'}
        assert lst[3] == {'id': 3, 'username': 'mosh_s'}

    def test_get_data_by_id(self):
        # Создаем и наполняем односвязный список
        ll = LinkedList()

        ll.insert_beginning({'id': 1, 'username': 'lazzy508509'})
        ll.insert_at_end({'id': 2, 'username': 'mik.roz'})
        ll.insert_at_end({'id': 3, 'username': 'mosh_s'})
        ll.insert_beginning({'id': 0, 'username': 'serebro'})

        # метод get_data_by_id()
        user_data = ll.get_data_by_id(3)
        assert user_data == {'id': 3, 'username': 'mosh_s'}

    def test_exception(self):
        # работа блока try/except
        ll = LinkedList()
        ll.insert_beginning({'id': 1, 'username': 'lazzy508509'})
        ll.insert_at_end('idusername')
        ll.insert_at_end([1, 2, 3])
        ll.insert_at_end({'id': 2, 'username': 'mosh_s'})

        user_data = ll.get_data_by_id(2)
        # Данные не являются словарем или в словаре нет id.
        # Данные не являются словарем или в словаре нет id.
        print(user_data)
        # {'id': 2, 'username': 'mosh_s'}