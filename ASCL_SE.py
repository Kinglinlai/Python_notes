import sys
def con(n,target=2):
    num = n
    rem = [] #
    if target <= 1:  #
        return(False) #
    while num > 0: #
        temp = num % target #
        num = num // target #
        rem.append(temp) #
    rem.reverse() #
    return(rem) #


def deci(seqseq,base=2):
    res = 0
    seq = seqseq
    seq.reverse()
    if base < 1:
        return(False)
    lenth = len(seq)
    for i in range(lenth):
        seq[i] = seq[i]*(base**i)
    for x in seq:
        res += x
    return(res)

def c(seqseq=[1,2,3,4,5,6,7],base=10,target=8):
    seq = seqseq.copy()
    for ind in seq:
        if ind >= base:
            return(False)
    res = con(deci(seq,base),target)
    return(res)

def hexaToBase10(str):
    n = ['1','2','3','4','5','6','7','8','9','0']
    h = ['A','B','C','D','E','F']
    res = 0
    for x in range(len(str)):
        if str[x] in n:
            res += int(str[x]) * (16**x)
        else:
            temp = 0
            for i in range(len(h)):
                if h[i] == str[x]:
                    res += (i+10)*(16**x)
    return(res)
        
        
        

def numTriangleGene(str):
    res = 0
    nums = []
    start = '' #s
    diff = '' #d
    line = '' #r
    swi = 1
    for x in range(len(str)):
        if str[x] == ' ':
            if swi == 1:
                swi = 2
            else:
                swi = 3
        else:
            if swi == 1:
                start += str[x]
            elif swi == 2:
                diff += str[x]
            elif swi == 3:
                line += str[x]
    start = hexaToBase10(start)
    diff = hexaToBase10(diff)
    line = int(line)
    temp = 0
    counter = 1
    while counter < line:
        temp += counter
        counter += 1
    for n in range(temp):
        nums.append(start + (diff * n))
    nums.reverse()
    i = 0
    new_nums = []
    while i < line:
        new_nums.append(nums[i])
        i += 1
    res = [new_nums,line]
    return(res)

def process(num):
    temp = con(num,16)
    while len(temp) != 1:
        seqseq = list(str(sum(temp)))
        seq = []
        for x in seqseq:
            seq.append(int(x))
        temp = seq
        print(temp)
    return(temp)
    
def main(str):
    last = numTriangleGene(str)
    last = last[0]
    summ = sum(last)
    res = process(summ)
    return(res[0] + 3)

    
    
            
            
            
            
    
    
