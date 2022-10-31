from constraint import *

if __name__ == '__main__':
    problem =Problem(BacktrackingSolver())
    n = int(input())
    participants = []
    for i in range(n):
        line = input()
        seperate = line.split(" ")

        participants.append(((float)(seperate[0]), seperate[1]))

    participants = tuple(participants)

    m = int(input())
    leaders = []
    for i in range(m):
        line = input()
        seperate = line.split(" ")

        leaders.append(((float)(seperate[0]), seperate[1]))

    leaders = tuple(leaders)

    variables = ("Leader", "Participant 1", "Participant 2", "Participant 3", "Participant 4","Participant 5")
    problem.addVariable("Leader", leaders)
    problem.addVariables(("Participant 1", "Participant 2", "Participant 3", "Participant 4", "Participant 5"), participants)

    for i in variables:
        for j in variables:
            if i<j:
                problem.addConstraint(lambda x, y: x!=y, (i, j))
    # problem.addConstraint(MaxSumConstraint(100))
    problem.addConstraint(lambda leader, p1, p2, p3, p4, p5: p1[0] + p2[0] + p3[0]+p4[0]+p5[0]+leader[0] <= 100, variables)
    #p1[0] + p2[0] + p3[0]+p4[0]+p5[0]+leader[0] <= 100
    solutions = problem.getSolutions()


    bestSolutionIndex = 0
    bestSolutionSum = 0
    for i in range(len(solutions)):
        tempSum = 0
        for j in solutions[i].values():
            tempSum = tempSum+j[0]
        if(bestSolutionSum < tempSum):
            bestSolutionSum = tempSum
            bestSolutionIndex = i
    #format the output

    solution = dict()
    solution["Leader"] = solutions[bestSolutionIndex]["Leader"][1]
    solution["Participant 1"] = solutions[bestSolutionIndex]["Participant 1"][1]
    solution["Participant 2"] = solutions[bestSolutionIndex]["Participant 2"][1]
    solution["Participant 3"] = solutions[bestSolutionIndex]["Participant 3"][1]
    solution["Participant 4"] = solutions[bestSolutionIndex]["Participant 4"][1]
    solution["Participant 5"] = solutions[bestSolutionIndex]["Participant 5"][1]



    print(solution)