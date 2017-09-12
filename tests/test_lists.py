from unittest import TestCase

from qdict import *


class ListEqualOperatorTests(TestCase):
    def test_equal__find_obj_simple_value__get_obj_correctly(self):
        # fixtures
        obj = [
            {"a": 1, "b": True, "c": {"a": 2}},
            {"a": 2, "b": True, "c": {"a": 2}},
            {"a": 3, "b": False, "c": {"a": 1}},
            {"a": 3, "b": False, "c": {"a": 1}},
        ]
        query = {"a": 1}

        # test
        result = find(obj, query)

        # asserts
        result_list = list(result)
        self.assertEqual(1, len(result_list))
        self.assertIn({"a": 1, "b": True, "c": {"a": 2}}, result_list)

    def test_equal__find_objs_with_query_key_with_another_dict__get_objs_correctly(self):
        # fixtures
        obj = [
            {"a": 1, "b": True, "c": {"a": 2}},
            {"a": 2, "b": True, "c": {"a": 2}},
            {"a": 3, "b": False, "c": {"a": 1}},
            {"a": 3, "b": False, "c": {"a": 1}},
        ]
        query = {"c": {"a": 1}}

        # test
        result = find(obj, query)

        # asserts
        result_list = list(result)
        self.assertEqual(2, len(result_list))
        self.assertIn({"a": 3, "b": False, "c": {"a": 1}}, result_list)
        self.assertIn({"a": 3, "b": False, "c": {"a": 1}}, result_list)

    def test_equal__find_objs__query_with_two_keys_simple_and_another_dict__get_objs_correctly(self):
        # fixtures
        obj = [
            {"a": 1, "b": True, "c": {"a": 2}},
            {"a": 2, "b": False, "c": {"a": 2}},
            {"a": 3, "b": True, "c": {"a": 1}},
            {"a": 3, "b": False, "c": {"a": 1}},
        ]
        query = {"c": {"a": 1}, "b": False}

        # test
        result = find(obj, query)

        # asserts
        result_list = list(result)
        self.assertEqual(1, len(result_list))
        self.assertIn({"a": 3, "b": False, "c": {"a": 1}}, result_list)

    def test_equal__find_objs__query_with_two_keys_dict__get_objs_correctly(self):
        # fixtures
        obj = [
            {"a": 1, "b": True, "c": {"a": 2}, "d": {"a": 1}},
            {"a": 2, "b": False, "c": {"a": 2}},
            {"a": 1, "b": True, "c": {"a": 1}},
            {"a": 3, "b": False, "c": {"a": 1}, "d": {"a": 1}},
        ]
        query = {"c": {"a": 1}, "d": {"a": 1}}

        # test
        result = find(obj, query)

        # asserts
        result_list = list(result)
        self.assertEqual(1, len(result_list))
        self.assertIn({"a": 3, "b": False, "c": {"a": 1}, "d": {"a": 1}}, result_list)


class ListNotOperatorTests(TestCase):
    def test_not__find_obj_simple_value__get_obj_correctly(self):
        # fixtures
        obj = [
            {"a": 1, "b": True, "c": {"a": 2}},
            {"a": 2, "b": True, "c": {"a": 2}},
            {"a": 3, "b": False, "c": {"a": 1}},
            {"a": 3, "b": False, "c": {"a": 1}},
        ]
        query = {"a": {"$not": 1}}

        # test
        result = find(obj, query)

        # asserts
        result_list = list(result)
        self.assertEqual(3, len(result_list))
        self.assertIn({"a": 2, "b": True, "c": {"a": 2}}, result_list)
        self.assertIn({"a": 3, "b": False, "c": {"a": 1}}, result_list)
        self.assertIn({"a": 3, "b": False, "c": {"a": 1}}, result_list)

    def test_not__find_objs_with_query_key_with_another_dict__get_objs_correctly(self):
        # fixtures
        obj = [
            {"a": 1, "b": True, "c": {"a": 2}},
            {"a": 2, "b": True, "c": {"a": 2}},
            {"a": 3, "b": False, "c": {"a": 1}},
            {"a": 3, "b": False, "c": {"a": 1}},
        ]
        query = {"c": {"a": {"$not": 1}}}

        # test
        result = find(obj, query)

        # asserts
        result_list = list(result)
        self.assertEqual(2, len(result_list))
        self.assertIn({"a": 1, "b": True, "c": {"a": 2}}, result_list)
        self.assertIn({"a": 2, "b": True, "c": {"a": 2}}, result_list)

    def test_not__find_objs__query_with_two_keys_simple_and_another_dict__get_objs_correctly(self):
        # fixtures
        obj = [
            {"a": 1, "b": True, "c": {"a": 2}},
            {"a": 2, "b": False, "c": {"a": 2}},
            {"a": 3, "b": True, "c": {"a": 1}},
            {"a": 3, "b": False, "c": {"a": 1}},
        ]
        query = {"c": {"a": {"$not": 1}}, "b": False}

        # test
        result = find(obj, query)

        # asserts
        result_list = list(result)
        self.assertEqual(1, len(result_list))
        self.assertIn({"a": 2, "b": False, "c": {"a": 2}}, result_list)

    def test_not__find_objs__query_with_two_keys_dict__get_objs_correctly(self):
        # fixtures
        obj = [
            {"a": 1, "b": True, "c": {"a": 2}, "d": {"a": 1}},
            {"a": 2, "b": False, "c": {"a": 2}},  # "d" key missing
            {"a": 1, "b": True, "c": {"a": 1}},  # "d" key missing
            {"a": 3, "b": False, "c": {"a": 1}, "d": {"a": 1}},
        ]
        query = {"c": {"a": 1}, "d": {"a": {"$not": 1}}}

        # test
        result = find(obj, query)

        # asserts
        result_list = list(result)
        self.assertEqual([], result_list)


