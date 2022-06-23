# Claudio Cicimurri

def tarjan(graph):
    # Data structures
    # - list of SCC to return
    sccs = []
    # - stack for the literals
    stack = []
    # - Dictionaries for each attribute
    #   required by the algorithm
    d_index = { l: None for l in graph.literals }
    d_lowlink = { l: None for l in graph.literals }
    d_onstack = { l: False for l in graph.literals }

    # Current index variable
    index = 0
    # Update all literals in the graph
    for v in graph.literals:
        if d_index[v] is None:
            strong_connect(v)
    
    def strong_connect(v):
        d_index[v] = index
        d_lowlink[v] = index
        index += 1
        stack.push(v)
        d_onstack[v] = True

        for w in graph.neighbors(v):
            if d_index[w] is None:
                strong_connect(w)
                d_lowlink[v] = min(d_lowlink[v], d_lowlink[w])
            elif d_onstack[w]:
                d_lowlink[v] = min(d_lowlink[v], d_index[w])

        if d_lowlink[v] == d_index[v]:
            sc = []
            
            w = stack.pop()
            d_onstack[w] = False
            while w != v:
                sc.append(w)
                w = stack.pop()
                d_onstack[w] = False
            
            sccs.append(sc)

    return sccs
