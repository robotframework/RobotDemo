from Calculator import Calculator, CalculationError


class CalculatorLibrary(object):

    def __init__(self):
        self._calc = Calculator()
        self._result = ''

    def push_button(self, button):
        self._result = self._calc.push(button)

    def result_should_be(self, expected):
        assert self._result == expected, '%s != %s' % (self._result, expected)

    def input(self, expression):
        for button in expression.replace(' ',''):
            self.push_button(button)

    def should_fail(self, expression):
        try:
            self.input(expression)
        except CalculationError, err:
            return str(err)
        else:
            raise AssertionError('%s should have failed' % expression)
