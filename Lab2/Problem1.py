from constraint import *

if __name__ == '__main__':
    problem = Problem(BacktrackingSolver())

    possibleParticipants = int(input())
    participantsName = []
    participantsTezina = []
    for i in range(possibleParticipants):
        line =  input().split(" ")
        tezina = float(line[0])
        ime = line[1]
        participantsName.append(ime)
        participantsTezina.append(tezina)

    possibleLeaders = int(input())
    leadersName = []
    leadersTezina = []

    for i in range(possibleLeaders):
        line = input().split(" ")
        tezina = float(line[0])
        ime = line[1]
        leadersName.append(ime)
        leadersTezina.append(tezina)


    #Tezina of leaders
    # for i in leadersTezina:
    #     print(i)

    # we choose 5 from participants
    problem.addVariables(["Participant 1", "Participant 2", "Participant 3", "Participant 4", "Participant 5"], participantsTezina)

    #we choose 1 from leaders
    problem.addVariable("Leader", leadersTezina)
    variables = ["Participant 1","Participant 2","Participant 3","Participant 4","Participant 5","Leader"]
    #Constraints
    problem.addConstraint(MaxSumConstraint(100.0), variables)
    problem.addConstraint(AllDifferentConstraint(), variables)
    solutions = problem.getSolutions()

    # for singleTuple in solutions:
    #     print(singleTuple)
    bestTuple = 0
    sumFromBestTuple = -1

    for i in range(len(solutions)):
        currentSum = 0
        for j in solutions[i].values():
            currentSum+=j
        if currentSum > sumFromBestTuple:
            sumFromBestTuple = currentSum
            bestTuple = i

    print("Total score:", round(sumFromBestTuple, 1))
    print("Team leader:", leadersName[leadersTezina.index(solutions[bestTuple]["Leader"])])
    print("Participant 1:", participantsName[participantsTezina.index(solutions[bestTuple]["Participant 1"])])
    print("Participant 2:", participantsName[participantsTezina.index(solutions[bestTuple]["Participant 2"])])
    print("Participant 3:", participantsName[participantsTezina.index(solutions[bestTuple]["Participant 3"])])
    print("Participant 4:", participantsName[participantsTezina.index(solutions[bestTuple]["Participant 4"])])
    print("Participant 5:", participantsName[participantsTezina.index(solutions[bestTuple]["Participant 5"])])