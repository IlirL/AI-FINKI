from constraint import *

if __name__ == '__main__':
    problem = Problem(BacktrackingSolver())
    variables = ["S", "E", "N", "D", "M", "O", "R", "Y"]
    for variable in variables:
        problem.addVariable(variable, Domain(set(range(10))))

    # ---Tuka dodadete gi ogranichuvanjata----------------
    problem.addConstraint(AllDifferentConstraint(), variables)
    # problem.addConstraint(lambda a,b,c:  (a+b)%10 == c, ("D", "E", "Y"))
    # problem.addConstraint(lambda a,b,c,d,e: ((int)((c+d-e)/10) + a+b)%10 == d, ("N", "R", "D", "E", "Y"))
    # problem.addConstraint(lambda a,b,c,d:((int)((c+d - a) /10) + a + b)%10 == c, ("E", "O", "N", "R"))
    # problem.addConstraint(lambda a,b,c,d,e: ((int)((c+d-e)/10)+a+b)%10==d, ("S", "M", "E", "O", "N"))
    # problem.addConstraint(lambda a:  a!=0, ("S"))
    # problem.addConstraint(lambda a: a!=0, ("M"))
    # problem.addConstraint(lambda a,b,c: (int)((a+b-c)/10) == b, ("S", "M", "O"))
    # ----------------------------------------------------
    problem.addConstraint(lambda a,b,c,d,e,f,g,h: 1000*a+100*b+10*c+d + 1000*e+100*f+10*g+b == 10000*e+1000*f+100*c+10*b+h, variables)
    print(problem.getSolution())
