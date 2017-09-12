from unittest import TestCase

from qdict import *


class DictionaryEqualOperatorTests(TestCase):
    def test_equal__find_obj_simple_value__get_obj_correctly(self):
        # fixtures
        obj = {
            "obj1": {"a": 1, "b": True, "c": {"a": 2}},
            "obj2": {"a": 2, "b": True, "c": {"a": 2}},
            "obj3": {"a": 3, "b": False, "c": {"a": 1}},
            "obj4": {"a": 3, "b": False, "c": {"a": 1}},
        }
        query = {"a": 1}

        # test
        result = find(obj, query)

        # asserts
        result_dict = dict(result)
        self.assertEqual(1, len(result_dict.keys()))
        self.assertIn("obj1", result_dict)

    def test_equal__find_objs_with_query_key_with_another_dict__get_objs_correctly(self):
        # fixtures
        obj = {
            "obj1": {"a": 1, "b": True, "c": {"a": 2}},
            "obj2": {"a": 2, "b": True, "c": {"a": 2}},
            "obj3": {"a": 3, "b": False, "c": {"a": 1}},
            "obj4": {"a": 3, "b": False, "c": {"a": 1}},
        }
        query = {"c": {"a": 1}}

        # test
        result = find(obj, query)

        # asserts
        result_dict = dict(result)
        self.assertEqual(2, len(result_dict.keys()))
        self.assertIn("obj3", result_dict)
        self.assertIn("obj4", result_dict)

    def test_equal__find_objs__query_with_two_keys_simple_and_another_dict__get_objs_correctly(self):
        # fixtures
        obj = {
            "obj1": {"a": 1, "b": True, "c": {"a": 2}},
            "obj2": {"a": 2, "b": False, "c": {"a": 2}},
            "obj3": {"a": 3, "b": True, "c": {"a": 1}},
            "obj4": {"a": 3, "b": False, "c": {"a": 1}},
        }
        query = {"c": {"a": 1}, "b": False}

        # test
        result = find(obj, query)

        # asserts
        result_dict = dict(result)
        self.assertEqual(1, len(result_dict.keys()))
        self.assertIn("obj4", result_dict)

    def test_equal__find_objs__query_with_two_keys_dict__get_objs_correctly(self):
        # fixtures
        obj = {
            "obj1": {"a": 1, "b": True, "c": {"a": 2}, "d": {"a": 1}},
            "obj2": {"a": 2, "b": False, "c": {"a": 2}},
            "obj3": {"a": 1, "b": True, "c": {"a": 1}},
            "obj4": {"a": 3, "b": False, "c": {"a": 1}, "d": {"a": 1}},
        }
        query = {"c": {"a": 1}, "d": {"a": 1}}

        # test
        result = find(obj, query)

        # asserts
        result_dict = dict(result)
        self.assertEqual(1, len(result_dict.keys()))
        self.assertIn("obj4", result_dict)


class DictionaryNotOperatorTests(TestCase):
    def test_not__find_obj_simple_value__get_obj_correctly(self):
        # fixtures
        obj = {
            "obj1": {"a": 1, "b": True, "c": {"a": 2}},
            "obj2": {"a": 2, "b": True, "c": {"a": 2}},
            "obj3": {"a": 3, "b": False, "c": {"a": 1}},
            "obj4": {"a": 3, "b": False, "c": {"a": 1}},
        }
        query = {"a": {"$not": 1}}

        # test
        result = find(obj, query)

        # asserts
        result_dict = dict(result)
        self.assertEqual(3, len(result_dict.keys()))
        self.assertIn("obj2", result_dict)
        self.assertIn("obj3", result_dict)
        self.assertIn("obj4", result_dict)

    def test_not__find_objs_with_query_key_with_another_dict__get_objs_correctly(self):
        # fixtures
        obj = {
            "obj1": {"a": 1, "b": True, "c": {"a": 2}},
            "obj2": {"a": 2, "b": True, "c": {"a": 2}},
            "obj3": {"a": 3, "b": False, "c": {"a": 1}},
            "obj4": {"a": 3, "b": False, "c": {"a": 1}},
        }
        query = {"c": {"a": {"$not": 1}}}

        # test
        result = find(obj, query)

        # asserts
        result_dict = dict(result)
        self.assertEqual(2, len(result_dict.keys()))
        self.assertIn("obj1", result_dict)
        self.assertIn("obj2", result_dict)

    def test_not__find_objs__query_with_two_keys_simple_and_another_dict__get_objs_correctly(self):
        # fixtures
        obj = {
            "obj1": {"a": 1, "b": True, "c": {"a": 2}},
            "obj2": {"a": 2, "b": False, "c": {"a": 2}},
            "obj3": {"a": 3, "b": True, "c": {"a": 1}},
            "obj4": {"a": 3, "b": False, "c": {"a": 1}},
        }
        query = {"c": {"a": {"$not": 1}}, "b": False}

        # test
        result = find(obj, query)

        # asserts
        result_dict = dict(result)
        self.assertEqual(1, len(result_dict.keys()))
        self.assertIn("obj2", result_dict)

    def test_not__find_objs__query_with_two_keys_dict__get_objs_correctly(self):
        # fixtures
        obj = {
            "obj1": {"a": 1, "b": True, "c": {"a": 2}, "d": {"a": 1}},
            "obj2": {"a": 2, "b": False, "c": {"a": 2}},  # "d" key missing
            "obj3": {"a": 1, "b": True, "c": {"a": 1}},  # "d" key missing
            "obj4": {"a": 3, "b": False, "c": {"a": 1}, "d": {"a": 1}},
        }
        query = {"c": {"a": 1}, "d": {"a": {"$not": 1}}}

        # test
        result = find(obj, query)

        # asserts
        result_dict = dict(result)
        self.assertEqual({}, result_dict)


