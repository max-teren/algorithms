import stack


class Dijkstra:
    def __init__(self):
        self.values = stack.ArrayStack()
        self.operations = stack.ArrayStack()

    def calculate(self, expression: str):
        for char in expression:
            if char == ')':
                right_value = self.values.pop()
                left_value = self.values.pop()
                operation = self.operations.pop()
                if operation == '+':
                    result = left_value + right_value
                elif operation == '-':
                    result = left_value - right_value
                elif operation == '*':
                    result = left_value * right_value
                elif operation == '/':
                    result = left_value / right_value
                self.values.push(result)
            elif char in ['+', '-', '*', '/']:
                self.operations.push(char)
            elif self.try_parse_int(char):
                self.values.push(int(char))
            else:
                continue
        return self.values.pop()

    def try_parse_int(self, char):
        try:
            int(char)
            return True
        except ValueError:
            return False


if __name__ == '__main__':
    dijkstra = Dijkstra()
    print(dijkstra.calculate('(1+((2+3)*(4*5)))'))
