'''
Created on 2018. 9. 14.

@author: DPain
'''

def isDigitsPunct(string):
    from string import punctuation
    
    for i in range(0, len(string)):
        if not string[i].isdigit() and not string[i] in punctuation:
            return False
        
    return True