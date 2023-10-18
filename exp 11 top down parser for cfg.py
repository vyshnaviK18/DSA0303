class Parser:
    def __init__(self, input):
        self.tokens = input.split()
        self.index = 0

    def parse(self):
        return self.parse_expression()

    def parse_expression(self):
        left_operand = self.parse_term()

        while self.index < len(self.tokens):
            operator = self.tokens[self.index]
            if operator in ('+', '-'):
                self.index += 1
                right_operand = self.parse_term()
                if operator == '+':
                    left_operand += right_operand
                else:
                    left_operand -= right_operand
            else:
                break

        return left_operand

    def parse_term(self):
        if self.index < len(self.tokens):
            token = self.tokens[self.index]
            if token.isdigit():
                self.index += 1
                return int(token)
            else:
                raise SyntaxError("Invalid token: " + token)
        else:
            raise SyntaxError("Unexpected end of input")

# Example usage:
input_expression = "5 + 3 - 2"
parser = Parser(input_expression)
result = parser.parse()
print("Result:", result)
