#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  9 14:14:49 2018

@author: Logan
"""
debug=False
level=0

def printdecorator(func):
    def wrapper(*args, **kwargs):
        return func(level*"\t",*args, **kwargs)
    return wrapper

if debug: print = printdecorator(print)

def printdebugger(func):
    if not debug: return func
    def wrapper(*args, **kwargs):
        global level
        print("Enter function: "+func.__name__+str(args))
        level+=1
        results=func(*args,**kwargs)
        level-=1
        print("Exit function: "+func.__name__)
        return results
    return wrapper

@printdebugger      
def wrapper(gene1, gene2):
    '''wrapper for genesplicer that cuts strings down to matching lengths'''
    if len(gene1)==len(gene2): return recursive_splicing(gene1,gene2)
    elif len(gene1)>len(gene2):
        forward=gene1[:-len(gene2)]+recursive_splicing(gene1[-len(gene2):],gene2)
        reverse=recursive_splicing(gene2,gene1[:len(gene2)])+gene1[len(gene2):]
    else:
        forward=recursive_splicing(gene1,gene2[:len(gene1)])+gene2[len(gene1):]
        reverse=gene2[:-len(gene1)]+recursive_splicing(gene2[-len(gene1):],gene1)
        
    if len(forward)<len(reverse): return forward
    else: return reverse
    
@printdebugger
def recursive_splicing(gene1, gene2):
    '''takes two strings of the same length and returns the splicing'''
    if gene1==gene2: return gene1
    if len(gene1)<=1: return gene1+gene2
    else:
        return gene1[0] + recursive_splicing(gene1[1:],gene2[:-1]) + gene2[-1]
        
        
def main():
    gene1="AACCTGT"
    gene2="GCTGTACGA"
    print(wrapper(gene1,gene2))
    
main()