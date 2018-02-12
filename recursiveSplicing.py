#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  9 14:14:49 2018

@author: Logan
"""
accepted = ['A','C','G','T']    

def recursive_wrapper(gene1, gene2):
    '''wrapper for genesplicer that cuts strings down to matching lengths'''
    #if one is already a substring of the other--DONE
    if gene1 in gene2: return gene2
    if gene2 in gene1: return gene1
    
    #clean up strings so they are same length
    if len(gene1)==len(gene2): 
        forward= recursive_splicing(gene1,gene2)
        reverse=recursive_splicing(gene2,gene1)
    elif len(gene1)>len(gene2):
        forward=gene1[:-len(gene2)]+recursive_splicing(gene1[-len(gene2):],gene2)
        reverse=recursive_splicing(gene2,gene1[:len(gene2)])+gene1[len(gene2):]
    else:
        forward=recursive_splicing(gene1,gene2[:len(gene1)])+gene2[len(gene1):]
        reverse=gene2[:-len(gene1)]+recursive_splicing(gene2[-len(gene1):],gene1)
        
    if len(forward)<len(reverse): return forward
    else: return reverse
    
def recursive_splicing(gene1, gene2):
    '''takes two strings of the same length and returns the splicing'''
    #base case: complete overlap
    if gene1==gene2: return gene1
    #base case: reached end of string
    if len(gene1)<=1: return gene1+gene2
    else:
        return gene1[0] + recursive_splicing(gene1[1:],gene2[:-1]) + gene2[-1]
        
        
def main():
    gene1="CGA"
    gene2="GCTGTACGA"
    check_string(gene1)
    check_string(gene2)
    print(recursive_wrapper(gene1,gene2))
    
def check_string(str1):
    '''checks to see if str1 is a valid input'''
    for char in str1:
        if not char in accepted:
            raise Exception("invalid input")
    
main()