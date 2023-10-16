class Automaton:
    def __init__(self):
        self.state = 'q0'

    def transition(self, input_value):
        if self.state == 'q0':
            if input_value == 'a':
                self.state = 'q1'
            else:
                self.state = 'q0'
        elif self.state == 'q1':
            if input_value == 'b':
                self.state = 'q2'
            else:
                self.state = 'q0'
        else:
            self.state = 'q0'

    def is_accept_state(self):
        return self.state == 'q2'

# Test the automaton
automaton = Automaton()
test_string = "xyzab"

for char in test_string:
    automaton.transition(char)

if automaton.is_accept_state():
    print(f"The string '{test_string}' ends with 'ab'")
else:
    print(f"The string '{test_string}' does not end with 'ab'")
