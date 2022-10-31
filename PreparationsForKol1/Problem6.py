from constraint import *

if __name__ == '__main__':
    problem = Problem(BacktrackingSolver())
    variables = []
    for i in range(1, 10):
        for j in range(1, 10):
            variables.append((i, j))
    domain = range(1,10)
    # print("Domain:", domain)
    problem.addVariables(variables, domain)
    # print("First For:")

    for row in range(1, 10):
        problem.addConstraint(AllDifferentConstraint(), [(row, j) for j in range(1,10)])
        # print([(row, j) for j in range(1,10)])

    # print("Second For:")
    for column in range(1,10):
        problem.addConstraint(AllDifferentConstraint(), [(i, column) for i in range(1,10)])
        # print([(i, column) for i in range(1,10)])

    # print("Third For:")
    # print([(i,j) for i in range(1,4) for j in range(1, 4)])
    for row in range(1, 10, 3):
        problem.addConstraint(AllDifferentConstraint(), [(i, j) for i in range(row, row+3) for j in range(row, row+3)])
        # print([(i, j) for i in range(row, row+3) for j in range(row, row+3)])


# ---Tuka dodadete gi ogranichuvanjata----------------

# ----------------------------------------------------

print(problem.getSolution())