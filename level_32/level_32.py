# LEVEL 32
# http://www.pythonchallenge.com/pc/rock/arecibo.html
# This is a Constraint Satisfaction Problem
# State = all rows + starts (rows assigned)
# Variables = row[k]
# Each lengths is a variable that has values from the
# Domain = lengths where sum(lengths) - len(lengths) + 1 <= max_len
import os
import re
import time

import backtracking


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
            numbers = tuple(map(int, line.split()))
            if logical_line == 1:
                w, h = numbers[0], numbers[1]
            elif 1 < logical_line <= w + 1:
                horiz_constr.append(numbers)
            elif w + 1 < logical_line <= w + h + 1:
                vert_constr.append(numbers)
            else:
                break
    return w, h, tuple(horiz_constr), tuple(vert_constr)


# csp = load_csp('data/warmup.txt')
#
# print(row_is_consistent(csp, '000000000', []))
# print(row_is_consistent(csp, '111111111', [9]))
# print(row_is_consistent(csp, '100000000', [1]))
# print(row_is_consistent(csp, '010000000', [1]))
# print(row_is_consistent(csp, '001000000', [1]))
# print(row_is_consistent(csp, '000000010', [1]))
# print(row_is_consistent(csp, '000000001', [1]))
# print(row_is_consistent(csp, '001100011', [2, 2]))
# print(row_is_consistent(csp, '011000011', [2, 2]))
# print(row_is_consistent(csp, '110000011', [2, 2]))
# print(row_is_consistent(csp, '110000110', [2, 2]))
# print(row_is_consistent(csp, '110001100', [2, 2]))
# print(row_is_consistent(csp, '011000011', [2, 2]))
# print(row_is_consistent(csp, '001101011', [2, 1, 2]))
# print(row_is_consistent(csp, '011001011', [2, 1, 2]))
# print(row_is_consistent(csp, '110001011', [2, 1, 2]))
# print(row_is_consistent(csp, '110010110', [2, 1, 2]))
# print(row_is_consistent(csp, '110101100', [2, 1, 2]))
# print(row_is_consistent(csp, '011010011', [2, 1, 2]))
# print(row_is_consistent(csp, '101101011', [1, 2, 1, 2]))
# print(row_is_consistent(csp, '101101011', [1, 2, 1, 2]))
# print(row_is_consistent(csp, '101010011', [1, 1, 1, 2]))
# print(row_is_consistent(csp, '101010110', [1, 1, 1, 2]))
# print(row_is_consistent(csp, '101010101', [1, 1, 1, 1, 1]))
# print()
# print(row_is_consistent(csp, '000010000', []))
# print(row_is_consistent(csp, '111011111', [9]))
# print(row_is_consistent(csp, '100001000', [1]))
# print(row_is_consistent(csp, '010000100', [1]))
# print(row_is_consistent(csp, '001001000', [1]))
# print(row_is_consistent(csp, '000100010', [1]))
# print(row_is_consistent(csp, '000010001', [1]))
# print(row_is_consistent(csp, '001101011', [2, 2]))
# print(row_is_consistent(csp, '011001011', [2, 2]))
# print(row_is_consistent(csp, '110000111', [2, 2]))
# print(row_is_consistent(csp, '110000111', [2, 2]))
# print(row_is_consistent(csp, '110001101', [2, 2]))
# print(row_is_consistent(csp, '011000111', [2, 2]))
# print(row_is_consistent(csp, '001101111', [2, 1, 2]))
# print(row_is_consistent(csp, '011011011', [2, 1, 2]))
# print(row_is_consistent(csp, '110011011', [2, 1, 2]))
# print(row_is_consistent(csp, '110011110', [2, 1, 2]))
# print(row_is_consistent(csp, '110101101', [2, 1, 2]))
# print(row_is_consistent(csp, '011110011', [2, 1, 2]))
# print(row_is_consistent(csp, '101111011', [1, 2, 1, 2]))
# print(row_is_consistent(csp, '101111011', [1, 2, 1, 2]))
# print(row_is_consistent(csp, '101011011', [1, 1, 1, 2]))
# print(row_is_consistent(csp, '101110110', [1, 1, 1, 2]))
# print(row_is_consistent(csp, '101110101', [1, 1, 1, 1, 1]))
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