class DictionaryOrOperatorTests(TestCase):
    def test_or__find_obj_simple_value__get_obj_correctly(self):
        # fixtures
        obj = {
            "obj1": {"a": 1, "b": True, "c": {"a": 2}},
            "obj2": {"a": 2, "b": True, "c": {"a": 2}},
            "obj3": {"a": 3, "b": False, "c": {"a": 1}},
            "obj4": {"a": 3, "b": False, "c": {"a": 1}},
        }
        query = {"$or": ({"a": 2}, {"a": 3})}

        # test
        result = find(obj, query)

        # asserts
        result_dict = dict(result)
        self.assertEqual(3, len(result_dict.keys()))
        self.assertIn("obj2", result_dict)
        self.assertIn("obj3", result_dict)
        self.assertIn("obj4", result_dict)

    def test_or__find_objs_with_query_key_with_another_dict__get_objs_correctly(self):
        # fixtures
        obj = {
            "obj1": {"a": 1, "b": True, "c": {"a": 3}},
            "obj2": {"a": 2, "b": True, "c": {"a": 2}},
            "obj3": {"a": 3, "b": False, "c": {"a": 1}},
            "obj4": {"a": 3, "b": False, "c": {"a": 1}},
        }
        query = {"c": {"$or": ({"a": 2}, {"a": 1})}}

        # test
        result = find(obj, query)

        # asserts
        result_dict = dict(result)
        self.assertEqual(3, len(result_dict.keys()))
        self.assertIn("obj2", result_dict)
        self.assertIn("obj3", result_dict)
        self.assertIn("obj4", result_dict)

    def test_or__find_objs__query_with_two_keys_simple_and_another_dict__get_objs_correctly(self):
        # fixtures
        obj = {
            "obj1": {"a": 1, "b": True, "c": {"a": 2}, "d": False},
            "obj2": {"a": 2, "b": False, "c": {"a": 2}, "d": False},
            "obj3": {"a": 3, "b": True, "c": {"a": 1}, "d": True},
            "obj4": {"a": 3, "b": False, "c": {"a": 1}},
            "obj5": {"a": 3, "b": False, "c": {"a": 3}}
        }
        query = {"c": {"$or": ({"a": 1}, {"a": 3})}}

        # test
        result = find(obj, query)

        # asserts
        result_dict = dict(result)
        self.assertEqual(3, len(result_dict.keys()))
        self.assertIn("obj3", result_dict)
        self.assertIn("obj4", result_dict)
        self.assertIn("obj5", result_dict)

    def test_or__find_objs__query_with_two_keys_dict__get_objs_correctly(self):
        # fixtures
        obj = {
            "obj1": {"a": 1, "b": True,  "c": {"a": 2}, "d": {"a": 1}},
            "obj2": {"a": 2, "b": False, "c": {"a": 1}},
            "obj3": {"a": 1, "b": True,  "c": {"a": 1}, "d": {"a": 2}},
            "obj4": {"a": 3, "b": False, "c": {"a": 3}, "d": {"a": 1}},
        }
        query = {
            "c": {"$or": ({"a": 1}, {"a": 3})},
            "d": {"$or": ({"a": 1}, {"a": 3})}
        }

        # test
        result = find(obj, query)

        # asserts
        result_dict = dict(result)
        self.assertEqual(1, len(result_dict.keys()))
        self.assertIn("obj4", result_dict)


class DictionaryGreaterThanTests(TestCase):
    def test_greater__greater_simple__return_obj_correctly(self):
        # fixtures
        obj = {
            "obj1": {"a": 1, "b": True, "c": {"a": 1}, "d": {"a": 1}},
            "obj2": {"a": 3, "b": False, "c": {"a": 6}},
            "obj3": {"a": 3, "b": True, "c": {"a": 8}, "d": {"a": 2}},
            "obj4": {"a": 4, "b": False, "c": {"a": 3}, "d": {"a": 1}},
        }

        query = {
            "a": {"$gt": 3}
        }

        # test
        result = find(obj, query)

        # asserts
        result_dict = dict(result)
        self.assertEqual(1, len(result_dict.keys()))
        self.assertIn("obj4", result_dict)

    def test_greater__greater_than_in_sub_key__return_pair_values(self):
        # fixtures
        obj = {
            "obj1": {"a": 1, "b": True, "c": {"a": 1}, "d": {"a": 1}},
            "obj2": {"a": 3, "b": False, "c": {"a": 6}},
            "obj3": {"a": 3, "b": True, "c": {"a": 8}, "d": {"a": 2}},
            "obj4": {"a": 4, "b": False, "c": {"a": 3}, "d": {"a": 1}},
        }

        query = {
            "c": {"a": {"$gt": 5}}
        }

        # test
        result = find(obj, query)

        # asserts
        result_dict = dict(result)
        self.assertEqual(2, len(result_dict))
        self.assertIn("obj2", result_dict)
        self.assertIn("obj3", result_dict)


