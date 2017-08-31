from qdict import find

if __name__ == '__main__':
    # simple search
    obj = [{"a": 1, "b": False}, {"a": 2, "b": True}, {"b": True}]
    result = find(obj, {"b": True})
    print(list(result))  # [{'a': 2, 'b': True}, {'a': 3, 'b': True}]
    result = find(obj, {"$has": "a"})
    print(list(result))  # [{'a': 1, 'b': False}, {'a': 2, 'b': True}]
    result = find(obj, {"$not": {"$has": "a"}})
    print(list(result))  # [{'b': True}]

    # search with subkeys
    obj = [{"a": 1, "b": {"c": "Positive"}}, {"a": 1, "b": {"c": "Negative"}},
           {"a": 1, "b": {}}]
    result = find(obj, {"b": {"c": "Negative"}})
    print(list(result))  # [{'a': 1, 'b': {'c': 'Negative'}}]

    # $or
    obj = [{"a": 1, "b": {"c": "Positive"}}, {"a": 1, "b": {"c": "Negative"}},
           {"a": 1, "b": {"c": "Undefined"}}, {"a": 1}]
    result = find(obj, {
        "$or": [{"b": {"c": "Positive"}},
                {"$not": {"$has": "b"}}]
    })
    print(list(result))  # [{'a': 1, 'b': {'c': 'Positive'}}, {'a': 1}]

    # $not



