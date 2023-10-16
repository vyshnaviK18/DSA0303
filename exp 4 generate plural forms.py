class PluralFSA:
    def __init__(self):
        self.state = 'q0'

    def transition(self, input_value):
        if self.state == 'q0':
            if input_value in ['s', 'x', 'z', 'ch', 'sh']:
                self.state = 'q1'
            else:
                self.state = 'q2'

    def get_plural(self, noun):
        for char in noun[::-1]:
            self.transition(char)
        if self.state == 'q1':
            return noun + 'es'
        else:
            return noun + 's'

# Test the finite-state machine
fsa = PluralFSA()
nouns = ["cat", "dog", "fish", "child", "box"]
for noun in nouns:
    print(f"Original Noun: {noun} \t Plural Form: {fsa.get_plural(noun)}")