class ListOrOperatorTests(TestCase):
    def test_or__find_obj_simple_value__get_obj_correctly(self):
        # fixtures
        obj = [
            {"a": 1, "b": True, "c": {"a": 2}},
            {"a": 2, "b": True, "c": {"a": 2}},
            {"a": 3, "b": False, "c": {"a": 1}},
            {"a": 3, "b": False, "c": {"a": 1}},
        ]
        query = {"$or": ({"a": 2}, {"a": 3})}

        # test
        result = find(obj, query)

        # asserts
        result_list = list(result)
        self.assertEqual(3, len(result_list))
        self.assertIn({"a": 2, "b": True, "c": {"a": 2}}, result_list)
        self.assertIn({"a": 3, "b": False, "c": {"a": 1}}, result_list)
        self.assertIn({"a": 3, "b": False, "c": {"a": 1}}, result_list)

    def test_or__find_objs_with_query_key_with_another_dict__get_objs_correctly(self):
        # fixtures
        obj = [
            {"a": 1, "b": True, "c": {"a": 3}},
            {"a": 2, "b": True, "c": {"a": 2}},
            {"a": 3, "b": False, "c": {"a": 1}},
            {"a": 3, "b": False, "c": {"a": 1}},
        ]
        query = {"c": {"$or": ({"a": 2}, {"a": 1})}}

        # test
        result = find(obj, query)

        # asserts
        result_list = list(result)
        self.assertEqual(3, len(result_list))
        self.assertIn({"a": 2, "b": True, "c": {"a": 2}}, result_list)
        self.assertIn({"a": 3, "b": False, "c": {"a": 1}}, result_list)
        self.assertIn({"a": 3, "b": False, "c": {"a": 1}}, result_list)

    def test_or__find_objs__query_with_two_keys_simple_and_another_dict__get_objs_correctly(self):
        # fixtures
        obj = [
            {"a": 1, "b": True, "c": {"a": 2}, "d": False},
            {"a": 2, "b": False, "c": {"a": 2}, "d": False},
            {"a": 3, "b": True, "c": {"a": 1}, "d": True},
            {"a": 3, "b": False, "c": {"a": 1}},
            {"a": 3, "b": False, "c": {"a": 3}}
        ]
        query = {"c": {"$or": ({"a": 1}, {"a": 3})}}

        # test
        result = find(obj, query)

        # asserts
        result_list = list(result)
        self.assertEqual(3, len(result_list))
        self.assertIn({"a": 3, "b": True, "c": {"a": 1}, "d": True}, result_list)
        self.assertIn({"a": 3, "b": False, "c": {"a": 1}}, result_list)
        self.assertIn({"a": 3, "b": False, "c": {"a": 3}}, result_list)

    def test_or__find_objs__query_with_two_keys_dict__get_objs_correctly(self):
        # fixtures
        obj = [
            {"a": 1, "b": True, "c": {"a": 2}, "d": {"a": 1}},
            {"a": 2, "b": False, "c": {"a": 1}},
            {"a": 1, "b": True, "c": {"a": 1}, "d": {"a": 2}},
            {"a": 3, "b": False, "c": {"a": 3}, "d": {"a": 1}},
        ]
        query = {
            "c": {"$or": ({"a": 1}, {"a": 3})},
            "d": {"$or": ({"a": 1}, {"a": 3})}
        }

        # test
        result = find(obj, query)

        # asserts
        result_list = list(result)
        self.assertEqual(1, len(result_list))
        self.assertIn({"a": 3, "b": False, "c": {"a": 3}, "d": {"a": 1}}, result_list)


