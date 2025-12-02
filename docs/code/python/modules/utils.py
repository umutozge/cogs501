def proc_seq(n, sequencer, alive, update, init):
    """Process a sequence of items.

    sequencer: function that produces the next item in the sequence
    alive: function that tests whether to continue processing
    update: function that updates the state
    init: initial state

    >>> def sequencer(n): return n - 1
    >>> def alive(n): return n > 0
    >>> def update(state, n): return state + n
    >>> proc_seq(5, sequencer, alive, update, 0)
    15
    """
    state = init
    while alive(n):
        state = update(state, n)
        n = sequencer(n)
    return state
