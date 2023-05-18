import random
import math
from inorder_to_tree import *

def is_operation(op):
    if op == '+' or op =='-' or op == '*' or op == '/' or op =='**':
        return True
    return False

def CrossOver( stringA , stringB):
    idxA = random.randint(0 , min(len(stringA) , len(stringB)) -1 )
    idxB = random.randint(0 , min(len(stringA) , len(stringB)) -1 )
    while not is_operation(stringA[idxA]) :
        if min(len(stringA) , len(stringB))==1:
            break
        idxA = random.randint(0 , min(len(stringA ), len(stringB)) -1)
    while not is_operation(stringB[idxB]) :
        if min(len(stringA) , len(stringB))==1:
            break
        idxB = random.randint(0 , min(len(stringA) , len(stringB)) -1)
    tmpA_1 = stringA[:idxA + 1]
    tmpA_2 = stringB[0:idxB]
    if tmpA_1 == '' or tmpA_1 == ' ' or tmpA_2 == ' ' or tmpA_2 == '':
        tmpstringA = stringA
    else:
        tmpstringA = tmpA_1 + tmpA_2
    tmpB_2 = stringA[idxA +1:]
    tmpB_1 = stringB[idxB:]
    if tmpB_1 == '' or tmpB_1 == ' ' or tmpB_2 == ' ' or tmpB_2 == '':
        tmpstringB = stringB
    else:
        tmpstringB = tmpB_2 + tmpB_1
    return  tmpstringA ,  tmpstringB

def swap(a , b):
    tmp = a
    a = b
    b = tmp

OP_LIST = ['*' , '+' , '-' , '/'  , '**']
def Mutation(stringA):
    idx2 = random.randint(0 , 3)
    if len(stringA) <=1:
        return stringA
    idx1 = random.randint(0 , len(stringA ) -1)
    while not is_operation(stringA[idx1]):
        idx1 = random.randint(0 , len(stringA ) -1)
    while stringA[idx1] == OP_LIST[idx2]:
        idx2 = random.randint(0 , 3)
    return stringA.replace(stringA[idx1], OP_LIST[idx2])


