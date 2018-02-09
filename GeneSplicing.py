#File: GeneSplicing.py
#Coding Challenge II
#Authors: Mégane Michaud, Logan Swanson

def geneSplicing(str1, str2):
    string = str1
    flag= True
    while len(string)>0:
        if string in str2:
            flag = False
            str1=str1.replace(string, "")
            print ("yes "+str1 + str2)
            break
        string = string[1:]
    if flag:
        print ("Nope"+str1 + str2)
        
        
def main():
    geneSplicing("AACCTGT","CTGTACG")
        
main()