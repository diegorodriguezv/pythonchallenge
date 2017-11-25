import importlib
import random

csp_module = importlib.import_module('csp_bitstring')


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
    for value in csp_module.order_domain_values(csp, var):
        new_assignment = csp_module.assign_value(assignment, value, var)
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
        result += 0 if csp_module.col_is_consistent(csp, assignment, vert_constr[col], col) else 1
    # for row in range(h):
    #     result += 0 if csp_module.row_is_consistent(csp, assignment, horiz_constr[row]) else 1
    return result


def iterative_improvement(csp, csp_impl):
    global csp_module
    w, h, horiz_constr, vert_constr = csp
    csp_module = importlib.import_module(csp_impl)
    assignment = csp_module.complete_assignment(csp)
    assert csp_module.is_complete(csp, assignment)
    min_violations = w + 1
    tries = 0
    while True:
        var = select_conflicted_variable(csp, assignment)
        value, viol = choose_best_value(csp, assignment, var)
        new_assignment = csp_module.assign_value(assignment, value, var)
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