tests_dir = 'data/'
tests_patterns = r'level_32_test_03_[0-9]+.*\.txt', r'level_32_test_04_[0-9]+.*\.txt'
files = [f for f in os.listdir(tests_dir) if any([re.match(pat, f) for pat in tests_patterns])]
print(files)

times = 1
for filename in files:
    for implementation in ('csp_tuple',):  # 'csp_list', 'csp_bitstring', 'csp_number'):
        csp_data = load_csp(tests_dir + filename)
        zero = time.process_time()
        for _ in range(times):
            solution = backtracking.backtracking_search(csp_data, implementation)
        elapsed = time.process_time() - zero
        print('{} backtracking_search({}): {}'.format(filename, implementation, elapsed / times))
        if solution:
            for line in solution:
                # print(('{:0' + str(w) + 'b}').format(line).replace('1', '8').replace('0', ' '))
                # print(line.replace('1', '8').replace('0', ' '))
                print(line)
                pass
        else:
            print('NOT FOUND')
            # zero = time.process_time()
            # for _ in range(times):
            #     solution = iterimprov.iterative_improvement(csp_data, implementation)
            # elapsed = time.process_time() - zero
            # print('{} iterative_improvement({}): {}'.format(filename, implementation, elapsed / times))
            # if solution:
            #     for line in solution:
            #         # print(('{:0' + str(w) + 'b}').format(line).replace('1', '8').replace('0', ' '))
            #         # print(line.replace('1', '8').replace('0', ' '))
            #         print(line)
            #         pass
            # else:
            #     print('NOT FOUND')
pass
# warmup.txt backtracking
#   generate values by brute force
#     using bit strings as assignment
#       23.28125 - 23.171875
#     using numbers
#       15.2
#   generate values moving bits
#     using bit strings as assignment
#       0.546875
#     using numbers
#       0.625
#     using lists
#       0.46875
#     To beat:
#       warmup
#         0.03125
#         0.046875

# not memoizing
#     constraints are tuples
#
#     constraints are lists
#
# memoizing domain values
#
# in csp_tuple
#     not memoizing
#         assignment is lists: 0.34453125
#         assignment is tuples: 0.3359375
#     memoizing only domain_values
#         assignment is lists: 0.08671875
#         assignment is tuples: 0.07734375
#     memoize only row_is_consistent
#         assignment is lists: 0.34765625
#         assignment is tuples: 0.3390625
#     memoize only col_is_consistent
#         assignment is tuples: 0.3375
#     memoize only is_consistent
#         assignment is tuples: 0.35625
#     memoize everything
#         assignment is tuples: 0.08828125






# filename = '../data/up.txt'
# csp_data = load_csp(filename)
# zero = time.process_time()
# implementation = 'csp_list'
# solution = iterimprov.iterative_improvement(csp_data, implementation)
# print('{} iterative_improvement({}): {}'.format(filename, implementation, time.process_time() - zero))
# for line in solution:
#     # print(('{:0' + str(w) + 'b}').format(line).replace('1', '8').replace('0', ' '))
#     # print(line.replace('1', '8').replace('0', ' '))
#     print(line)
#     # pass
# solution = backtracking.backtracking_search(csp_data, implementation)
# print('{} backtracking_search({}): {}'.format(filename, implementation, time.process_time() - zero))
# for line in solution:
#     # print(('{:0' + str(w) + 'b}').format(line).replace('1', '8').replace('0', ' '))
#     # print(line.replace('1', '8').replace('0', ' '))
#     print(line)
#     # pass
# # up.txt
# #     To beat:
# #       0.578125
# #       0.625
