from cnf_parser import parse_cnf
from implication_graph import ImplicationGraph
from tarjan import tarjan

def two_sat(sccs, duals):
    """
    Returns None if the formula is unsatisfiable,
    else returns a model for the formula in the
    form of a key-value dictionary.
    """
    # Pop the largest component
    model = {}

    while len(sccs) > 0:
        # Get the minimal component
        minimal = sccs.pop()
        # Get its dual component
        dual = duals[minimal]
        # Remove it from the sccs
        try:
            sccs.remove(dual)
        except:
            pass

        # If they match, the formula is unsatisfiable
        if minimal == dual:
            return None

        # Assign false to the literals in the minimal SCC
        for literal in minimal:
            model[literal] = False
        # Assign true to the literals in the dual SCC
        for literal in dual:
            model[literal] = True

    return model



def find_duals(sccs):
    """
    Returns a dictionary returning the dual
    component of each component
    """
    literal_duals = {}
    for scc in sccs:
        for literal in scc:
            literal_duals[-literal] = scc

    duals = {}
    for scc in sccs:
        duals[scc] = literal_duals[scc[0]]

    return duals


def solve_cnf_file(filename):
    formula = parse_cnf(filename)
    graph = ImplicationGraph(formula)
    graph.draw()
    sccs = tarjan(graph)
    print(sccs)
    duals = find_duals(sccs)
    
    graph.draw_sccs()

    model = two_sat(sccs, duals)
    if model is None:
        print("The given formula is unsatisfiable")
    else:
        print("There is a model for the given formula. Here it is:")
        
        show_letters = len(model)
        for literal in sorted(model):
            if literal < 0:
                continue
            
            if show_letters:
                letter = chr(literal + ord('a') - 1)
                print(f"{letter} = {model[literal]}")
            else:
                print(f"x_{literal} = {model[literal]}")


solve_cnf_file(f"cnf_tests/test3.cnf")
