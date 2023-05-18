import csv
import random
import math
# this works only for equation with maximum of 3 variables
def csv_creator(function , num_of_variables , num_of_tests , csv_filename):
    var_name = ["x" , "y" , "z"]
    fieldnames = []
    rows = []
    for i in range(0 , num_of_variables):
        fieldnames.append(var_name[i])
    fieldnames.append("f")
    for i in range(1 , num_of_tests+1):
        data=[]
        variables = []
        for i in range(0 , num_of_variables ):
            value = random.randint(-100,100)
            while(value == 0):
                value = random.randint(0,100)
            variables.append(value)
            data.append(value)
        new_dict = {}
        for j in range(0 , num_of_variables):
            new_dict[fieldnames[j]] = variables[j]
        data.append(eval(function , {} , new_dict))
        rows.append(data)
    f = open(csv_filename, 'w', newline='')
    writer = csv.writer(f)
    writer.writerow(fieldnames)
    writer.writerows(rows)
    f.close()
def csv_creator_sin(num_of_variables , num_of_tests , csv_filename):
    var_name = ["x" , "y" , "z"]
    fieldnames = []
    rows = []
    for i in range(0 , num_of_variables):
        fieldnames.append(var_name[i])
    fieldnames.append("f")
    for i in range(1 , num_of_tests+1):
        data=[]
        variables = []
        for i in range(0 , num_of_variables ):
            value = random.randint(-100,100)
            while(value == 0):
                value = random.randint(0,100)
            variables.append(value)
            data.append(value)
        new_dict = {}
        for j in range(0 , num_of_variables):
            new_dict[fieldnames[j]] = variables[j]
        data.append(math.sin(new_dict[fieldnames[j]]))
        rows.append(data)
    f = open(csv_filename, 'w', newline='')
    writer = csv.writer(f)
    writer.writerow(fieldnames)
    writer.writerows(rows)
    f.close()

# csv_creator("x + 100" , 1 , 100 , "test1.csv")
# csv_creator("x * 2 + y + 5" , 2 , 100 , "test2.csv")
# csv_creator("2*x + 50" , 1 , 100 , "test3.csv" )
# csv_creator("x**2 + 2*x + 4" , 1 ,100 , "test4.csv")
# csv_creator("x - 2 + 5*y + 2*z" ,3, 100 , "test5.csv")
# csv_creator_sin(1 , 100 , "test6.csv")


