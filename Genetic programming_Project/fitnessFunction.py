from sklearn.metrics import mean_squared_error
from generateRandomfunction import *
from crossover_mutation import *

def fitness_function(solutions_string , gen_root , data_samples , num_of_variables):
    solutions = []
    Real_solutions = []
    for s in solutions_string:
        s_sol = []
        if num_of_variables == 1:
            for i in range(0 , len(data_samples)):
                try:
                    exec(s , {} , {'x' : data_samples[i][0]})
                except ZeroDivisionError:
                    s_list = randomFunctionGenerator(1 , 1000 , num_of_variables)
                    root = buildTree(s_list , 0 , len(s_list) -1)
                    s = convert(inOrder(root))
                s_sol.append(eval(s , {} , {'x' : data_samples[i][0]}))
        elif num_of_variables == 2:
            for i in range(0 , len(data_samples)):
                try:
                    exec(s , {} , {'x' : data_samples[i][0] , 'y' : data_samples[i][1]})
                except ZeroDivisionError:
                    s_list = randomFunctionGenerator(1 , 1000 , num_of_variables)
                    root = buildTree(s_list , 0 , len(s_list) -1)
                    s = convert(inOrder(root))
                s_sol.append(eval(s , {} , {'x' : data_samples[i][0] , 'y' : data_samples[i][1]}))
        else:
            for i in range(0 , len(data_samples)):
                try:
                    exec(s , {} , {'x' : data_samples[i][0] , 'y' : data_samples[i][1] , 'z' : data_samples[i][2]})
                except ZeroDivisionError:
                    s_list = randomFunctionGenerator(1 , 1000 , num_of_variables)
                    root = buildTree(s_list , 0 , len(s_list) -1)
                    s = convert(inOrder(root))
                s_sol.append(eval(s , {} , {'x' : data_samples[i][0] , 'y' : data_samples[i][1] , 'z' : data_samples[i][2]}))
        solutions.append(s_sol)
    for i in range(0 , len(data_samples)):
        Real_solutions.append(data_samples[i][num_of_variables])
    MSE_total = []
    for i in range(len(solutions)):
        MSE_total.append((solutions_string[i] , mean_squared_error(Real_solutions , solutions[i])))
    return MSE_total





