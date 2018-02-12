#File: GeneSplicing.py
#Coding Challenge II
#Authors: Mégane Michaud, Logan Swanson

def iterative_wrapper(str1,str2):
    forward=geneSplicing(str1,str2)
    reverse=geneSplicing(str2,str1)
    
    if len(forward)<len(reverse): return forward
    else: return reverse
    

def geneSplicing(str1, str2):
    if str1 in str2: return str2
    string = str1
    while len(string)>0:
        if string==str2[0:len(string)]:
            str1=str1.replace(string, "")
            return str1 + str2
        string = string[1:]
    return str1+str2

def main():
    gene1="AACCTGT"
    gene2="GCTGTACGA"
    print(iterative_wrapper(gene1,gene2))

        
main()