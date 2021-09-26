import random
#import matplotlib.pyplot as plt
# single choose
def sif(ur = 0.01, ssr = 0.04, sr = 0.15, r = 0.8, specifier = 1000):
    poolur = ['UR'] * int(ur * specifier)
    poolssr = ['SSR'] * int(ssr * specifier)
    poolsr = ['SR'] * int(sr * specifier)
    poolr = ['R'] * int(r * specifier)
    pool = poolur + poolssr + poolsr + poolr
    result = random.choice(pool)
    return(result)
# 11
def sif11(times = 11):
    swi = times
    c = []
    while swi > 0:
        temp = sif()
        c.append(temp)
        swi -= 1
    cUR = c.count('UR')
    cSSR = c.count('SSR')
    cSR = c.count('SR')
    cR = c.count('R')
    #result = ('There are %s UR, %s SSR, %s SR and %s R' % (cUR,cSSR,cSR,cR))
    #print(result)
    return(cUR)
        
# box
def box():
    ur = ['UR']
    ssr = ['SSR']*4
    sr = ['SR']*15
    r = ['R']*80
    total = ur + ssr + sr +r
    count = 0
    swi = True
    while swi == True:
        temp = sif()
        if total != [] and temp != 'UR':
            if temp in total:
                total.remove(temp)
                count += 1
        elif temp == 'UR':
            return(count)
        elif total == []:
            return(False)
    
# verifier
def sif_veri(count):
    swi = True
    t = count
    cUR = 0
    cSSR = 0
    cSR = 0
    while swi == True:
        temp = sif()
        if temp == 'UR':
            cUR += 1
        elif temp == 'SSR':
            cSSR += 1
        elif temp == 'SR':
            cSR += 1
        t -= 1
        if t <= 0:
            swi = False
    ur = str(cUR / count)
    ssr = str(cSSR / count)
    sr = str(cSR / count)
    print('The UR rate is %s ; The SSR rate is %s ; SR rate is %s' % (ur,ssr,sr))
    return(None)

def loveca(loveca,will = 1,proximitynum = 200):
    times = (loveca / 50) * 11
    if loveca < 50:
        print('You donnot have enough loveca for it!')
        return(False)
    t = proximitynum
    count = 0
    highest = 0
    while t > 0:
        temp = sif11(times)
        if temp >= will:
            count += 1
        if temp > highest:
            highest = temp
        t -= 1
    result = (count / proximitynum) * 100
    print('The chances that you get at least %s UR with %s loveca is %s percent' % (will,loveca,result))
    print('The best shot gives you %s UR' % (highest))
    return(result)

##def loveca_plot(maxi_loveca,willl,proximi = 300,delta = 50):
##    #
##    #
##    maxi = maxi_loveca #
##    init = 50 #
##    swi = init #
##    
##    x = [] #
##    y = [] #
##    
##    while maxi > swi: #
##        x.append(swi) #
##        temp = loveca(swi,willl,proximi) #
##        y.append(temp) #
##        swi += delta #
##    
##    plt.plot(x,y,linewidth = 5) #
##    plt.title('Loveca with chances getting %s UR' % willl) #
##    plt.xlabel('loveca used') #
##    plt.ylabel('estimated rate with %s UR' % willl) #
##
##    plt.show() #
    
    
    

    
def box_veri(count):
    swi = True
    x = 0
    t = count
    while swi == True:
        temp = box()
        x += temp
        t -= 1
        if t <= 0:
            swi = False
    result = x / count
    return(result)
    
