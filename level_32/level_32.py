# LEVEL 32
# http://www.pythonchallenge.com/pc/rock/arecibo.html
# This is a Constraint Satisfaction Problem
# State = all rows + starts (rows assigned)
# Variables = row[k]
# Each lengths is a variable that has values from the
# Domain = lengths where sum(lengths) - len(lengths) + 1 <= max_len
import random
import time


def load_csp(file_name):
    with open(file_name) as f:
        horiz_constr = []
        vert_constr = []
        logical_line = 0
        while True:
            line = f.readline()
            if line.startswith('#') or line.startswith('\n'):
                continue
            logical_line += 1
            numbers = list(map(int, line.split()))
            if logical_line == 1:
                w, h = numbers[0], numbers[1]
            elif 1 < logical_line <= w + 1:
                horiz_constr.append(numbers)
            elif w + 1 < logical_line <= w + h + 1:
                vert_constr.append(numbers)
            else:
                break
    return w, h, horiz_constr, vert_constr


def is_complete(csp, assignment):
    w, h, horiz_constr, vert_constr = csp
    return len(assignment) == h


def select_unassigned_variable(csp, assignment):
    return len(assignment)


def bit_str_is_consistent(csp, bin_bits_str, constraint):
    lengths_of_1 = []
    prev = False
    current_length = 0
    for bit in bin_bits_str:
        if bit == '1':
            current_length += 1
        else:
            if prev:
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


def order_domain_values2(csp, assignment, var):
    w, h, horiz_constr, vert_constr = csp
    # brute force generation: try each possible combination of w bits
    # todo: calculate the possible lengths and movements
    for bits in range(2 ** w):
        if row_is_consistent(csp, bits, horiz_constr[var]):
            yield bits


def order_domain_values(csp, assignment, var):
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


def recursive_backtracking(csp, assignment):
    if is_complete(csp, assignment):
        return assignment
    var = select_unassigned_variable(csp, assignment)
    for value in order_domain_values(csp, assignment, var):
        if is_consistent(csp, assignment, value):
            assignment.append(value)
            result = recursive_backtracking(csp, assignment)
            if result is not None:
                return result
            del assignment[-1]
    return None


def backtracking_search(csp):
    return recursive_backtracking(csp, [])


