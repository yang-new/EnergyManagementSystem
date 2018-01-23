# The main entrance of the optimal power flow in unviersal energy management system
import threading  # Thread management (timeout and return value)
from scipy import optimize  # linear programming solver
from solvers.mixed_integer_solvers_gurobi import mixed_integer_linear_programming

class SolvingThread(threading.Thread):
    # Thread operation with time control and return value
    def __init__(self, parameter):
        threading.Thread.__init__(self)
        self.parameter = parameter
        self.value = 0

    def run(self):
        self.value = solving_procedure(self.parameter)


def solving_procedure(*args):
    # By using linear programming to solve the optimal power flow problem
    # The input is dictionary
    c = args[0]["c"]
    A = args[0]["A"]
    b = args[0]["b"]
    Aeq = args[0]["Aeq"]
    beq = args[0]["beq"]
    lb = args[0]["lb"]
    ub = args[0]["ub"]
    option = {"disp": False}

    # Convert list into tuple
    # boundary = tuple()
    # for i in range(len(lb)):
    #     boundary += ((lb[i], ub[i]),)
    vtypes = ["c"] * len(lb)
    (solution, obj, success) = mixed_integer_linear_programming(c, Aeq=Aeq, beq=beq, A=A, b=b, xmin=lb, xmax=ub, vtypes=vtypes)
    # res = optimize.linprog(c, A_ub=A, b_ub=b, A_eq=Aeq, b_eq=beq, bounds=boundary, options=option)

    res = {"x": solution,
           "obj": obj,
           "success": success > 0}

    return res
