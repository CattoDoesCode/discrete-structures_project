# logical connectives

def _negate(truth_value):
    if truth_value == "T":
        return "F"
    else:
        return "T"


def _and(p, q):
    if p == "T" and q == "T":
        return "T"
    else:
        return "F"


def _or(p, q):
    if p == "F" and q == "F":
        return "F"
    else:
        return "T"


def _xor(p, q):
    if (p == "T" and q == "T") or (p == "F" and q == "F"):
        return "F"
    else:
        return "T"


def _implies(p, q):
    if p == "T" and q == "F":
        return "F"
    else:
        return "T"


def _iff(p, q):
    if (p == "T" and q == "T") or (p == "F" and q == "F"):
        return "T"
    else:
        return "F"


# operators to generate truth values

def op_negate(p):
    truth_values = []
    for x in range(len(p)):
        t_v = _negate(p[x])
        truth_values.append(t_v)

    return truth_values


def op_and(p, q):
    truth_values = []
    for x in range(len(p)):
        t_v = _and(p[x], q[x])
        truth_values.append(t_v)

    return truth_values


def op_or(p, q):
    truth_values = []
    for x in range(len(p)):
        t_v = _or(p[x], q[x])
        truth_values.append(t_v)

    return truth_values


def op_xor(p, q):
    truth_values = []
    for x in range(len(p)):
        t_v = _xor(p[x], q[x])
        truth_values.append(t_v)

    return truth_values


def op_implies(p, q):
    truth_values = []
    for x in range(len(p)):
        t_v = _implies(p[x], q[x])
        truth_values.append(t_v)

    return truth_values


def op_iff(p, q):
    truth_values = []
    for x in range(len(p)):
        t_v = _iff(p[x], q[x])
        truth_values.append(t_v)

    return truth_values
