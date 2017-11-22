def is_complete(csp, assignment):
    w, h, horiz_constr, vert_constr = csp
    return len(assignment) == h


def order_domain_values2(csp, var):
    w, h, horiz_constr, vert_constr = csp
    # brute force generation: try each possible combination of w bits
    for bits in range(2 ** w):
        if row_is_consistent(csp, bits, horiz_constr[var]):
            yield bits


def order_domain_values(csp, var):
    w, h, horiz_constr, vert_constr = csp
    # calculate the possible lengths and movements
    # generate the numbers by moving sequences of ones
    for bits in generate_bits(horiz_constr[var][::-1], w):
        yield bits_to_num(bits)


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


def bits_to_num(bits):
    result = 0
    for i in range(len(bits), 0, -1):
        result += bits[len(bits) - i] * 2 ** (len(bits) - i)
    return result


def col_is_consistent(csp, assignment, constr, col):
    w, h, horiz_constr, vert_constr = csp
    row = ''.join([('{:0' + str(w) + 'b}').format(bits)[col] for bits in assignment])
    return bit_str_is_consistent(csp, row, constr)


def is_consistent(csp, assignment, value):
    w, h, horiz_constr, vert_constr = csp
    new_ass = assignment + [value]
    if len(new_ass) == h:
        for col in range(len(vert_constr)):
            if not col_is_consistent(csp, new_ass, vert_constr[col], col):
                return False
    return True


def bit_str_is_consistent(csp, bin_bits_str, constraint):
    lengths_of_1 = []
    prev = False
    current_length = 0
    for bit in bin_bits_str:
        if bit == '1':
            current_length += 1
        else:
            if prev:
                if len(lengths_of_1) < len(constraint) and current_length != constraint[len(lengths_of_1)]:
                    return False
                lengths_of_1.append(current_length)
                current_length = 0
        prev = bit == '1'
    if current_length > 0:
        lengths_of_1.append(current_length)
    return lengths_of_1 == constraint


def row_is_consistent(csp, value, constraint):
    w, h, horiz_constr, vert_constr = csp
    lengths_of_1 = []
    prev = False
    current_length = 0
    mask = 1 << w - 1
    while True:
        bit = mask & value
        mask = mask >> 1
        if bit:
            current_length += 1
        else:
            if prev:
                if len(lengths_of_1) < len(constraint) and current_length != constraint[len(lengths_of_1)]:
                    return False
                lengths_of_1.append(current_length)
                current_length = 0
        if mask == 0:
            break
        prev = bit
    if current_length > 0:
        lengths_of_1.append(current_length)
    return lengths_of_1 == constraint
