from Calculator import Calculator, CalculationError


class CalculatorLibrary(object):

    def __init__(self):
        self.calc = Calculator()
        self.result = ''

    def push_button(self, button):
        self.result = self.calc.push(button)

    def result_should_be(self, expected):
        self._should_be_equal(self.result, expected)

    def input(self, expression):
        for button in expression.replace(' ', ''):
            self.push_button(button)
        return self.result

    def should_fail(self, expression):
        try:
            self.input(expression)
        except CalculationError, err:
            return str(err)
        else:
            raise AssertionError('%s should have failed' % expression)

    def _should_be_equal(self, first, second):
        if first != second:
            raise AssertionError('%s != %s' % (first, second))
