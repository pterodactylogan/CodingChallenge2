#File: GeneSplicing.py
#Coding Challenge II
#Authors: Mégane Michaud, Logan Swanson

accepted = ['A','C','G','T']

def iterative_wrapper(str1,str2):
    forward=iterative_splicing(str1,str2)
    reverse=iterative_splicing(str2,str1)
    
    if len(forward)<len(reverse): return forward
    else: return reverse
    

def iterative_splicing(str1, str2):
    if str1 in str2: return str2
    string = str1
    while len(string)>0:
        if string==str2[0:len(string)]:
            str1=str1.replace(string, "")
            return str1 + str2
        string = string[1:]
    return str1+str2

def main():
    gene1="AACTGT"
    gene2="GCTGTACGA"
    check_string(gene1)
    check_string(gene2)
    print(iterative_wrapper(gene1,gene2))

def check_string(str1):
    '''checks to see if str1 is a valid input'''
    for char in str1:
        if not char in accepted:
            raise Exception("invalid input")
            
main()