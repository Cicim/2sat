# Claudio Cicimurri

index = 0
def tarjan(graph):
    # Data structures
    # - list of SCC to return
    sccs = []
    # - stack for the literals
    stack = []
    # - Dictionaries for each attribute
    #   required by the algorithm
    d_index = { l: None for l in graph.literals() }
    d_lowlink = { l: None for l in graph.literals() }
    d_onstack = { l: False for l in graph.literals() }

    # Current index variable
    global index
    index = 0

    def strong_connect(v):
        global index

        d_index[v] = index
        d_lowlink[v] = index
        index += 1
        stack.append(v)
        d_onstack[v] = True

        for w in graph.successors(v):
            if d_index[w] is None:
                strong_connect(w)
                d_lowlink[v] = min(d_lowlink[v], d_lowlink[w])
            elif d_onstack[w]:
                d_lowlink[v] = min(d_lowlink[v], d_index[w])

        if d_lowlink[v] == d_index[v]:
            sc = []
            
            w = stack.pop()
            d_onstack[w] = False
            sc.append(w)
            while w != v:
                w = stack.pop()
                d_onstack[w] = False
                sc.append(w)
            
            sccs.append(tuple(sc))

    # Update all literals in the graph
    for v in graph.literals():
        if d_index[v] is None:
            strong_connect(v)

    return sccs
