import importlib

# import csp_bitstring as csp_module

csp_module = importlib.import_module('csp_bitstring')


def recursive_backtracking(csp, assignment):
    if csp_module.is_complete(csp, assignment):
        return assignment
    var = select_unassigned_variable(csp, assignment)
    for value in csp_module.order_domain_values(csp, var):
        if csp_module.is_consistent(csp, assignment, value):
            new_assignment = csp_module.assign_value(assignment, value, var)
            result = recursive_backtracking(csp, new_assignment)
            if result is not None:
                return result
    return None


def backtracking_search(csp, csp_impl):
    global csp_module
    csp_module = importlib.import_module(csp_impl)
    return recursive_backtracking(csp, csp_module.null_assignment())


def select_unassigned_variable(csp, assignment):
    return len(assignment)


def solution_is_consistent(csp, solution):
    w, h, horiz_constr, vert_constr = csp
    if len(solution) != h or len(solution[0]) != w:
        return False
    for col in range(len(vert_constr)):
        if not csp_module.col_is_consistent(csp, solution, vert_constr[col], col):
            return False
    for row in range(len(horiz_constr)):
        if not csp_module.row_is_consistent(csp, solution[row], horiz_constr[row]):
            return False
    return True
