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
    for x in rem: #
        print(x,end = "")
    print('\n')
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
        print(seq[i])
    for x in seq:
        res += x
    return(res)

def c(seqseq=[1,2,3,4,5,6,7],base=10,target=8):
    seq = seqseq.copy()
    for ind in seq:
        if ind >= base:
            print('Error: The sequence does not match the base')
            return(False)
    res = con(deci(seq,base),target)
    return(res)
