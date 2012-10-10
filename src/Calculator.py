

class Calculator(object):

    def __init__(self):
        self._expression = ''
        self._callbacks = self._get_callbacks()

    def _get_callbacks(self):
        callbacks = dict((b, self._push_button) for b in '0123456789+-*/()')
        callbacks['c'] = callbacks['C'] = self._clear
        callbacks['='] = self._evaluate
        return callbacks

    def push(self, button):
        try:
            callback = self._callbacks[button]
        except KeyError:
            raise CalculationError('Invalid button')
        self._expression = callback(self._expression, button)
        return self._expression

    def _push_button(self, expression, button):
        return expression + button

    def _clear(self, expression, button):
        return ''

    def _evaluate(self, expression, button):
        if not expression:
            return ''
        try:
            return str(eval(expression))
        except SyntaxError:
            raise CalculationError('Invalid expression')
        except ZeroDivisionError:
            raise CalculationError('Division by zero')


class CalculationError(Exception):
    pass
