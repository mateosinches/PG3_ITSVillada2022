from operator import index 
import string 

def EncontarNum(numero, my_list):
    return(my_list.index(numero))

numero=int(input())
my_list = [47,5,10,8,19,50,1]
print (EncontarNum(numero))