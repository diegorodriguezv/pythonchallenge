import importlib
# import csp_bitstring as csp_module

csp_module = importlib.import_module('csp_bitstring')


def recursive_backtracking(csp, assignment):
    if csp_module.is_complete(csp, assignment):
        return assignment
    var = select_unassigned_variable(csp, assignment)
    for value in csp_module.order_domain_values(csp, var):
        if csp_module.is_consistent(csp, assignment, value):
            assignment.append(value)
            result = recursive_backtracking(csp, assignment)
            if result is not None:
                return result
            del assignment[-1]
    return None


def backtracking_search(csp, csp_impl):
    global csp_module
    csp_module = importlib.import_module(csp_impl)
    return recursive_backtracking(csp, [])


def select_unassigned_variable(csp, assignment):
    return len(assignment)
