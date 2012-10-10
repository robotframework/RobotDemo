import unittest
from Calculator import Calculator, CalculationError

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_push_numbers(self):
        for i in range(10):
            self.calc.push(str(i))

    def _push_and_expect(self, button, expected):
        self.assertEquals(self.calc.push(button), expected)

    def _push_and_raise(self, button, message):
        try:
            self.calc.push(button)
        except CalculationError as e:
            self.assertEquals(str(e), message)
        else:
            self.fail('Exception not raised')

    def test_display_numbers(self):
        self.assertEquals(self.calc._expression, '')
        self._push_and_expect('1', '1')
        self._push_and_expect('2', '12')

    def test_addition(self):
        self._push_and_expect('1', '1')
        self._push_and_expect('+', '1+')
        self._push_and_expect('1', '1+1')
        self._push_and_expect('=', '2')

    def test_continue_calcs(self):
        self._push_and_expect('1', '1')
        self._push_and_expect('+', '1+')
        self._push_and_expect('1', '1+1')
        self._push_and_expect('=', '2')
        self._push_and_expect('+', '2+')
        self._push_and_expect('1', '2+1')
        self._push_and_expect('=', '3')

    def test_clear(self):
        self._push_and_expect('c', '')
        self._push_and_expect('1', '1')
        self._push_and_expect('C', '')
        self._push_and_expect('1', '1')
        self._push_and_expect('+', '1+')
        self._push_and_expect('c', '')

    def test_identity(self):
        self._push_and_expect('=', '')
        self._push_and_expect('1', '1')
        self._push_and_expect('=', '1')

    def test_unfinished(self):
        self._push_and_expect('1', '1')
        self._push_and_expect('+', '1+')
        self._push_and_raise('=', 'Invalid expression')
        self._push_and_expect('1', '1+1')
        self._push_and_expect('=', '2')

    def test_zero_division(self):
        self._push_and_expect('1', '1')
        self._push_and_expect('/', '1/')
        self._push_and_expect('0', '1/0')
        self._push_and_raise('=', 'Division by zero')

    def test_zero_by_zero_division(self):
        self._push_and_expect('0', '0')
        self._push_and_expect('/', '0/')
        self._push_and_expect('0', '0/0')
        self._push_and_raise('=', 'Division by zero')

    def test_unmatched_parens(self):
        self._push_and_expect(')', ')')
        self._push_and_raise('=', 'Invalid expression')

    def test_large_numbers(self):
        self._push_and_expect('1', '1')
        self._push_and_expect('1', '11')
        self._push_and_expect('9', '119')
        self._push_and_expect('+', '119+')
        self._push_and_expect('8', '119+8')
        self._push_and_expect('5', '119+85')
        self._push_and_expect('7', '119+857')
        self._push_and_expect('=', '976')
