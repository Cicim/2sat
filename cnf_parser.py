# Claudio Cicimurri

class InvalidCnfFileError(Exception):
    def __init__(self, message: int, line: int) -> None:
        self.message = message
        self.line = line
    
    def __str__(self) -> str:
        return f"Error in DIMACS CNF File [line {self.line}]: {self.message}"


def parse_int(string, line_number):
    try:
        return int(string)
    except ValueError:
        raise InvalidCnfFileError("invalid integer", line_number)


def parse_cnf_string(string):
    # Divide the string into lines
    lines = string.split("\n")
    
    formula = []
    current_clause = []

    header = None
    var_count = clause_count = None
    for line_number, line in enumerate(lines, start=1):
        # Strip it
        line = line.strip()
        # Skip it if it's empty or a comment
        if line == '' or line[0] == 'c':
            continue

        words = list(map(lambda e: e.strip(), line.split(" ")))
        # Make sure the first line is the header
        if header is None:
            if words[0] != "p":
                raise InvalidCnfFileError("the first non-comment line should be the header", line_number)
            elif words[1] != "cnf":
                raise InvalidCnfFileError("only the cnf problem is supported", line_number)
            elif len(words) != 4:
                raise InvalidCnfFileError("not enough arguments for the header", line_number)
            else:
                header = var_count, clause_count = parse_int(words[2], line_number), parse_int(words[3], line_number)
        else:
            # Parse all the numbers in this line
            for n in map(lambda n: parse_int(n, line_number), words):
                # Clause end
                if n == 0:
                    if len(formula) + 1 > clause_count:
                        raise InvalidCnfFileError("too many clauses", line_number)

                    # Add the clause to the formula
                    formula.append(tuple(current_clause))
                    current_clause = []
                else:
                    if abs(n) > var_count:
                        raise InvalidCnfFileError("variabile number outside of range", line_number)

                    # Add this variable to the current clause
                    current_clause.append(n)
                    # Check that the number of clauses is correct
                    if len(current_clause) > 2:
                        raise InvalidCnfFileError("this solver accepts only 2-SAT formulas", line_number)

    if len(current_clause) != 0:
        raise InvalidCnfFileError("last clause does not end", line_number-1)

    return formula



def parse_cnf(filename):
    with open(filename, "r") as file:
        contents = file.read()
        return parse_cnf_string(contents)
