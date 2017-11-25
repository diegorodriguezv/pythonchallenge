"""This script tests the csp solver by reading a file with valid states, encoding them to constraints, solving the csp
with those constraints and then comparing the solution to the original states."""
import time
import logging
import backtracking


def problem_has_errors(problem):
    logging.debug('checking:', problem)
    WARNING, ERROR = 0, 1
    issues = {}
    for row in range(len(problem)):
        if len(problem[row]) != len(problem):
            issues['warning: problem not square'] = WARNING
        if row > 0 and len(problem[row]) != last_len:
            issues['error: problem with different widths'] = ERROR
        last_len = len(problem[row])
        one_in_col = False
        for col in range(len(problem[row])):
            if problem[row][col] == '1':
                one_in_col = True
        if not one_in_col:
            issues['error: problem has no 1 in row: {}'.format(row)] = ERROR
    for col in range(last_len):
        one_in_row = False
        for row in range(len(problem)):
            if col < len(problem[row]) and problem[row][col] == '1':
                one_in_row = True
        if not one_in_row:
            issues['error: problem has no 1 in column: {}'.format(col)] = ERROR
    for issue, kind in issues.items():
        if kind == WARNING:
            logging.debug(issue)
    has_errors = False
    for issue, kind in issues.items():
        if kind == ERROR:
            logging.debug(issue)
            has_errors = True
    logging.debug('finished')
    return has_errors


def row_to_bits(row):
    return [bit == '1' for bit in row]


def encode_row(bits):
    lengths_of_1 = []
    prev = False
    current_length = 0
    for bit in bits:
        if bit:
            current_length += 1
        else:
            if prev:
                lengths_of_1.append(current_length)
                current_length = 0
        prev = bit
    if current_length > 0:
        lengths_of_1.append(current_length)
    return lengths_of_1


def encode_col(problem, col):
    return encode_row([row[col] == '1' for row in problem])


def csp_from_problem(problem):
    horiz = []
    h = len(problem)
    w = len(problem[0])
    for row in problem:
        horiz.append(tuple(encode_row(row_to_bits(row))))
    vert = []
    for col in range(w):
        vert.append(tuple(encode_col(problem, col)))
    return w, h, tuple(horiz), tuple(vert)


is_new_problem = True
problems = []
with open('data/csp_tester_problems.txt') as f:
    while True:
        line = f.readline()
        if line:
            if line.isspace() or line.startswith('#'):
                if not is_new_problem:
                    problems.append(problem)
                is_new_problem = True
                continue
            if is_new_problem:
                problem = [line.strip()]
                is_new_problem = False
            else:
                problem.append(line.strip())
        else:
            if not is_new_problem:
                problems.append(problem)
            break
logging.debug(problems)
times = 1
for problem in problems:
    if not problem_has_errors(problem):
        csp_data = csp_from_problem(problem)
        print('problem')
        for line in problem:
            print('  ', line)
        print('csp',csp_data)
        for implementation in ('csp_tuple',):  # 'csp_list', 'csp_bitstring', 'csp_number'):
            zero = time.process_time()
            for _ in range(times):
                solution = backtracking.backtracking_search(csp_data, implementation)
            elapsed = time.process_time() - zero
            if solution:
                for line in solution:
                    # print(('{:0' + str(w) + 'b}').format(line).replace('1', '8').replace('0', ' '))
                    # print(line.replace('1', '8').replace('0', ' '))
                    print('  ', line)
                equal = True
                for i in range(len(solution)):
                    equal = equal and len(solution[i]) == len(problem[i]) and all([(a and b == '1' or not a and b == '0') for a, b in zip(solution[i], problem[i])])
                print('same solution:', equal)
                print('consistent solution:', backtracking.solution_is_consistent(csp_data, solution))
            else:
                print('NOT FOUND')
            print('backtracking_search({}): {}'.format(implementation, elapsed / times))
            print()
