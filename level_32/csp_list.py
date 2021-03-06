from memoize import memoized


def is_complete(csp, assignment):
    w, h, horiz_constr, vert_constr = csp
    return len(assignment) == h


@memoized
def order_domain_values(csp, var):
    w, h, horiz_constr, vert_constr = csp
    # calculate the possible lengths and movements
    # generate the numbers by moving sequences of ones
    for bits in generate_bits(horiz_constr[var][::-1], w):
        yield bits


def generate_bits(constraint, length):
    return generate_bits_rec(constraint, length, bits=[], zeros=[], part=0)


def generate_bits_rec(constraint, length, bits, zeros, part):
    if len(bits) == length and part == len(constraint) + 1:
        yield bits
    if part == 0 or part >= len(constraint):
        choice_start = 0
    else:
        choice_start = 1
    for choice in range(choice_start, length - sum(constraint) - sum(zeros) + 1):
        if part < len(constraint):
            new_bits = bits + [0] * choice + [1] * constraint[part]
        else:
            new_bits = bits + [0] * choice
        new_zeros = zeros + [choice]
        new_part = part + 1
        if new_part <= len(constraint) + 1 and len(new_bits) <= length:
            yield from generate_bits_rec(constraint, length, new_bits, new_zeros, new_part)


def is_consistent(csp, assignment, value):
    w, h, horiz_constr, vert_constr = csp
    new_ass = assign_value(assignment, value, len(assignment))
    if len(new_ass) == h:
        for col in range(len(vert_constr)):
            if not col_is_consistent(csp, new_ass, vert_constr[col], col):
                return False
    return True


def col_is_consistent(csp, assignment, constr, col):
    w, h, horiz_constr, vert_constr = csp
    row = [bits[col] for bits in assignment]
    return row_is_consistent(csp, row, constr)


def row_is_consistent(csp, bits, constraint):
    lengths_of_1 = []
    prev = False
    current_length = 0
    for bit in bits:
        if bit:
            current_length += 1
        else:
            if prev:
                if len(lengths_of_1) < len(constraint) and current_length != constraint[len(lengths_of_1)]:
                    return False
                lengths_of_1.append(current_length)
                current_length = 0
        prev = bit
    if current_length > 0:
        lengths_of_1.append(current_length)
    return len(lengths_of_1) == len(constraint) and all([(a == b) for a, b in zip(lengths_of_1, constraint)])


def complete_assignment(csp):
    w, h, horiz_constr, vert_constr = csp
    assignment = null_assignment()
    for var in range(h):
        assignment = assign_value(assignment, next(order_domain_values(csp, var)), var)
    # todo: maybe choosing values consistent with the vertical constraints will speed things up since we start "nearer"
    return assignment


# def assign_value(assignment, value, var):
#     return assignment[:var] + [value] + assignment[var + 1:]
#
#
# def null_assignment():
#     return []


def assign_value(assignment, value, var):
    return assignment[:var] + (value,) + assignment[var + 1:]


def null_assignment():
    return ()
