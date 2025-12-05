def proc_seq(n, seq, alive, update, init, debug=False):
    """Process a sequence of items.

    n: seed
    seq: function that produces the next item in the sequence
    alive: function that tests whether to continue processing
    update: function that updates the state
    init: initial state

    >>> def next(n): return n - 1
    >>> def alive(n): return n > 0
    >>> def update(state, n): return state + n
    >>> proc_seq(5, next, alive, update, 0)
    15
    """
    store = init
    while alive(n):
        store = update(store, n)
        n = seq(n)
        if debug:
            print(store,n)
    return store 
