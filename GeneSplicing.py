#File: GeneSplicing.py
#Coding Challenge II
#Authors: Mégane Michaud, Logan Swanson

def iterative_wrapper(str1,str2):
	'''returns the shortest string such that both str1 and str2 are substrings'''
    #check both directions
	forward=iterative_splicing(str1,str2)
	reverse=iterative_splicing(str2,str1)
	
	if len(forward)<len(reverse): 
		return forward
	else: 
		return reverse
    

def iterative_splicing(str1, str2):
	'''takes two strings and returns the string resulting from their maximum amount of overlap'''
    #if str1 is already a substring of str2, DONE
	if str1 in str2: return str2
	string = str1
	while len(string)>0:
        #overlap found
		if string==str2[0:len(string)]:
			str1=str1.replace(string, "",1)
			return str1 + str2
		string = string[1:]
    #no overlap found--just conjoin
	return str1+str2

def main():
    gene1 = input("Input the first gene: ").upper()   
    gene2 = input("Input the second gene: ").upper()
    check_string(gene1)
    check_string(gene2)
    print_out(iterative_wrapper(gene1,gene2),gene1,gene2)

def check_string(str1):
    '''checks to see if str1 is a valid input'''
    accepted = ['A','C','G','T']
    for char in str1:
        if not char in accepted:
            raise Exception("invalid input")
            
def print_out(shorter, str1, str2):   
	'''prints out results in a neatly formatted way'''
	print ("********************************************")
	print ("string 1 - "+str1+"    string 2 - "+str2)
	print("shortest string that has both as substring")
	print(shorter + "\t(length "+str(len(shorter))+")")
	print ("********************************************")  
            
main()