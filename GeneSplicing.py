#File: GeneSplicing.py
#Coding Challenge II
#Authors: Mégane Michaud, Logan Swanson

def iterative_wrapper(str1,str2):
    forward=geneSplicing(str1,str2)
    reverse=geneSplicing(str2,str1)
    
    if len(forward)<len(reverse): return forward
    else: return reverse
    

def geneSplicing(str1, str2):
    string = str1
    flag= True
    while len(string)>0:
        if string in str2:
            flag = False
            str1=str1.replace(string, "")
            return str1 + str2
            break
        string = string[1:]
    if flag:
        return str1+str2

def main():
    gene1="AACCTGT"
    gene2="CTGTACG"
    print(iterative_wrapper(gene1,gene2))

        
main()