class DictionaryGreaterThanEqualTests(TestCase):
    def test_greater_equal__greater_simple__return_obj_correctly(self):
        # fixtures
        obj = {
            "obj1": {"a": 1, "b": True, "c": {"a": 1}, "d": {"a": 1}},
            "obj2": {"a": 3, "b": False, "c": {"a": 6}},
            "obj3": {"a": 3, "b": True, "c": {"a": 8}, "d": {"a": 2}},
            "obj4": {"a": 4, "b": False, "c": {"a": 3}, "d": {"a": 1}},
        }

        query = {
            "a": {"$gte": 3}
        }

        # test
        result = find(obj, query)

        # asserts
        result_dict = dict(result)
        self.assertEqual(3, len(result_dict.keys()))
        self.assertIn("obj2", result_dict)
        self.assertIn("obj3", result_dict)
        self.assertIn("obj4", result_dict)

    def test_greater_equal__greater_than_in_sub_key__return_pair_values(self):
        # fixtures
        obj = {
            "obj1": {"a": 1, "b": True, "c": {"a": 1}, "d": {"a": 1}},
            "obj2": {"a": 3, "b": False, "c": {"a": 5}},
            "obj3": {"a": 3, "b": True, "c": {"a": 8}, "d": {"a": 2}},
            "obj4": {"a": 4, "b": False, "c": {"a": 3}, "d": {"a": 1}},
        }

        query = {
            "c": {"a": {"$gte": 5}}
        }

        # test
        result = find(obj, query)

        # asserts
        result_dict = dict(result)
        self.assertEqual(2, len(result_dict))
        self.assertIn("obj2", result_dict)
        self.assertIn("obj3", result_dict)


class DictionaryCustomOperatorTest(TestCase):
    def test_custom__custom_pair_values__return_pair_values(self):
        # fixtures
        obj = {
            "obj1": {"a": 6, "b": True, "c": {"a": 1}, "d": {"a": 1}},
            "obj2": {"a": 3, "b": False, "c": {"a": 6}},
            "obj3": {"a": 3, "b": True, "c": {"a": 8}, "d": {"a": 2}},
            "obj4": {"a": 4, "b": False, "c": {"a": 3}, "d": {"a": 1}},
        }

        def pair(num):
            return num % 2 == 0

        query = {"$custom": (pair, "a")}

        # test
        result = find(obj, query)

        # asserts
        result_dict = dict(result)
        self.assertEqual(2, len(result_dict.keys()))
        self.assertIn("obj1", result_dict)
        self.assertIn("obj4", result_dict)

    def test_custom__custom_pair_values_subkey__return_pair_values(self):
        # fixtures
        obj = {
            "obj1": {"a": 1, "b": True, "c": {"a": 1}, "d": {"a": 1}},
            "obj2": {"a": 3, "b": False, "c": {"a": 6}},
            "obj3": {"a": 3, "b": True, "c": {"a": 8}, "d": {"a": 2}},
            "obj4": {"a": 4, "b": False, "c": {"a": 3}, "d": {"a": 1}},
        }

        def pair(num):
            return num % 2 == 0

        query = {
            "c": {"$custom": (pair, "a")}
        }

        # test
        result = find(obj, query)

        # asserts
        result_dict = dict(result)
        self.assertEqual(2, len(result_dict.keys()))
        self.assertIn("obj2", result_dict)
        self.assertIn("obj3", result_dict)

    def test_custom__custom_negative_pair_values__return_pair_values(self):
        # fixtures
        obj = {
            "obj1": {"a": 1, "b": True, "c": {"a": 1}, "d": {"a": 1}},
            "obj2": {"a": 3, "b": False, "c": {"a": 6}},
            "obj3": {"a": 3, "b": True, "c": {"a": 8}, "d": {"a": 2}},
            "obj4": {"a": 4, "b": False, "c": {"a": 3}, "d": {"a": 1}},
        }

        def pair(num):
            return num % 2 == 0

        query = {
            "c": {"$not": {"$custom": (pair, "a")}}
        }

        # test
        result = find(obj, query)

        # asserts
        result_dict = dict(result)
        self.assertEqual(2, len(result_dict.keys()))
        self.assertIn("obj1", result_dict)
        self.assertIn("obj4", result_dict)
