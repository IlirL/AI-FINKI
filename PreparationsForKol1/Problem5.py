from constraint import *
def queens_not_attacking(queen1, queen2):
    if queen1[0] == queen2[0] or queen1[1] == queen2[1] or abs(queen1[0] - queen2[0]) == abs(queen1[1] - queen2[1]):
        return False
    # print("Queen1: ", queen1)
    # print("Queen2: ", queen2)
    return True
if __name__ == '__main__':
    problem = Problem(BacktrackingSolver())
    # variables = ["A", "B", "C", "D", "E", "F"]
    # for variable in variables:
    #     problem.addVariable(variable, Domain(set(range(100))))
    n = int(input())
    queens = range(1, n+1)
    domain = [(i,j) for i in range(0, n) for j in range(0, n)]


    # ---Tuka dodadete gi ogranichuvanjata----------------
    problem.addVariables(queens, domain)
    for queen1 in queens:
        for queen2 in queens:
            if queen1<queen2:
                problem.addConstraint(queens_not_attacking, (queen1, queen2))

    # ----------------------------------------------------

    print(problem.getSolution())