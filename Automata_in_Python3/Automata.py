"""Author: Chihabeddine AOURINMOUCHE
   Email: chihab2007@gmail.com

   Open-source it up, guys!!
"""

class State:
    """This class corresponds to each state of the automata."""

    def __init__(self, state_label):
        """Each state has a label and a list of transitions."""
        self.state_label = state_label
        self.transitions = []

    def add_transition(self, transition):
        """Adds a transition to the list of transitions."""
        self.transitions.append(transition)

    def get_transition(self, transition_label):
        for transition in self.transitions:
            if transition.transition_label == transition_label:
                return transition
        return None

    def __str__(self):
        state = "(%s): " % self.state_label
        for transition in self.transitions:
            state += transition + "; "
        return state.strip(" ")

    def __add__(self, other):
        return str(self) + other

    def __radd__(self, other):
        return other + str(self)

    def equals(self, state):
        """Compares two states; if they have the same label then they are the same state.
           While creating states, be careful not to give the same label to two different states.
        """
        ok = (self.state_label == state.state_label)
        if len(self.transitions) == len(state.transitions):
            for i in range(len(self.transitions)):
                ok = ok and (self.transitions[i] == state.transitions[i])
            return ok
        else:
            return False

class Transition:
    """This class corresponds to each transition in the automata."""

    def __init__(self, from_state, transition_label, to_state):
        """Each transition starts from one state, and given its label it leads to another state that could also be its starting state."""
        self.from_state = from_state
        self.transition_label = transition_label
        self.to_state = to_state

    def __str__(self):
        return "(%s --%s--> %s)" % (self.from_state.state_label, self.transition_label, self.to_state.state_label)

    def __add__(self, other):
        return str(self) + other

    def __radd__(self, other):
        return other + str(self)

    def equals(self, transition):
        """Compares two transitions; if they have the same stating state, the same label, and the same ending state then they are the same transition.
           Creating two transitions that are equals leads to a redundant transition.
        """
        return (self.from_state == transition.from_state) and (self.transition_label == transition.transition_label) and (self.to_state == transition.to_state)

class Automata:
    """This class corresponds to the automata."""

    def __init__(self, initial_states, states, terminal_states):
        """Each automata has a set of states, some of them are initial states and others are terminal states."""
        self.initial_states = initial_states
        self.states = states
        self.terminal_states = terminal_states

    def accepts(self, initial_state, string):
        """Given a stating state, we may know if a certain string is accepted or not. The string is accepted if it ends at a terminal state."""
        state = initial_state
        for character in string:
            state = state.get_transition(character).to_state
        for terminal_state in self.terminal_states:
            if terminal_state.equals(state):
                return True
        return False

    def __str__(self):
        terminal_states = ""
        for terminal_state in self.terminal_states:
            terminal_states += terminal_state.state_label + "; "
        initial_states = ""
        for initial_state in self.initial_states:
            initial_states += initial_state.state_label + "; "
        automata = "Initial states: %s\nTerminal states: %s\n" % (initial_states.strip(" "), terminal_states.strip(" "))
        for state in self.states:
            automata += state + "\n"
        return automata

    def __add__(self, other):
        return str(self) + other

    def __radd__(self, other):
        return other + str(self)




if __name__ == '__main__':
    pass

    """States are created here."""
    s0 = State("s0")
    s1 = State("s1")
    s2 = State("s2")

    """Transitions are created here."""
    s0_0_s0 = Transition(s0, '0', s0)
    s0_1_s1 = Transition(s0, '1', s1)
    s1_0_s2 = Transition(s1, '0', s2)
    s1_1_s0 = Transition(s1, '1', s0)
    s2_0_s1 = Transition(s2, '0', s1)
    s2_1_s2 = Transition(s2, '1', s2)

    """Transitions are added to their corresponding states."""
    s0.add_transition(s0_0_s0)
    s0.add_transition(s0_1_s1)
    s1.add_transition(s1_0_s2)
    s1.add_transition(s1_1_s0)
    s2.add_transition(s2_0_s1)
    s2.add_transition(s2_1_s2)

    """An automata is created here."""
    a = Automata([s0, s1], [s0, s1, s2], [s0, s1])

    """Tests & Demonstration"""
    print(a)
    print(a.accepts(s0, '1011101')) #True
    print(a.accepts(s0, '10111011')) #True
    print(a.accepts(s0, '101110110')) #False
