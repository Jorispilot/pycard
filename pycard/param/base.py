params = dict()


class Param(object):

    def __init__(self, name, value=None):
        self._name = name
        self._value = value
        params[self.format()] = self

    @property
    def name(self):
        return self._name

    def format(self):
        string = self.name
        if self.value is not None:
            string += "=" + self.value
        return string

    @property
    def value(self):
        return self._value


class UnknownParam(Param):

    def __init__(self, name, value=None):
        self._name = name
        self._value = value
        ## Do not append the parameter to the list.
