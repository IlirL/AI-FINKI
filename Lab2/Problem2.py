from constraint import *

if __name__ == '__main__':
    problem = Problem(BacktrackingSolver())

    # ---Dadeni se promenlivite, dodadete gi domenite-----
    simonaPossibleHoursForSostanok = (13, 14, 16, 19)
    marijaPossibleHoursForSostanok = (14,15,18)
    petarPossibleHoursForSostanok = (12, 13, 16, 17,18,19)
    possibleHoursForSostanok = (12,13,14,15,16,17,18,19)

    problem.addVariable("Simona_prisustvo", simonaPossibleHoursForSostanok)
    problem.addVariable("Marija_prisustvo", marijaPossibleHoursForSostanok)
    problem.addVariable("Petar_prisustvo", petarPossibleHoursForSostanok)
    problem.addVariable("vreme_sostanok", possibleHoursForSostanok)
    # ----------------------------------------------------

    # ---Tuka dodadete gi ogranichuvanjata----------------
    problem.addConstraint(lambda a,b,c, d: (a==b and a==d) or (a==c and a==d) or(a==b and a==c and a==d), ("Simona_prisustvo", "Marija_prisustvo", "Petar_prisustvo","vreme_sostanok"))
    # problem.addConstraint(lambda a, b: a==b, ("Simona_prisustvo", "vreme_sostanok"))
    # ----------------------------------------------------

    # [print(solution) for solution in problem.getSolutions()]
    buildSolutions = []
    zafateniTermini = []
    for solution in problem.getSolutions():
        # print(solution)
        termin = solution["vreme_sostanok"]
        if termin in zafateniTermini:
            continue
        buildSolution = dict()
        if solution["Simona_prisustvo"] == solution["vreme_sostanok"]:
            buildSolution["Simona_prisustvo"] = 1
        else:
            buildSolution["Simona_prisustvo"] = 0

        if solution["Marija_prisustvo"] == solution["vreme_sostanok"]:
            buildSolution["Marija_prisustvo"] = 1
        else:
            buildSolution["Marija_prisustvo"] = 0

        if solution["Petar_prisustvo"] == solution["vreme_sostanok"]:
            buildSolution["Petar_prisustvo"] = 1
        else:
            buildSolution["Petar_prisustvo"] = 0

        buildSolution["vreme_sostanok"] = solution["vreme_sostanok"]
        zafateniTermini.append(termin)
        print(buildSolution)