class ListGreaterThanTests(TestCase):
    def test_greater__greater_simple__return_obj_correctely(self):
        # fixtures
        obj = [
            {"a": 1, "b": True, "c": {"a": 1}, "d": {"a": 1}},
            {"a": 3, "b": False, "c": {"a": 6}},
            {"a": 3, "b": True, "c": {"a": 8}, "d": {"a": 2}},
            {"a": 4, "b": False, "c": {"a": 3}, "d": {"a": 1}},
        ]

        query = {
            "a": {"$gt": 3}
        }

        # test
        result = find(obj, query)

        # asserts
        result_list = list(result)
        self.assertEqual(1, len(result_list))
        self.assertIn({"a": 4, "b": False, "c": {"a": 3}, "d": {"a": 1}}, result_list)

    def test_greater__greater_than_in_sub_key__return_pair_values(self):
        # fixtures
        obj = [
            {"a": 1, "b": True, "c": {"a": 1}, "d": {"a": 1}},
            {"a": 3, "b": False, "c": {"a": 6}},
            {"a": 3, "b": True, "c": {"a": 8}, "d": {"a": 2}},
            {"a": 4, "b": False, "c": {"a": 3}, "d": {"a": 1}},
        ]

        query = {
            "c": {"a": {"$gt": 5}}
        }

        # test
        result = find(obj, query)

        # asserts
        result_list = list(result)
        self.assertEqual(2, len(result_list))
        self.assertIn({"a": 3, "b": False, "c": {"a": 6}}, result_list)
        self.assertIn({"a": 3, "b": True, "c": {"a": 8}, "d": {"a": 2}}, result_list)


class ListCustomOperatorTest(TestCase):
    def test_custom__custom_pair_values_subkey__return_pair_values(self):
        # fixtures
        obj = [
            {"a": 1, "b": True, "c": {"a": 1}, "d": {"a": 1}},
            {"a": 3, "b": False, "c": {"a": 6}},
            {"a": 3, "b": True, "c": {"a": 8}, "d": {"a": 2}},
            {"a": 4, "b": False, "c": {"a": 3}, "d": {"a": 1}},
        ]

        def pair(num):
            return num % 2 == 0

        query = {
            "c": {"$custom": (pair, "a")}
        }

        # test
        result = find(obj, query)

        # asserts
        result_list = list(result)
        self.assertEqual(2, len(result_list))
        self.assertIn({"a": 3, "b": False, "c": {"a": 6}}, result_list)
        self.assertIn({"a": 3, "b": True, "c": {"a": 8}, "d": {"a": 2}}, result_list)

    def test_custom__custom_pair_values__return_pair_values(self):
        # fixtures
        obj = [
            {"a": 1, "b": True, "c": {"a": 1}, "d": {"a": 1}},
            {"a": 6, "b": False, "c": {"a": 6}},
            {"a": 3, "b": True, "c": {"a": 8}, "d": {"a": 2}},
            {"a": 4, "b": False, "c": {"a": 3}, "d": {"a": 1}},
        ]

        def pair(num):
            return num % 2 == 0

        query = {"$custom": (pair, "a")}

        # test
        result = find(obj, query)

        # asserts
        result_list = list(result)
        self.assertEqual(2, len(result_list))
        self.assertIn({"a": 6, "b": False, "c": {"a": 6}}, result_list)
        self.assertIn({"a": 4, "b": False, "c": {"a": 3}, "d": {"a": 1}}, result_list)

    def test_custom__custom_negative_pair_values__return_pair_values(self):
        # fixtures
        obj = [
            {"a": 1, "b": True, "c": {"a": 1}, "d": {"a": 1}},
            {"a": 3, "b": False, "c": {"a": 6}},
            {"a": 3, "b": True, "c": {"a": 8}, "d": {"a": 2}},
            {"a": 4, "b": False, "c": {"a": 3}, "d": {"a": 1}},
        ]

        def pair(num):
            return num % 2 == 0

        query = {
            "c": {"$not": {"$custom": (pair, "a")}}
        }

        # test
        result = find(obj, query)

        # asserts
        result_list = list(result)
        self.assertEqual(2, len(result_list))
        self.assertIn({"a": 1, "b": True, "c": {"a": 1}, "d": {"a": 1}}, result_list)
        self.assertIn({"a": 4, "b": False, "c": {"a": 3}, "d": {"a": 1}}, result_list)