# csp = load_csp('data/warmup.txt')
#
# print(bit_str_is_consistent(csp, '000000000', []))
# print(bit_str_is_consistent(csp, '111111111', [9]))
# print(bit_str_is_consistent(csp, '100000000', [1]))
# print(bit_str_is_consistent(csp, '010000000', [1]))
# print(bit_str_is_consistent(csp, '001000000', [1]))
# print(bit_str_is_consistent(csp, '000000010', [1]))
# print(bit_str_is_consistent(csp, '000000001', [1]))
# print(bit_str_is_consistent(csp, '001100011', [2, 2]))
# print(bit_str_is_consistent(csp, '011000011', [2, 2]))
# print(bit_str_is_consistent(csp, '110000011', [2, 2]))
# print(bit_str_is_consistent(csp, '110000110', [2, 2]))
# print(bit_str_is_consistent(csp, '110001100', [2, 2]))
# print(bit_str_is_consistent(csp, '011000011', [2, 2]))
# print(bit_str_is_consistent(csp, '001101011', [2, 1, 2]))
# print(bit_str_is_consistent(csp, '011001011', [2, 1, 2]))
# print(bit_str_is_consistent(csp, '110001011', [2, 1, 2]))
# print(bit_str_is_consistent(csp, '110010110', [2, 1, 2]))
# print(bit_str_is_consistent(csp, '110101100', [2, 1, 2]))
# print(bit_str_is_consistent(csp, '011010011', [2, 1, 2]))
# print(bit_str_is_consistent(csp, '101101011', [1, 2, 1, 2]))
# print(bit_str_is_consistent(csp, '101101011', [1, 2, 1, 2]))
# print(bit_str_is_consistent(csp, '101010011', [1, 1, 1, 2]))
# print(bit_str_is_consistent(csp, '101010110', [1, 1, 1, 2]))
# print(bit_str_is_consistent(csp, '101010101', [1, 1, 1, 1, 1]))
# print()
# print(bit_str_is_consistent(csp, '000010000', []))
# print(bit_str_is_consistent(csp, '111011111', [9]))
# print(bit_str_is_consistent(csp, '100001000', [1]))
# print(bit_str_is_consistent(csp, '010000100', [1]))
# print(bit_str_is_consistent(csp, '001001000', [1]))
# print(bit_str_is_consistent(csp, '000100010', [1]))
# print(bit_str_is_consistent(csp, '000010001', [1]))
# print(bit_str_is_consistent(csp, '001101011', [2, 2]))
# print(bit_str_is_consistent(csp, '011001011', [2, 2]))
# print(bit_str_is_consistent(csp, '110000111', [2, 2]))
# print(bit_str_is_consistent(csp, '110000111', [2, 2]))
# print(bit_str_is_consistent(csp, '110001101', [2, 2]))
# print(bit_str_is_consistent(csp, '011000111', [2, 2]))
# print(bit_str_is_consistent(csp, '001101111', [2, 1, 2]))
# print(bit_str_is_consistent(csp, '011011011', [2, 1, 2]))
# print(bit_str_is_consistent(csp, '110011011', [2, 1, 2]))
# print(bit_str_is_consistent(csp, '110011110', [2, 1, 2]))
# print(bit_str_is_consistent(csp, '110101101', [2, 1, 2]))
# print(bit_str_is_consistent(csp, '011110011', [2, 1, 2]))
# print(bit_str_is_consistent(csp, '101111011', [1, 2, 1, 2]))
# print(bit_str_is_consistent(csp, '101111011', [1, 2, 1, 2]))
# print(bit_str_is_consistent(csp, '101011011', [1, 1, 1, 2]))
# print(bit_str_is_consistent(csp, '101110110', [1, 1, 1, 2]))
# print(bit_str_is_consistent(csp, '101110101', [1, 1, 1, 1, 1]))
# print()
# print()
# print(row_is_consistent(csp, 0b000000000, []))
# print(row_is_consistent(csp, 0b111111111, [9]))
# print(row_is_consistent(csp, 0b100000000, [1]))
# print(row_is_consistent(csp, 0b010000000, [1]))
# print(row_is_consistent(csp, 0b001000000, [1]))
# print(row_is_consistent(csp, 0b000000010, [1]))
# print(row_is_consistent(csp, 0b000000001, [1]))
# print(row_is_consistent(csp, 0b001100011, [2, 2]))
# print(row_is_consistent(csp, 0b011000011, [2, 2]))
# print(row_is_consistent(csp, 0b110000011, [2, 2]))
# print(row_is_consistent(csp, 0b110000110, [2, 2]))
# print(row_is_consistent(csp, 0b110001100, [2, 2]))
# print(row_is_consistent(csp, 0b011000011, [2, 2]))
# print(row_is_consistent(csp, 0b001101011, [2, 1, 2]))
# print(row_is_consistent(csp, 0b011001011, [2, 1, 2]))
# print(row_is_consistent(csp, 0b110001011, [2, 1, 2]))
# print(row_is_consistent(csp, 0b110010110, [2, 1, 2]))
# print(row_is_consistent(csp, 0b110101100, [2, 1, 2]))
# print(row_is_consistent(csp, 0b011010011, [2, 1, 2]))
# print(row_is_consistent(csp, 0b101101011, [1, 2, 1, 2]))
# print(row_is_consistent(csp, 0b101101011, [1, 2, 1, 2]))
# print(row_is_consistent(csp, 0b101010011, [1, 1, 1, 2]))
# print(row_is_consistent(csp, 0b101010110, [1, 1, 1, 2]))
# print(row_is_consistent(csp, 0b101010101, [1, 1, 1, 1, 1]))
# print()
# print(row_is_consistent(csp, 0b000010000, []))
# print(row_is_consistent(csp, 0b110111111, [9]))
# print(row_is_consistent(csp, 0b100001000, [1]))
# print(row_is_consistent(csp, 0b010000100, [1]))
# print(row_is_consistent(csp, 0b001001000, [1]))
# print(row_is_consistent(csp, 0b000100010, [1]))
# print(row_is_consistent(csp, 0b000010001, [1]))
# print(row_is_consistent(csp, 0b001101011, [2, 2]))
# print(row_is_consistent(csp, 0b011001011, [2, 2]))
# print(row_is_consistent(csp, 0b110000111, [2, 2]))
# print(row_is_consistent(csp, 0b110000111, [2, 2]))
# print(row_is_consistent(csp, 0b110001101, [2, 2]))
# print(row_is_consistent(csp, 0b011000111, [2, 2]))
# print(row_is_consistent(csp, 0b001101111, [2, 1, 2]))
# print(row_is_consistent(csp, 0b011011011, [2, 1, 2]))
# print(row_is_consistent(csp, 0b110011011, [2, 1, 2]))
# print(row_is_consistent(csp, 0b110011110, [2, 1, 2]))
# print(row_is_consistent(csp, 0b110101101, [2, 1, 2]))
# print(row_is_consistent(csp, 0b011110011, [2, 1, 2]))
# print(row_is_consistent(csp, 0b101111011, [1, 2, 1, 2]))
# print(row_is_consistent(csp, 0b101111011, [1, 2, 1, 2]))
# print(row_is_consistent(csp, 0b101011011, [1, 1, 1, 2]))
# print(row_is_consistent(csp, 0b101110110, [1, 1, 1, 2]))
# print(row_is_consistent(csp, 0b101110101, [1, 1, 1, 1, 1]))
#
# print()
# print()
# w, h, horiz_constr, vert_constr = csp
# assignment = [
#     0b010110011,
#     0b100111001,
#     0b110111000,
#     0b011111111,
#     0b101111110,
#     0b001111100,
#     0b110111011,
#     0b110111011,
#     0b110011011]
# for i in range(9):
#     print(col_is_consistent(csp, assignment, vert_constr[i], i))
# print()
# assignment = [
#     0b010110011,
#     0b100111001,
#     0b110111000,
#     0b100000000,
#     0b101111110,
#     0b001111100,
#     0b110111011,
#     0b110111011,
#     0b110011011]
# print()
# for i in range(9):
#     print(col_is_consistent(csp, assignment, vert_constr[i], i))
# assignment = [
#     0b010110011,
#     0b100111001,
#     0b110111000,
#     0b011111111,
#     0b101111110,
#     0b001111100,
#     0b110111011,
#     0b110111011]
# print()
# print(is_consistent(csp, assignment, 0b110011011))
# print(is_consistent(csp, assignment, 0b001100100))
# print(is_consistent(csp, assignment, 0b110011111))

