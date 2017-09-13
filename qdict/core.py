from qdict.exceptions import InvalidOperator, CustomValueError


def resolve(func, query_value, value, operator_str: str):
    try:
        if func == "%snot" % operator_str:
            return not matcher_level(value, query_value, operator_str)
        elif func == "%sor" % operator_str:
            return any(map(lambda q: matcher_level(value, q, operator_str), query_value))
        elif func == "%sand" % operator_str:
            return all(map(lambda q: matcher_level(value, q, operator_str), query_value))
        elif func == "%scustom" % operator_str:
            try:
                return query_value[0](*list(map(lambda k: value.get(k), query_value[1:])))
            except IndexError:
                raise CustomValueError()
        else:
            return FUNCS[func[1:]](query_value, value)
    except KeyError as e:
        raise InvalidOperator(e)


def matcher_level(value, query, operator_str: str):
    matched = True
    if isinstance(query, dict):
        for qk, qv in query.items():
            if qk[0] == operator_str:
                matched = resolve(qk, qv, value, operator_str)
                if not matched:
                    break
            else:
                if qk in value:
                    matched = matcher_level(value[qk], qv, operator_str)
                else:
                    matched = False
                if not matched:
                    break
    else:
        return FUNCS['equal'](value, query)

    return matched


def find(obj, query, operator_str: str = "$"):
    if isinstance(obj, list):
        for v in obj:
            if matcher_level(v, query, operator_str):
                yield v
    else:
        for k, v in obj.items() if isinstance(obj, dict) else obj:
            if matcher_level(v, query, operator_str):
                yield (k, v)


def contains(item, array):
    return item in array


def equal(a, b):
    return a == b


def has_key(key, value):
    return key in value


def in_(array, value):
    return value in array


def greater(a, b):
    return b > a


def greater_equal(a, b):
    return b >= a


def less(a, b):
    return b < a


def less_equal(a, b):
    return b <= a


FUNCS = {
    "contains": contains,
    "equal": equal,
    "has": has_key,
    "in": in_,
    "gt": greater,
    "gte": greater_equal,
    "lt": less,
    "lte": less_equal
}
