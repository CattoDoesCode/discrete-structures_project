# pretty straightforward, no need to comment here.

# TODO: make negate operator available
# def negate(truth_value):
#     if truth_value == "T":
#         return "F"
#     else:
#         return "T"


def AND(p_truth_value, q_truth_value):
    if p_truth_value == "T" and q_truth_value == "T":
        return "T"
    else:
        return "F"


def OR(p_truth_value, q_truth_value):
    if p_truth_value == "F" and q_truth_value == "F":
        return "F"
    else:
        return "T"


def XOR(p_truth_value, q_truth_value):
    if (p_truth_value == "T" and q_truth_value == "T") or (p_truth_value == "F" and q_truth_value == "F"):
        return "F"
    else:
        return "T"


def IMPLIES(p_truth_value, q_truth_value):
    if p_truth_value == "T" and q_truth_value == "F":
        return "F"
    else:
        return "T"


def IFF(p_truth_value, q_truth_value):
    if (p_truth_value == "T" and q_truth_value == "T") or (p_truth_value == "F" and q_truth_value == "F"):
        return "T"
    else:
        return "F"
