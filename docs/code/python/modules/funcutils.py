def proc_seq(n, seq, alive, update, init, debug=False):
    """Process a sequence of items.

    n: seed
    seq: function that produces the next item in the sequence
    alive: function that tests whether to continue processing
    update: function that updates the state
    init: initial state
    """
    store = init
    while alive(n):
        store = update(store, n)
        n = seq(n)
        if debug:
            print(store,n)
    return store

def proc(state, alive, update, debug=False, display=lambda x: print(x) or x):
    """Process as succession of states.

    state: initial state
    alive: one-place function that tests whether state is alive
    update: function that updates the state
    """
    while alive(state):
        state = update(state) if not debug else display(update(state))
    return state 

def make_generator(seq, init):
    """Create a generator from a sequence function.

    seq: function that produces the next item in the sequence
    init: initial state
    """

    def f():
        nonlocal init 
        init = seq((result := init))
        return result 
    return f
