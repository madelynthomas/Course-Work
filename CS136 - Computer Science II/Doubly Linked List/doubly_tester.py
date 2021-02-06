#!/usr/bin/env python


import unittest
import doubly_linked_list


class SetUpCase(unittest.TestCase):

    def setUp(self):
        self.ll_one = doubly_linked_list.LinkedList()
        self.ll_two = doubly_linked_list.LinkedList()

    def add_first_test(self):
        self.ll_one.add_first(42)
        self.assertFalse(self.ll_one.is_empty())

    def add_last_list_test(self):
        self.ll_one.add_first(42)
        self.ll_one.add_last(84)
        self.ll_one.add_last(128)
        self.ll_one.__getitem__(0)

    def change_first_list_test(self):
        self.ll_one.add_first(42)
        self.ll_one.add_last(84)
        self.ll_one.__setitem__(42, 84)
        self.assertTrue(self.ll_one.__contains__(84))

    def change_last_list_test(self):
        self.ll_one.add_first(42)
        self.ll_one.add_last(84)
        self.ll_one.__setitem__(1, 84)
        self.assertTrue(self.ll_one.__contains__(84))

    def copy_test(self):
        copy = self.ll_one.copy()
        self.assertTrue(copy.is_empty())

    def contents_node_test(self):
        self.first_node = doubly_linked_list.Node(42)
        string = str(self.first_node)
        self.assertEqual(string, "42")

    def delete_entry_list_test(self):
        self.ll_one.add_first(84)
        self.ll_one.add_first(42)
        del self.ll_one[1]
        self.assertTrue(self.ll_one.__contains__(42))

    def delete_list_test(self):
        self.ll_one.add_last(42)
        self.ll_one.add_last(84)
        self.ll_one.add_last(126)
        self.ll_one.__delitem__(1)
        self.assertEqual(self.ll_one.__str__(), "[42, 126]")

    def empty_list_test(self):
        self.assertTrue(self.ll_one.is_empty())

    def empty_iterator_test(self):
        linda = self.ll_one.__iter__()
        self.assertRaises(StopIteration, linda.next)

    def empty_reverse_iterator_test(self):
        linda = self.ll_one.__reversed__()
        self.assertRaises(StopIteration, linda.next)

    def equality_test(self):
        self.ll_one.add_first(42)
        self.ll_one.add_first(84)
        self.ll_two.add_last(84)
        self.ll_two.add_last(42)
        self.assertTrue(self.ll_one.__eq__(self.ll_two))

    def filled_iterator_test(self):
        self.ll_one.add_first(42)
        linda = self.ll_one.__iter__()
        self.assertRaises(StopIteration)

    def filled_reverse_iterator_test(self):
        self.ll_one.add_first(42)
        linda = self.ll_one.__reversed__()
        self.assertRaises(StopIteration)

    def get_item_test(self):
        self.ll_one.add_last(42)
        self.assertTrue(self.ll_one[0].__str__(), "42")

    def remove_first_list_test(self):
        self.ll_one.add_first(42)
        self.ll_one.remove_first()
        self.assertTrue(self.ll_one.is_empty())

    def remove_last_list_test(self):
        self.ll_one.add_last(42)
        self.ll_one.remove_last()
        self.assertTrue(self.ll_one.is_empty())

    def reverse_string_list_test(self):
        self.ll_one.add_first(42)
        string = str(reversed(self.ll_one))
        self.assertTrue(string, "[24]")

    def string_list_test(self):
        self.ll_one.add_first(42)
        string = str(self.ll_one)
        self.assertEqual(string, "[42]")


def suite():
    suite = unittest.TestSuite()
    suite.addTest(SetUpCase("add_first_test"))
    suite.addTest(SetUpCase("add_last_list_test"))
    suite.addTest(SetUpCase("change_first_list_test"))
    suite.addTest(SetUpCase("change_last_list_test"))
    suite.addTest(SetUpCase("copy_test"))
    suite.addTest(SetUpCase("contents_node_test"))
    suite.addTest(SetUpCase("delete_entry_list_test"))
    suite.addTest(SetUpCase("delete_list_test"))
    suite.addTest(SetUpCase("empty_iterator_test"))
    suite.addTest(SetUpCase("empty_list_test"))
    suite.addTest(SetUpCase("empty_reverse_iterator_test"))
    suite.addTest(SetUpCase("equality_test"))
    suite.addTest(SetUpCase("filled_iterator_test"))
    suite.addTest(SetUpCase("filled_reverse_iterator_test"))
    suite.addTest(SetUpCase("get_item_test"))
    suite.addTest(SetUpCase("remove_first_list_test"))
    suite.addTest(SetUpCase("remove_last_list_test"))
    suite.addTest(SetUpCase("reverse_string_list_test"))
    suite.addTest(SetUpCase("string_list_test"))
    return suite


if __name__ == "__main__":
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite())
