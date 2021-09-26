from random import *


options = """
################################
# Welcome to the Pyencripter   #
#[0] Help                      #
#[1] Default Setting           #
#[2] UpCase                    #
#[3] LowCase                   #
#[4] Numbers                   #
#[5] Quit                      #
################################
"""

def main():
    #Intialize nums sequence
    nums = []
    for i in range(100):
        nums.append(str(i))
    print(options)
    swi = True
    res = []
    
    while swi == True:
        opt = input('Please enter your choice')

        
        if opt == '0':
            print(options)
            
        elif opt == '1':
            length = input("Length of Password???")
            while length not in nums:
                length = input('Plz retry')
            length = int(length)
            x = genePass(length,"Default")
            res.append(x)
            
        elif opt == '2':
            length = input("Length of Password???")
            while length not in nums:
                length = input('Plz retry')
            length = int(length)
            x = genePass(length,"UpCase")
            res.append(x)
            
        elif opt == '3':
            length = input("Length of Password???")
            while length not in nums:
                length = input('Plz retry')
            length = int(length)
            x = genePass(length,"LowCase")
            res.append(x)
            
        elif opt == '4':
            length = input("Length of Password???")
            while length not in nums:
                length = input('Plz retry')
            length = int(length)
            x = genePass(length,"Number")
            res.append(x)
            
        elif opt == '5':
            swi = False
            
        else:
            print("Invalid Input, Retry")
            
    for t in res:
        print(t)
    

def genePass(length,mode = 'Default'):
    minim = 48
    maxim = 122
    
    if mode == 'Default':
        minim = 48
        maxim = 122
        
    elif mode == 'LowCase':
        minim = 97
        maxim = 122
        
    elif mode == 'UpCase':
        minim = 65
        maxim = 90
        
    elif mode == "Number":
        minim = 48
        maxim = 57
        
    i = length
    res = ""
    
    while i > 0:
        res += geneAword(minim,maxim)
        i -= 1
        
    return(res)

def geneAword(minim = 48,maxim = 122):
    random = randint(minim,maxim)
    return(chr(random))