#
#
# def generator(step):
#     for i in range(0, 10):
#         yield i * step
#
#
# for g1 in generator(1):
#     print(g1, end=' ')
# print()
#
# for g2 in generator(2):
#     print(g2, end=' ')
# print()
#
# for s in range(5):
#     for gs in generator(s):
#         print(gs, end=' ')
#     print()
#
# print(list(order_domain_values(csp, [], 0)))
# print(len(list(order_domain_values(csp, [], 0))))
# print(list(order_domain_values(csp, [], 1)))
# print(len(list(order_domain_values(csp, [], 1))))
# print(list(order_domain_values(csp, [], 2)))
# print(len(list(order_domain_values(csp, [], 2))))
#
# i = 0
# for c in range(len(vert_constr)):
#     print(c, end=' ')
#     values = order_domain_values(csp, [], c)
#     for d in values:
#         print(d, end=' ')
#         i += 1
#     print()


# w, h, horiz_constr, vert_constr = csp
# print((w, h))
# print(horiz_constr)
# print(len(horiz_constr))
# print(vert_constr)
# print(len(vert_constr))
# for i in range(len(horiz_constr)):
#     assert sum(horiz_constr[i]) - len(horiz_constr[i]) + 1 <= w
# for i in range(len(vert_constr)):
#     assert sum(vert_constr[i]) - len(vert_constr[i]) + 1 <= h
# print('Constraints read OK')


