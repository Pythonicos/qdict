def resolve(func, query_value, value):
    try:
        if func == "$not":
            return not matcher_level(value, query_value)
        elif func == "$or":
            return any(map(lambda q: matcher_level(value, q), query_value))
        elif func == "$and":
            return all(map(lambda q: matcher_level(value, q), query_value))
        elif func == "$custom":
            key_params = query_value[1:]
            return all(map(lambda k: k in value, key_params)) and query_value[0](
                *list(map(lambda k: value[k] if k in value else None, key_params))
            )
        else:
            return funcs[func](query_value, value)
    except KeyError as e:
        raise e


def matcher_level(value, query):
    matched = True
    if isinstance(query, dict):
        for qk, qv in query.items():
            if qk[0] == "$":
                matched = resolve(qk, qv, value)
                if not matched:
                    break
            else:
                if qk in value:
                    matched = matcher_level(value[qk], qv)
                else:
                    matched = False
                if not matched:
                    break
    else:
        return funcs['$equal'](value, query)

    return matched


def find(obj, query):
    if isinstance(obj, list):
        for v in obj:
            if matcher_level(v, query):
                yield v
    else:
        for k, v in obj.items() if isinstance(obj, dict) else obj:
            if matcher_level(v, query):
                yield (k, v)


def contains(item, array):
    return item in array


def in_(array, value):
    return value in array


def equal(a, b):
    return a == b


def has_key(key, value):
    return key in value


funcs = {
    "$contains": contains,
    "$equal": equal,
    "$has": has_key,
    "$in": in_
}
