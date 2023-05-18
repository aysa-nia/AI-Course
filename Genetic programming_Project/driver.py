from generateRandomfunction import *
from create_inputs import *
from fitnessFunction import *
from crossover_mutation import *
import numpy
from sympy import * 
from draw_plot import *
import csv
import random
import math
def readData(filename):
    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file,delimiter=',')
        dataset=list(csv_reader)
        columns = dataset[0]
        dataset = dataset[1:]
        for row in range(len(dataset)):
            for col in range(len(dataset[row])):
                dataset[row][col] = float(dataset[row][col])
        return dataset
def Is_Verfied(string , num_of_variable):
    countx = 0
    county = 0
    countz = 0
    if num_of_variable == 1:
        for i in string:
            if i == 'x':
                countx+=1
        if countx == 0:
            return False
        else:
            return True
    elif num_of_variable == 2:
        for i in string:
            if i == 'x':
                countx+=1
            if i == 'y':
                county+=1
        if countx == 0 and county == 0:
            return False
        else:
            return True
    else:
        for i in string:
            if i == 'x':
                countx+=1
            if i == 'y':
                county+=1
            if i == 'z':
                countz+=1
        if countx == 0 and county == 0 and countz == 0:
            return False
        else:
            return True

def Is_Variable(a):
    if a == 'x' or a == 'y' or a == 'z':
        return True
    return False

def Is_In_Correct_Form(string):
    for i in range(1 , len(string)):
        if is_operation(string[0]) or is_operation(string[len(string)-1]):
            return False
        if Is_Variable(string[i - 1]):
            if Is_Variable(string[i]):
                return False
        if string[i-1].isdigit():
            if Is_Variable(string[i]):
                return False
        if Is_Variable(string[i-1]):
            if string[i].isdigit():
                return False
    return True

result = []
best_fitness_each_generation = []
generations = []

def GeneticAlgorithm(NUMOFVAR , NAMEOFFILE ):
    x = symbols('x')
    y = symbols('y')
    GEN_SOLUTIONS_ROOT = []
    GEN_SOLUTIONS_STRINGS = []
    data_samples = readData(NAMEOFFILE)
    for i in range(0 , 100):
        exp_list = randomFunctionGenerator(0 , 10 , NUMOFVAR)
        root = buildTree(exp_list , 0 , len(exp_list) -1)
        GEN_SOLUTIONS_ROOT.append(root)
        GEN_SOLUTIONS_STRINGS.append(convert(inOrder(root)))
    for i in range(0 ,20):
        generations.append(i)
        print("Generation : " , i)
        Fintness_MSE = fitness_function(GEN_SOLUTIONS_STRINGS , GEN_SOLUTIONS_ROOT , data_samples , NUMOFVAR)
        Fintness_MSE = sorted(Fintness_MSE , key=lambda x: x[1])
        best_fitness_each_generation.append(Fintness_MSE[0][1])
        CrossOvered_items = []
        if Fintness_MSE[0][1] < 150:
            print("solution is found" , simplify(Fintness_MSE[0][0]) , Fintness_MSE[0][1] , "in generation " , i)
            result.append(Fintness_MSE[0][0])
        i_20percent = (int)(len(Fintness_MSE) * 0.2)
        first_best_20percent = []
        for i in range(0 , i_20percent):
            first_best_20percent.append(Fintness_MSE[i][0])
        sum_fitness = 0
        probability = []
        previous_probability = 0
        for j in range(len(Fintness_MSE)):
            sum_fitness+=Fintness_MSE[j][1]
        for j in range(len(Fintness_MSE)):
            probability.append((previous_probability + ( 1 - (Fintness_MSE[j][1] / sum_fitness)) , Fintness_MSE[j]))
            previous_probability = probability[j][0]
        for i in range(50): 
            n = random.uniform(0 , 100)
            m = random.uniform(0 ,100)
            for i in range(len(probability) - 1):
                if  probability[i][0] < n < probability[i+1][0] :
                    a = probability[i][1][0]
                elif probability[i][0] < m < probability[i+1][0] :
                    b = probability[i][1][0]
            new_stringA , new_stringB = CrossOver(a,b)
            CrossOvered_items.append(new_stringA)
            CrossOvered_items.append(new_stringB)
        Mutated_items = []
        for item in CrossOvered_items:
            new_item = Mutation(item)
            if Is_Verfied(new_item , NUMOFVAR) and Is_In_Correct_Form(new_item):
                Mutated_items.append(new_item)
        for i in first_best_20percent:
            Mutated_items.append(i)
        GEN_SOLUTIONS_STRINGS = Mutated_items
    if len(result) == 0:
        print("nothing found")


NUMOFVAR = int(input("number of variables :"))
function = input("enter function :")
csv_creator(function , NUMOFVAR , 100 , "test.csv")
NAMEOFFILE = 'test.csv'
x1 = []
x2 = []
y1 = []
y2 = []
data_samples = readData(NAMEOFFILE)
GeneticAlgorithm(NUMOFVAR , NAMEOFFILE)

if NUMOFVAR == 1 and len(result) != 0 :
    print("*******************************")
    print("The correct and final solution is :" , simplify(result[len(result)-1]))
    for i in range(len(data_samples)):
        x1.append(data_samples[i][0])
        y1.append(data_samples[i][1])
    for i in range(len(data_samples)):
        y2.append(eval(result[len(result)-1] , {} , {'x' : data_samples[i][0]}))
    draw_2plot(x1 , y1 , x1 , y2)
    draw_curved_plot(generations , best_fitness_each_generation)
elif NUMOFVAR == 2 and len(result) != 0  :
    print("*******************************")
    print("The correct and final solution is :" , simplify(result[len(result)-1]))
    for i in range(len(data_samples)):
        x1.append(data_samples[i][0])
        x2.append(data_samples[i][1])
        y1.append(data_samples[i][2])
    xy = list(zip(x1 , x2))
    for i in range(len(data_samples)):
        y2.append(eval( result[len(result)-1], {} , {'x' : data_samples[i][0] , 'y' : data_samples[i][1]}))
    draw_2plot(xy , y1 , xy , y2)
    draw_curved_plot(generations , best_fitness_each_generation)
else:
    draw_curved_plot(generations , best_fitness_each_generation)











