class Calculator(object):

    BUTTONS = '1234567890+-*/C='

    def __init__(self):
        self._expression = ''

    def push(self, button):
        if button not in self.BUTTONS:
            raise CalculationError('Invalid button "%s"' % button)
        if button == '=':
            self._expression = self._calculate()
        elif button == 'C':
            self._expression = ''
        else:
            self._expression += button
        return self._expression

    def _calculate(self):
        try:
            return str(eval(self._expression))
        except SyntaxError:
            raise CalculationError("Invalid expression")
        except ZeroDivisionError:
            raise CalculationError("Division by zero")

class CalculationError(Exception):
    pass
