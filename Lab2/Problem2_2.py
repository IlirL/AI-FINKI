from constraint import *

def func(simona, marija, petar, vreme):
    simonaPossibleHoursForSostanok = (13, 14, 16, 19)
    marijaPossibleHoursForSostanok = (14, 15, 18)
    petarPossibleHoursForSostanok = (12, 13, 16, 17, 18, 19)
    if simona == 1 and marija == 1 and petar == 0 and vreme in simonaPossibleHoursForSostanok and vreme in marijaPossibleHoursForSostanok:
        return True
    if simona == 1 and petar == 1 and marija == 0 and vreme in simonaPossibleHoursForSostanok and vreme in petarPossibleHoursForSostanok :
        return True
    return False

if __name__ == '__main__':
    problem = Problem(BacktrackingSolver())

    possibleHoursForSostanok = (12,13,14,15,16,17,18,19)
    # ---Dadeni se promenlivite, dodadete gi domenite-----
    problem.addVariable("Simona_prisustvo", (0,1))
    problem.addVariable("Marija_prisustvo", (0,1))
    problem.addVariable("Petar_prisustvo", (0,1))
    problem.addVariable("vreme_sostanok", possibleHoursForSostanok)
    # ----------------------------------------------------

    # ---Tuka dodadete gi ogranichuvanjata----------------
    problem.addConstraint(func, ("Simona_prisustvo","Marija_prisustvo","Petar_prisustvo","vreme_sostanok"))
    # ----------------------------------------------------

    # [print(solution) for solution in problem.getSolutions()]
    for solution in problem.getSolutions():
        buildSolution = dict()
        buildSolution["Simona_prisustvo"] = solution["Simona_prisustvo"]
        buildSolution["Marija_prisustvo"] = solution["Marija_prisustvo"]
        buildSolution["Petar_prisustvo"] = solution["Petar_prisustvo"]
        buildSolution["vreme_sostanok"] = solution["vreme_sostanok"]

        print(buildSolution)