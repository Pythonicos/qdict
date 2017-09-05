class InvalidOperator(Exception):
    def __init__(self, e: KeyError):
        super(InvalidOperator, self).__init__("The operator was not found. {}".format(e))


class CustomValueError(Exception):
    def __init__(self):
        super(CustomValueError, self).__init__("Custom operator needs to be a tuple. The first element is the "
                                               "function and the next are keys of current object that will be the "
                                               "params.")
