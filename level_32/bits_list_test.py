def generate_bits(constraint, length):
    return generate_bits_rec(constraint, length, bits=[], zeros=[], part=0)


def generate_bits_rec(constraint, length, bits, zeros, part):
    if len(bits) == length and part == len(constraint) + 1:
        yield bits
    if part == 0 or part >= len(constraint):
        choice_start = 0
    else:
        choice_start = 1
    result = []
    for choice in range(choice_start, length - sum(constraint) - sum(zeros) + 1):
        if part < len(constraint):
            new_bits = bits + [0] * choice + [1] * constraint[part]
        else:
            new_bits = bits + [0] * choice
        new_zeros = zeros + [choice]
        new_part = part + 1
        if new_part <= len(constraint) + 1 and len(new_bits) <= length:
            solutions = generate_bits_rec(constraint, length, new_bits, new_zeros, new_part)
            result.extend(solutions)
    yield from result


def bits_to_num(bits):
    result = 0
    for i in range(len(bits), 0, -1):
        result += bits[len(bits)-i] * 2 ** (len(bits)-i)
    return result


print(bits_to_num([0, 0, 0]))
print(bits_to_num([1, 0, 0]))
print(bits_to_num([0, 1, 0]))
print(bits_to_num([1, 1, 0]))
print(bits_to_num([0, 0, 1]))
print(bits_to_num([1, 0, 1]))
print(bits_to_num([0, 1, 1]))
print(bits_to_num([1, 1, 1]))


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


def order_domain_values(csp, assignment, var):
    w, h, horiz_constr, vert_constr = csp
    # brute force generation: try each possible combination of w bits
    # todo: calculate the possible lengths and movements
    for bits in range(2 ** w):
        if row_is_consistent(csp, bits, horiz_constr[var]):
            yield bits


possible_constraints = [
    ((1, 1),),
    ((1,),),
    ((1, 1, 1),),
    ((1,),),
    ((1,), (2,)),
    ((1,), (2,), (3,), (1, 1)),
    ((1,), (2,), (3,), (4,), (1, 1), (1, 2), (2, 1)),
    ((1,), (2,), (3,), (4,), (5,), (1, 1), (1, 2), (1, 3), (3, 1), (2, 1), (2, 2), (1, 1, 1,)),
    ((2, 1, 2), (1, 3, 1), (5,), (7,), (9,), (3,), (2, 3, 2), (2, 3, 2), (2, 3, 2), (2, 1, 3), (1, 2, 3), (3,), (8,),
     (9,), (8,), (3,), (1, 2, 3), (2, 1, 3),),
    ((3, 2,), (8,), (10,), (3, 1, 1,), (5, 2, 1,), (5, 2, 1,), (4, 1, 1,), (15,), (19,), (6, 14,), (6, 1, 12,),
     (6, 1, 10,), (7, 2, 1, 8,), (6, 1, 1, 2, 1, 1, 1, 1,), (5, 1, 4, 1,), (5, 4, 1, 4, 1, 1, 1,), (5, 1, 1, 8,),
     (5, 2, 1, 8,), (6, 1, 2, 1, 3,), (6, 3, 2, 1,), (6, 1, 5,), (1, 6, 3,), (2, 7, 2,), (3, 3, 10, 4,), (9, 12, 1,),
     (22, 1,), (21, 4,), (1, 17, 1,), (2, 8, 5, 1,), (2, 2, 4,), (5, 2, 1, 1,), (5,), (5,), (5,), (5,), (3, 1,),
     (3, 1,), (5,), (5,), (6,), (5, 6,), (9, 5,), (11, 5, 1,), (13, 6, 1,), (14, 6, 1,), (7, 12, 1,), (6, 1, 11, 1,),
     (3, 1, 1, 1, 9, 1,), (3, 4, 10,), (8, 1, 1, 2, 8, 1,), (10, 1, 1, 1, 7, 1,), (10, 4, 1, 1, 7, 1,),
     (3, 2, 5, 2, 1, 2, 6, 2,), (3, 2, 4, 2, 1, 1, 4, 1,), (2, 6, 3, 1, 1, 1, 1, 1,), (12, 3, 1, 2, 1, 1, 1,),
     (3, 2, 7, 3, 1, 2, 1, 2,), (2, 6, 3, 1, 1, 1, 1,), (12, 3, 1, 5,), (6, 3, 1,), (6, 4, 1,), (5, 4,), (4, 1, 1,),
     (5,),)]
lengths = [6, 6, 6, 1, 2, 3, 4, 5, 9, 32]
print(len(possible_constraints), len(lengths))
assert len(possible_constraints) == len(lengths)
print(len(possible_constraints), len(lengths))
for constraints, length in zip(possible_constraints, lengths):
    if length > 9:
        break
    for constraint in constraints:
        print('{:10} {:>3} {:10} {}'.format('length', length, 'constraint', constraint))
        assert sum(constraint) <= length
        s1 = set()
        for bits in generate_bits(constraint, length):
            # print('{:<10} {}'.format(bits_to_num(bits), bits))
            s1.add(bits_to_num(bits))
        s2 = set()
        for val in order_domain_values((length, 1, [list(constraint[::-1])], []), '', 0):
            # print('{}'.format(val))
            s2.add(val)
        if s1 == s2:
            print('OK')
        else:
            print('FAIL: constr:{} length:{} '.format(constraint, length))