def select_conflicted_variable(csp, assignment):
    """Randomly select any conflicted variable."""
    # All w variables are conflicted until a solution is found, in that case none are
    w, h, horiz_constr, vert_constr = csp
    # todo: maybe choose from the ones with less ¿most? violations
    return random.choice(range(w))


def choose_best_value(csp, assignment, var):
    """Choose a value that violates the fewest constraints."""
    w, h, horiz_constr, vert_constr = csp
    min_violations = w + 1
    min_values = []
    for value in order_domain_values(csp, assignment, var):
        new_assignment = assign_value(assignment, value, var)
        viol = assignment_violations(csp, new_assignment)
        if viol < min_violations:
            min_violations = viol
            min_values = [value]
        else:
            if viol == min_violations:
                min_values.append(value)
    return random.choice(min_values), min_violations


def assignment_violations(csp, assignment):
    w, h, horiz_constr, vert_constr = csp
    result = 0
    for col in range(w):
        result += 0 if col_is_consistent(csp, assignment, vert_constr[col], col) else 1
    return result


def assign_value(assignment, value, var):
    return assignment[:var] + [value] + assignment[var + 1:]


def iterative_improvement(csp):
    w, h, horiz_constr, vert_constr = csp
    assignment = complete_assignment(csp)
    assert is_complete(csp, assignment)
    min_violations = w + 1
    tries = 0
    while True:
        var = select_conflicted_variable(csp, assignment)
        value, viol = choose_best_value(csp, assignment, var)
        new_assignment = assign_value(assignment, value, var)
        if viol <= min_violations:
            min_violations = viol
            assignment = new_assignment
            tries = 0
        else:
            tries += 1
            assert new_assignment != assignment
            if tries > w * h ** 2:
                print('.', end='')
        if viol == 0:
            break
    return assignment


def complete_assignment(csp):
    w, h, horiz_constr, vert_constr = csp
    assignment = []
    for x in range(h):
        assignment.append(next(order_domain_values(csp, assignment, x)))
    # todo: maybe choosing values consistent with the vertical constraints will speed things up since we start "nearer"
    return assignment


csp = load_csp('data/warmup.txt')
w, h, horiz_constr, vert_constr = csp
zero = time.process_time()
solution = backtracking_search(csp)
print('warmup')
print('backtracking_search:{}'.format(time.process_time() - zero))
for line in solution:
    print(('{:0' + str(w) + 'b}').format(line).replace('1', '8').replace('0', ' '))
# using bit strings as assignment
# 23.28125
# 23.171875
# using numbers
# 15.2
# generating moving bits
# 0.625


csp = load_csp('data/warmup.txt')
w, h, horiz_constr, vert_constr = csp
zero = time.process_time()
solution = iterative_improvement(csp)
print('warmup')
print('iterative_improvement:{}'.format(time.process_time() - zero))
for line in solution:
    print(('{:0' + str(w) + 'b}').format(line).replace('1', '8').replace('0', ' '))
# using bit strings as assignment
# 0.125
# 0.1-0.03
# using numbers
# 0.14 - 0.03 ¿?
# generating moving bits
# 0.015625 - 0.03125

#
# csp = load_csp('data/up.txt')
# zero = time.process_time()
# solution = iterative_improvement(csp)
# print('up')
# print('iterative_improvement:{}'.format(time.process_time() - zero))
# for line in solution:
#     print(line.replace('1', '8').replace('0', ' '))
#
