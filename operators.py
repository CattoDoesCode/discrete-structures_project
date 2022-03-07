# pretty straightforward, no need to comment here.

def negate(truth_value):
    if truth_value == "T":
        return "F"
    else:
        return "T"


def AND(p, q):
    if p == "T" and q == "T":
        return "T"
    else:
        return "F"


def OR(p, q):
    if p == "F" and q == "F":
        return "F"
    else:
        return "T"


def XOR(p, q):
    if (p == "T" and q == "T") or (p == "F" and q == "F"):
        return "F"
    else:
        return "T"


def IMPLIES(p, q):
    if p == "T" and q == "F":
        return "F"
    else:
        return "T"


def IFF(p, q):
    if (p == "T" and q == "T") or (p == "F" and q == "F"):
        return "T"
    else:
        return "F"


def op_negate(p):
    truth_values = []
    for x in range(len(p)):
        t_v = negate(p[x])
        truth_values.append(t_v)

    return truth_values


def op_and(p, q):
    truth_values = []
    for x in range(len(p)):
        t_v = AND(p[x], q[x])
        truth_values.append(t_v)

    return truth_values


def op_or(p, q):
    truth_values = []
    for x in range(len(p)):
        t_v = OR(p[x], q[x])
        truth_values.append(t_v)

    return truth_values


def op_xor(p, q):
    truth_values = []
    for x in range(len(p)):
        t_v = XOR(p[x], q[x])
        truth_values.append(t_v)

    return truth_values


def op_implies(p, q):
    truth_values = []
    for x in range(len(p)):
        t_v = IMPLIES(p[x], q[x])
        truth_values.append(t_v)

    return truth_values


def op_iff(p, q):
    truth_values = []
    for x in range(len(p)):
        t_v = IFF(p[x], q[x])
        truth_values.append(t_v)

    return truth_values
