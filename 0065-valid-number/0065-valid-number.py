class Solution:
    def isNumber(self, s: str) -> bool:
        # Define the DFA transitions
        transitions = [
            {'digit': 2, 'sign': 1, 'dot': 3},  # START
            {'digit': 2, 'dot': 3},             # SIGN
            {'digit': 2, 'dot': 4, 'exp': 5},   # DIGIT
            {'digit': 4},                       # DOT
            {'digit': 4, 'exp': 5},             # DOT_DIGIT
            {'sign': 6, 'digit': 7},            # EXP
            {'digit': 7},                       # EXP_SIGN
            {'digit': 7}                        # EXP_DIGIT
        ]

        # Define the accepting states
        accepting_states = {2, 4, 7}

        # Initialize the current state
        state = 0

        for char in s:
            # Determine the type of the current character
            if char.isdigit():
                char_type = 'digit'
            elif char in '+-':
                char_type = 'sign'
            elif char == '.':
                char_type = 'dot'
            elif char in 'eE':
                char_type = 'exp'
            else:
                return False  # Invalid character

            # Transition to the next state
            if char_type in transitions[state]:
                state = transitions[state][char_type]
            else:
                return False  # Invalid transition

        # Check if the final state is an accepting state
        return state in accepting_states