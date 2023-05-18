import random
from inorder_to_tree import *

OPERATIONS = ["+","-","*","/","**"]
VARNAME = ["x","y","z"]
def randomFunctionGenerator(start:int, end:int, num_of_variables:int):
    count_of_elements = random.randint(1 , 10)
    elements = []
    count_variables = {"x" : 0 , "y" : 0 ,"z" :0}
    pre_flag = 10
    for i in range(0 , count_of_elements):
        # 0 -> add variable , 2 -> add operation , 1 -> add number
        if i == 0 :
            flag = random.randint(0,1)
            if flag == 0:
                if num_of_variables == 3:
                    idx = random.randint(0,2)
                    elements.append(VARNAME[idx])
                    count_variables[VARNAME[idx]]+=1
                elif num_of_variables == 2:
                    idx = random.randint(0,1)
                    elements.append(VARNAME[idx])
                    count_variables[VARNAME[idx]]+=1
                else:
                    elements.append(VARNAME[0])
                    count_variables[VARNAME[0]]+=1
            else:
                elements.append(str(random.randint(start,end)))
            pre_flag = flag
        elif i == count_of_elements -1 :
            if pre_flag != 0 and pre_flag != 1:
                flag = random.randint(0,1)
            else:
                break
            if flag == 0:
                if num_of_variables == 3:
                    idx = random.randint(0,2)
                    elements.append(VARNAME[idx])
                    count_variables[VARNAME[idx]]+=1
                elif num_of_variables == 2:
                    idx = random.randint(0,1)
                    elements.append(VARNAME[idx])
                    count_variables[VARNAME[idx]]+=1
                else:
                    elements.append(VARNAME[0])
                    count_variables[VARNAME[0]]+=1
            else:
                elements.append(str(random.randint(start,end)))
        else:
            if pre_flag == 1:
                flag = 2
            elif pre_flag == 0 :
                flag = 2
            else:
                flag = random.randint(0,1)
            if flag == 0:
                if num_of_variables == 3:
                    idx = random.randint(0,2)
                    elements.append(VARNAME[idx])
                    count_variables[VARNAME[idx]]+=1
                elif num_of_variables == 2:
                    idx = random.randint(0,1)
                    elements.append(VARNAME[idx])
                    count_variables[VARNAME[idx]]+=1
                else:
                    elements.append(VARNAME[0])
                    count_variables[VARNAME[0]]+=1
            elif flag ==1:
                elements.append(str(random.randint(start,end)))
            else:
                elements.append(OPERATIONS[random.randint(0,3)])
            pre_flag = flag
    if num_of_variables == 3:
        if count_variables["x"] == 0:
            elements.append(OPERATIONS[random.randint(0,3)])
            elements.append("x")
        if count_variables["y"] == 0:
            elements.append(OPERATIONS[random.randint(0,3)])
            elements.append("y")
        if count_variables["z"] == 0:
            elements.append(OPERATIONS[random.randint(0,3)])
            elements.append("z")
    if num_of_variables == 2:
        if count_variables["x"] == 0:
            elements.append(OPERATIONS[random.randint(0,3)])
            elements.append("x")
        if count_variables["y"] == 0:
            elements.append(OPERATIONS[random.randint(0,3)])
            elements.append("y")
    if num_of_variables == 1:
        if count_variables["x"] == 0:
            elements.append(OPERATIONS[random.randint(0,3)])
            elements.append("x")
    return elements

def convert(s):
        new = ""
        for x in s:
            new += x
        return new


