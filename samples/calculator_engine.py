calculator_states = {
    'init': 0,
    'first_figure': 1,
    'second_figure': 2,
    'result': 3,
}

class Calculator:
    
    def __init__(self):
        self.current_state = calculator_states['init']
        self.first_figure = 0
        self.second_figure = 0
        self.operator = ''


    def processNumber(self, number):
        if self.current_state == calculator_states['init']:
            self.first_figure = number
            self.current_state = calculator_states['first_figure']
            pass
        elif self.current_state == calculator_states['first_figure']:
            self.first_figure = self.first_figure * 10 + number
            pass
        elif self.current_state == calculator_states['second_figure']:
            self.second_figure = self.second_figure * 10 + number
            pass
        elif self.current_state == calculator_states['result']:
            pass


    def processSymbol(self, symbol):
        if self.current_state == calculator_states['init']:
            pass
        elif self.current_state == calculator_states['first_figure']:
            # check if symbol is operator
            if symbol == '+' or symbol == '-' or symbol == '*' or symbol == '/':
                self.operator = symbol
                self.current_state = calculator_states['second_figure']
            pass
        elif self.current_state == calculator_states['second_figure']:
            self.current_state = calculator_states['init']
            pass
        elif self.current_state == calculator_states['result']:
            pass
    
    def resolve(self):
        if self.operator == '+':
            return self.first_figure + self.second_figure
        elif self.operator == '-':
            return self.first_figure - self.second_figure
        elif self.operator == '*':
            return self.first_figure * self.second_figure
        elif self.operator == '/':
            return self.first_figure / self.second_figure
        
def processString(stringExpression):
    calcEngine = Calculator()
    for c in stringExpression:
        if c.isdigit():
            calcEngine.processNumber(int(c))
        else:
            calcEngine.processSymbol(c)
    if calcEngine.current_state == calculator_states['second_figure']:
        return calcEngine.resolve()
    return 'Invalid expression'