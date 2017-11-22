# LEVEL 32
# http://www.pythonchallenge.com/pc/rock/arecibo.html
# This is a Constraint Satisfaction Problem
# State = all rows + starts (rows assigned)
# Variables = row[k]
# Each lengths is a variable that has values from the
# Domain = lengths where sum(lengths) - len(lengths) + 1 <= max_len

import time

import backtracking
import iterimprov


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
    return w, h, (horiz_constr), (vert_constr)


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


times = 1
for filename in ('../data/warmup.txt',):
    for implementation in ('csp_number', 'csp_bitstring', 'csp_list'):
        csp_data = load_csp(filename)
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
        zero = time.process_time()
        for _ in range(times):
            solution = iterimprov.iterative_improvement(csp_data, implementation)
        elapsed = time.process_time() - zero
        print('{} iterative_improvement({}): {}'.format(filename, implementation, elapsed / times))
        if solution:
            for line in solution:
                # print(('{:0' + str(w) + 'b}').format(line).replace('1', '8').replace('0', ' '))
                # print(line.replace('1', '8').replace('0', ' '))
                print(line)
                pass
        else:
            print('NOT FOUND')
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

# warmup.txt  iterative improvement
#   generate values by brute force
#     using bit strings as assignment
#       0.125
#       0.1-0.03
#     using numbers
#       0.14 - 0.03 ¿?
#   generate values moving bits
#     using bit strings as assignment
#       0.015625 - 0.03125
#     using numbers
#       0.015625
#     using lists
#       0.015625
#     To beat:
#       warmup
#         0.03125
#         0.046875

# ../data/warmup.txt backtracking_search(csp_number): 0.616796875
# ../data/warmup.txt iterative_improvement(csp_number): 0.02265625
# ../data/warmup.txt backtracking_search(csp_bitstring): 0.546484375
# ../data/warmup.txt iterative_improvement(csp_bitstring): 0.009765625
# ../data/warmup.txt backtracking_search(csp_list): 0.47109375
# ../data/warmup.txt iterative_improvement(csp_list): 0.0078125
# After improving row_is_consistent to fail fast and remove result.extend
# ../data/warmup.txt backtracking_search(csp_number): 0.570703125
# ../data/warmup.txt iterative_improvement(csp_number): 0.026953125
# ../data/warmup.txt backtracking_search(csp_bitstring): 0.498828125
# ../data/warmup.txt iterative_improvement(csp_bitstring): 0.010546875
# ../data/warmup.txt backtracking_search(csp_list): 0.43046875
# ../data/warmup.txt iterative_improvement(csp_list): 0.00703125

# filename = '../data/up.txt'
# csp_data = load_csp(filename)
# zero = time.process_time()
# implementation = 'csp_list'
# solution = backtracking.backtracking_search(csp_data, implementation)
# print('{} backtracking_search({}): {}'.format(filename, implementation, time.process_time() - zero))
# solution = iterimprov.iterative_improvement(csp_data, implementation)
# print('{} iterative_improvement({}): {}'.format(filename, implementation, time.process_time() - zero))
# for line in solution:
#     # print(('{:0' + str(w) + 'b}').format(line).replace('1', '8').replace('0', ' '))
#     # print(line.replace('1', '8').replace('0', ' '))
#     print(line)
#     # pass

# up.txt
#     To beat:
#       0.578125
#       0.625
